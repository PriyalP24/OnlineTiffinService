import datetime
import pytz

d = datetime.date(2019, 12, 23)
print(d)

tdy = datetime.date.today()
print(tdy)
print(tdy.year)#only grab the year
print(tdy.day)#only grab the day

#monday- 0 sunday-6
print(tdy.weekday()) #today is monday my o/p = 0
print(tdy.isoweekday())#o/p = 1

#Timedelta

tdeltime= datetime.timedelta(days=7)
print(tdy+tdeltime)#displays date after 7 days will be


#date2 = date1 + timedelta

#timedelta = date1 + date2

bday = datetime.date(2020, 9, 20)

till_bdy = bday-tdy
print(till_bdy)#prints how many days are remains of my bdy from tdy
print(till_bdy.days)
print(till_bdy.total_seconds())






#datetime.time()

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

#datetime

t1 = datetime.datetime(2019, 12, 23, 9, 30, 45, 100000)
print(t1)
print(t1.date())
print(t1.time())


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

#pytz
dt1 = datetime.datetime(2019, 12, 23, 9, 30, 45, tzinfo=pytz.UTC)
print(dt1)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print("dt_now : ",dt_now)

#dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
#print(dt_utcnow)

dt_mtn1 = dt_now.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_mtn1)
dt_mtn2 = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn2)


#list of all timezones
for tz in pytz.all_timezones:
    print(tz)

dt_naive = datetime.datetime.now(tz=pytz.timezone('CST6CDT'))
print(dt_naive.strftime('%B %d, %Y'))#convert datetime into string

#convert string time into datetime

dt_str = 'December 22, 2019'
dt = datetime.datetime.strptime(dt_str,'%Y-%B-%dT%H:%M')
print(dt)