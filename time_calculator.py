# Time Calculator solution for freeCodeCamp Scientific Computing with Python certification

def add_time(start, duration, starting_day=None):
    st_am_pm = start.split()
    st_h, st_m = st_am_pm[0].split(":")

    # conversion to minute time
    if st_am_pm[1] == "AM":
        if st_h == "12":
            minute_time = int(st_m)
        else:
            minute_time = int(st_h) * 60 + int(st_m)
    else:
        if st_h == "12":
            minute_time = int(st_h) * 60 + int(st_m)
        else:
            minute_time = (int(st_h) + 12) * 60 + int(st_m)

    dur = duration.split(":")
    duration_in_minutes = int(dur[0]) * 60 + int(dur[1])

    # new time calculation
    new_time = minute_time + duration_in_minutes
    conver_time = new_time % (24 * 60)

    # conversion to am/pm time
    if conver_time < 60:
        new_h = 12
        new_m = conver_time
        am_pm = "AM"
    elif conver_time < 720:
        new_h = conver_time // 60
        new_m = conver_time % 60
        am_pm = "AM"
    elif conver_time < 780:
        new_h = conver_time // 60
        new_m = conver_time % 60
        am_pm = "PM"
    else:
        new_h = (conver_time - 12 * 60) // 60
        new_m = conver_time % 60
        am_pm = "PM"

    if new_time < 1440:
        number_of_days = 0
    else:
        number_of_days = new_time // 1440

    # final format
    if starting_day:
        days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
        for key, value in days.items():
            if starting_day.lower() == value.lower():
                day_index = key

        if number_of_days == 0:
            return f"{new_h}:{new_m:02d} {am_pm}, {days[day_index]}"
        elif number_of_days == 1:
            return f"{new_h}:{new_m:02d} {am_pm}, {days[day_index + 1]} (next day)"
        elif number_of_days > 1:
            return f"{new_h}:{new_m:02d} {am_pm}, {days[(day_index + number_of_days) % 7]} ({number_of_days} days later)"

    else:
        if number_of_days == 0:
            return f"{new_h}:{new_m:02d} {am_pm}"
        elif number_of_days == 1:
            return f"{new_h}:{new_m:02d} {am_pm} (next day)"
        elif number_of_days > 1:
            return f"{new_h}:{new_m:02d} {am_pm} ({number_of_days} days later)"
