def secondsIntoMinutes(seconds):
    minutes = seconds / 60
    print("There are", minutes, "minutes in",seconds,"seconds")
def secondsIntoHours(seconds):
    hours = seconds / 3600
    print("There are", hours, "hours in", seconds, "seconds")
def secondsIntoDays(seconds):
    days = seconds / 86400
    print("There are", days, "days in", seconds, "seconds")
def secondsIntoMilliseconds(seconds):
    milliseconds = seconds * 1000
    print("There are", milliseconds, "milliseconds in", seconds, "seconds")
secondsIntoMilliseconds(1)
secondsIntoDays(86400)
secondsIntoHours(900)
secondsIntoMinutes(298)
