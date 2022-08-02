def add_time(start, duration, day=False):
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    total_minutes = ((int(start.split(' ')[0].split(':')[0]) * 60)
                     + int(start.split(' ')[0].split(':')[-1]) 
                     + (int(duration.split(':')[0]) * 60)
                     + int(duration.split(':')[-1]))

    midday = start[-2:]
    
    
    # sets minutes to track 24hr timespan
    if midday == "PM":
        total_minutes = total_minutes + 720

    # sets AM/PM
    check = total_minutes // 720
    if check % 2 == 0: 
        midday = 'AM'
    else:
        midday = 'PM'

    # sets the hours and minutes for formatting
    minutes = str(int(total_minutes % 60)).rjust(2,'0')
    hours = total_minutes // 60
    num_days_forward = total_minutes // 1440
    day_adjust = total_minutes % 720
    hours = day_adjust // 60
    
    # checks for the correct 12 AM/PM
    if hours == 0:
        hours = 12

    # sets the new day
    if day != False:
        day = day.lower()
        if total_minutes > 1440:
            new_day = week[(week.index(day) + num_days_forward) % 7]
            new_day = f", {new_day[0].upper() + new_day[1:]}"
        else:
            new_day = f", {day[0].upper() + day[1:]}"

    # format statement
    # include new_day only when day isnt False
    # include forward_message only when isnt False

    final_time = f"{hours}:{minutes} {midday}"

    # set days forward message
    if num_days_forward == 0:
        forward_msg = False
    elif num_days_forward == 1:
        forward_msg = '(next day)'
    else:
        forward_msg = f'({num_days_forward} days later)'

    # include sameday with forward message
    if day != False:
        final_message = f"{final_time}{new_day} {forward_msg}"
    else:
        final_message = f"{final_time} {forward_msg}"

    # sameday check
    if num_days_forward == 0:
        if day != False:
            final_message = f"{final_time}{new_day}"
        else:
            final_message = f"{final_time}"

    return final_message