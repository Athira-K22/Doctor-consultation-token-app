from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timedelta

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DoctorStatus:
    def __init__(self):
        self.status = 'Not Started'  # Not Started, Available, Away
        self.started_at = None
        self.away_reason = ''

    def start(self):
        self.status = 'Available'
        self.started_at = datetime.now()
        self.away_reason = ''

    def go_away(self, reason):
        self.status = 'Away'
        self.away_reason = reason

    def come_back(self):
        self.status = 'Available'
        self.away_reason = ''

    def status_str(self):
        if self.status == 'Available' and self.started_at:
            return f"Available (Started at {self.started_at.strftime('%H:%M')})"
        elif self.status == 'Away':
            return f"Away ({self.away_reason})"
        else:
            return self.status

class TokenSystem:
    def __init__(self):
        self.tokens_issued = 0
        self.tokens_present = set()
        self.current_token = None
        self.token_times = {}  # token: (start_time, end_time)

    def issue_token(self):
        self.tokens_issued += 1
        return self.tokens_issued

    def mark_present(self, token):
        self.tokens_present.add(token)

    def mark_not_arrived(self, token):
        self.tokens_present.discard(token)

    def start_consultation(self, token):
        self.current_token = token
        self.token_times[token] = [datetime.now(), None]

    def end_consultation(self, token):
        if token in self.token_times:
            self.token_times[token][1] = datetime.now()
        self.current_token = None

    def get_not_arrived_tokens(self):
        return [t for t in range(1, self.tokens_issued+1) if t not in self.tokens_present]

class ConsultationStats:
    def __init__(self, token_system):
        self.token_system = token_system

    def avg_consult_time(self):
        times = [et - st for st, et in self.token_system.token_times.values() if st and et]
        if times:
            avg = sum([t.total_seconds() for t in times]) / len(times)
            return timedelta(seconds=int(avg))
        return timedelta(minutes=0)

    def est_wait_time(self, next_token):
        avg = self.avg_consult_time()
        if avg.total_seconds() == 0:
            return 'Unknown'
        tokens_ahead = [t for t in self.token_system.tokens_present if t < next_token]
        return str(avg * len(tokens_ahead))

doctor = DoctorStatus()
tokens = TokenSystem()
stats = ConsultationStats(tokens)

@app.get("/")
def read_root():
    return RedirectResponse(url="/static/index.html")

@app.get("/status")
def get_status():
    return {
        "doctor_status": doctor.status_str(),
        "current_token": tokens.current_token,
        "tokens_issued": tokens.tokens_issued,
        "tokens_present": sorted(list(tokens.tokens_present)),
        "tokens_not_arrived": tokens.get_not_arrived_tokens(),
        "avg_consult_time": str(stats.avg_consult_time()),
    }

@app.post("/doctor/start")
def doctor_start():
    doctor.start()
    return {"ok": True}

@app.post("/doctor/away")
async def doctor_away(request: Request):
    data = await request.json()
    reason = data.get('reason', 'Away')
    doctor.go_away(reason)
    return {"ok": True}

@app.post("/doctor/back")
def doctor_back():
    doctor.come_back()
    return {"ok": True}

@app.post("/token/issue")
def issue_token():
    token = tokens.issue_token()
    return {"token": token}

@app.post("/token/arrive/{token}")
def token_arrive(token: int):
    tokens.mark_present(token)
    return {"ok": True}

@app.post("/token/not-arrived/{token}")
def token_not_arrived(token: int):
    tokens.mark_not_arrived(token)
    return {"ok": True}

@app.post("/consult/start/{token}")
def consult_start(token: int):
    tokens.start_consultation(token)
    return {"ok": True}

@app.post("/consult/end/{token}")
def consult_end(token: int):
    tokens.end_consultation(token)
    return {"ok": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
