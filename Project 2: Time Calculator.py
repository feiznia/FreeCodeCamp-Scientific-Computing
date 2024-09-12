def add_time(start, duration, day=None):
    am_pm = start[-2:]
    star = start[:len(start)-3]
    start_hr =  int(star[:len(star)-3])
    start_min = int(star[len(star)-2:len(star)])
    duration_hr = int(duration[:(len(duration)-3)])
    duration_min = int(duration[-2:])
    # new_time = new_hr+":"+new_min
    if am_pm == 'PM':
        start_hr = start_hr+12
    new_hr = start_hr+duration_hr
    new_min = start_min+duration_min
    if new_min > 60:
        new_min_hr = new_min//60
        new_hr = new_hr + new_min_hr
        new_min = new_min%60
    days = new_hr//24
    if days == 0:
        ndays = ''
    elif days == 1:
        ndays = '(next day)'
    else:
        ndays = f'({days} days later)'
    while new_hr > 24:
        new_hr = new_hr - 24
    if new_hr == 24:
        tod = 'AM'
        new_hr = 12
    elif new_hr == 12:
        tod = 'PM'
        new_hr = 12
    elif new_hr <= 12:
        tod = 'AM'
    elif new_hr > 12 and new_hr < 24:
        tod = 'PM'
        new_hr = new_hr - 12

    new_hr = str(new_hr)
    tod = str(tod)
    ndays = str(ndays)
    if new_min < 10:
        new_min = '0'+str(new_min)
    else:
        new_min = str(new_min)
    
    if ndays:
        new_time = new_hr+":"+new_min+" "+tod+" "+ndays
    else:
        new_time = new_hr+":"+new_min+" "+tod
    # print(new_time)
    return new_time
