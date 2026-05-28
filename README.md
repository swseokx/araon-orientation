# ARAON Orientation

ARAON Orientation is the first-day OT/orientation workflow tool.

## Ownership

This app contains only first-day OT/orientation workflows while shared infrastructure lives in `araon-core`.

Orientation-owned areas:

- orientation dashboard
- OT time groups and alarms
- checklist management
- orientation LMS save
- orientation sheet update
- timetable assignment and clipboard text
- admission/orientation logs

Not included:

- opening/AS dashboard
- AS templates/manual AS add
- setup work sidebar
- Kakao quick workflow

## Install Dependencies

```bat
python -m pip install -r requirements.txt
```

## Run

```bat
python admission.py
```
