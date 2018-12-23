# import time

# print(time.gmtime(0))
#
# print(time.localtime())
#
# print(time.time())

# currentTime = time.localtime()
# print("year : {} , month : {} , day : {} "
#       "".format(currentTime[0], currentTime[1], currentTime[2]))
#
# print("year : {} , month : {} , day : {} "
#       "".format(currentTime.tm_year, currentTime.tm_mon, currentTime.tm_mday))

# ----------------------------------------------------------------------------------

# TIME GAME

# import time
# import random
#
# # from time import time as myTimer
#
# # there is another method to import which is more precise
# # from time import perf_counter as myTimer
#
# the another funtion we can use
# from time import monotonic as myTimer

# another funtion which executes according to the cpu
# from time import process_time as myTimer
#
# input("press enter to start the timer")
#
# wait = random.randint(1, 6)
# time.sleep(wait)
# startTimer = myTimer()
# input("press enter to stop the timer")
# stopTimer = myTimer()
#
# print('started at '+time.strftime("%X", time.localtime(startTimer)))
# print('ended at '+time.strftime("%X", time.localtime(stopTimer)))
#
# print("your reaction time was {} sec/secs".format((stopTimer-startTimer)))

# CHALLENGE

# import time
#
# print("time()   ", time.get_clock_info('time'))
# print("perf_counter()   ", time.get_clock_info('perf_counter'))
# print("perf_counter()   ", time.get_clock_info('monotonic'))
# print("process_time()   ", time.get_clock_info('process_time'))


# ----------------------------------------------------------------------------------

#DATETIME
#
# import time
#
# print("the epoch at this system starts at "
#       "" + time.strftime("%c", time.gmtime(0)))
# print("the current time zone is {} with an offset of {}"
#       "".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print('daylight saving time is in effect from this location')
#     print('the DST time zone is' + time.tzname[1])
#
# print("local time is " + time.strftime("%Y-%m-%d ; %H : %M : %S",
#                                        time.localtime()))
# print("UTC time is " + time.strftime("%Y:%m:%d ; %H : %M : %S",
#                                      time.gmtime()))


# import datetime
#
# print(datetime.datetime.now())
# print(datetime.datetime.today())
# print(datetime.datetime.utcnow())

#---------------------------------------------------------------------------

import pytz
import datetime

# country = 'Asia/Kolkata'
# timeZone = pytz.timezone(country)
# localTime = datetime.datetime.now(tz= timeZone)
#
# print(country)
# print(timeZone)
# print(localTime)
# print('the utc time is ',datetime.datetime.utcnow())

# for zones in pytz.all_timezones:
#     print(zones)
#
for x in pytz.country_names:
    print(x, ' : ', pytz.country_names[x], ' : ', pytz.country_timezones.get(x), end=": ")
    if x in pytz.country_timezones:
        for zone in pytz.country_timezones[x]:
            timeZone = pytz.timezone(zone)
            localTime = datetime.datetime.now(tz= timeZone)
            print('\t\t', zone, localTime)