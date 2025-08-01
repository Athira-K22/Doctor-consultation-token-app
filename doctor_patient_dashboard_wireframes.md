# Doctor Consultation Token App – Wireframe

---

## **Patient Dashboard**

```
-----------------------------------------------
|  Doctor Consultation Token App              |
-----------------------------------------------
| Doctor: Dr. [Name]     Status: [Active 🔵]  |
-----------------------------------------------

[Your Token]: 7              [Tokens Today]: 12

-----------------------------------------------
|  Live Queue                                 |
|---------------------------------------------|
| Token | Patient Name | Status    | ETA      |
|-------|--------------|-----------|----------|
|  5    | John Doe     | Completed | 09:40 AM |
|  6    | Jane Smith   | Skipped   | --       |
|  7    | [You]        | Waiting   | 10:10 AM |
|  8    | Ali Khan     | Checked-In| 10:20 AM |
|  9    | Sita Patel   | Absent    | --       |
-----------------------------------------------

[  Check-In Button  ]   [ Estimated Wait: 30 min ]

-----------------------------------------------
| Notifications                               |
|---------------------------------------------|
| 🔔 Doctor is now on break                   |
| 🔔 Token 6 was skipped                      |
| 🔔 Your turn is approaching!                |
-----------------------------------------------
```

---

## **Doctor/Admin Dashboard**

```
------------------------------------------------
|  Doctor Consultation Token App               |
------------------------------------------------
| Doctor: Dr. [Name]     Status: [Active 🔵]   |
|  [Start Consultation] [Break] [Emergency]    |
------------------------------------------------

[ Total Tokens Today: 12 ]   [ Now Serving: 7 ]

------------------------------------------------
|  Token Queue Overview                        |
|----------------------------------------------|
| Token | Patient Name | Checked In | Status   |
|-------|--------------|------------|----------|
|  5    | John Doe     | ✔️         | Done     |
|  6    | Jane Smith   | ❌         | Skipped  |
|  7    | Ali Khan     | ✔️         | Now      |
|  8    | Sita Patel   |            | Waiting  |
|  9    | (free)       |            | —        |
------------------------------------------------

[ Set Current Token:  [7 ▼] ]    [ Skip ] [ Complete ]

------------------------------------------------
| Attendance & Alerts                          |
|----------------------------------------------|
| ✔️  Patient 7 checked in                     |
| ❌  Patient 6 absent — skipped               |
| ⏱️  Avg. consult time: 12 min                |
| ⚠️  Emergency: Dr. called away               |
------------------------------------------------
```