import time
import datetime
import speedtest

# Vars for timer & speeds
t0 = time.time()
threads = None
try:
    s = speedtest.Speedtest()
except ConfigRetrievalError:
    f = open("speedLogs.txt", "a")
    f = open("speedLogs.txt", "a")
    f.write("\n\n_____________________________________________________________\n")
    f.write("---------   {0}   ---------".format(finalDateTime))
    f.write("\nYour Ping is: 0 ms\nYour download speed is: 0 Mbps\nYour upload speed is: 0 Mbps\nTime taken: 0 seconds".format())
    f.write("\n-------------------------------------------")
    f.write("\n___________________________________________________________")
    f.close()
    
mbpsDown = int(s.download(threads=threads) * (10**-6))
mbpsUp = int(s.upload(threads=threads) * (10**-6))
ping = int(s.results.ping)
t1 = time.time()
timeTaken = int(t1-t0)

# Creates list for day and time. 0-4 = year, 6-7 = month, 9-10 = day, 12-13 = hour, 15-16 = minutes, 18-19 = seconds, 21-26 = ms
dateTimeStr = str(datetime.datetime.now())
hoursMinutes = dateTimeStr[11:16]
date = dateTimeStr[0:10]

# Manual convert to 12 hour clock because who needs google 
# if int(hoursMinutes[:2]) > 12:
#     hoursMinutes = str(int(hoursMinutes[:2]) - 12) + hoursMinutes[2:] + "pm"
# else:
#     hoursMinutes = str(int(hoursMinutes[:2]) - 12) + hoursMinutes[2:] + "am"

finalDateTime = "{0}/{1}/{2} | {3}".format(date[5:7], date[8:10], date[0:4], hoursMinutes)


f = open("speedLogs.txt", "a")
f.write("\n\n_____________________________________________________________\n")
f.write("---------   {0}   ---------".format(finalDateTime))
f.write("\nYour Ping is: {0} ms\nYour download speed is: {1} Mbps\nYour upload speed is: {2} Mbps\nTime taken: {3} seconds".format(int(s.results.ping), mbpsDown, mbpsUp, timeTaken))
f.write("\n-------------------------------------------")
f.write("\n___________________________________________________________")
f.close()

print("---------   {0}   ---------".format(finalDateTime))
print("Your Ping is: {0} ms\nYour download speed is: {1} Mbps\nYour upload speed is: {2} Mbps\nTime taken: {3} seconds".format(int(s.results.ping), mbpsDown, mbpsUp, timeTaken))
print("-------------------------------------------")
print("___________________________________________________________\n\n")

f2 = open("pings.txt", "a")
f2.write("\n")
f2.write(str(int(s.results.ping)))
f2.close()