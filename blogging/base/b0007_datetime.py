import datetime

now = datetime.datetime.now()

print("Current Time :", now.strftime("%Y-%m-%d %H:%M:%S"))

days = dict({1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday',
             6: 'saturday', 7: 'sunday'})
print("Todays :", days[now.isoweekday()])

#timedelta : weeks, days, hours, minutes, seconds
tomorrow = now + datetime.timedelta(days=1)

if now < tomorrow:
    print("Tomorrow :", tomorrow.strftime("%Y-%m-%d %H:%M:%S"))

dt_string = tomorrow.strftime("%Y-%m-%d %H:%M:%S")
dt_format = "%Y-%m-%d %H:%M:%S"
dt = datetime.datetime.strptime(dt_string, dt_format)
print('type :', type(dt))
print('Timestamp :', dt.timestamp())
print('Timezone :', dt.astimezone(tz=None))