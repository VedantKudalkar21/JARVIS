from datetime import datetime, timedelta

event_time = "2024-03-19T12:30:45"
event_time_obj = datetime.strptime(event_time, "%Y-%m-%dT%H:%M:%S")

print(event_time_obj)  # Should print a valid datetime object
