import time
from datetime import datetime, timedelta

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

    def mark_absent(self, token):
        self.tokens_present.discard(token)

    def start_consultation(self, token):
        self.current_token = token
        self.token_times[token] = [datetime.now(), None]

    def end_consultation(self, token):
        if token in self.token_times:
            self.token_times[token][1] = datetime.now()
        self.current_token = None

    def get_absent_tokens(self):
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

def print_status(doctor, tokens, stats):
    print("\nClinic Consultation Status\n-------------------------")
    print(f"Doctor Status: {doctor.status_str()}")
    print(f"Current Token: {tokens.current_token}")
    print(f"Tokens Issued: {tokens.tokens_issued}")
    print(f"Tokens Present: {sorted(tokens.tokens_present)}")
    print(f"Tokens Absent: {tokens.get_absent_tokens()}")
    avg_time = stats.avg_consult_time()
    print(f"\nAverage Consultation Time: {avg_time if avg_time.total_seconds() else 'N/A'}")
    if tokens.current_token:
        print(f"Doctor is currently consulting token {tokens.current_token}.")
    else:
        print(f"Doctor is waiting for next patient.")

# --- Sample Simulation ---
if __name__ == "__main__":
    doctor = DoctorStatus()
    tokens = TokenSystem()
    stats = ConsultationStats(tokens)

    # Issue tokens 1-10
    for _ in range(10):
        tokens.issue_token()

    # Tokens 1,2,3,5,6,8,9 are present
    for t in [1,2,3,5,6,8,9]:
        tokens.mark_present(t)

    # Doctor starts consultation
    doctor.start()
    tokens.start_consultation(5)
    time.sleep(1)  # Simulate consultation time
    tokens.end_consultation(5)

    # Start consultation with token 6
    tokens.start_consultation(6)
    time.sleep(1)
    tokens.end_consultation(6)

    # Doctor goes away for emergency
    doctor.go_away('Emergency call')

    print_status(doctor, tokens, stats)
