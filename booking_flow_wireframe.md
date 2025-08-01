# Booking Flow Wireframe

---

## Step 1: Location Selection

```
-------------------------------------------------------
| Book a Token                                         |
-------------------------------------------------------
| 📍 Auto-detect location [On/Off]                     |
| OR                                                   |
| [State  ▼]  [District  ▼]  [City  ▼]                |
-------------------------------------------------------
|                          [Next]                     |
-------------------------------------------------------
```

---

## Step 2: Speciality Selection

```
-------------------------------------------------------
| Select Speciality                                    |
-------------------------------------------------------
| [ Pediatrics ] [ Surgeon ] [ General Medicine ]      |
| [ Orthopedics ] [ Dermatology ] [ ENT ] ...          |
| (Rectangular, card-style buttons—one per specialty)  |
-------------------------------------------------------
| [Back]                       [Next]                 |
-------------------------------------------------------
```

---

## Step 3: Doctor List

```
-------------------------------------------------------
| Select Doctor                                        |
-------------------------------------------------------
| --------------------------------------------------- |
| Dr. Anjali Rao   (MBBS, MD Pediatrics)              |
| Time: 10am–2pm, 4pm–6pm                             |
| Tokens Today: 20   Left: 5                          |
| [Book Token]   [📍 Location Link]                    |
| --------------------------------------------------- |
| Dr. Suraj Mehta   (MS General Surgery)              |
| Time: 11am–3pm                                      |
| Tokens Today: 15   Left: 2                          |
| [Book Token]   [📍 Location Link]                    |
| --------------------------------------------------- |
| ... more doctors ...                                |
-------------------------------------------------------
| [Back]                                               |
-------------------------------------------------------
```
- Each doctor is in a card/rectangle with:
  - Name & qualifications
  - Consultation times
  - Total tokens issued today, number left
  - [Book Token] button
  - Location link (opens map)

---

# Notes:
- All steps have consistent header and navigation.
- Optional: Add a progress bar (Step 1 of 3, etc.) for better UX.
- Doctor list is scrollable if many doctors match.