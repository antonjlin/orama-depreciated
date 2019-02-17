from datetime import datetime
import threading
from sys import stdout
printLock = threading.Lock()

def log(text,prefix=None,timestamp=True,file=False,silent=False):
    if prefix != None:
        task = "[" + str(prefix) + "] "
    else:
        task = ""
    if timestamp:
        timestamp = "[" + str(datetime.now().strftime("%H:%M:%S.%f")[:-4]) + "] "
    else:
        timestamp = ""
    total = "{}{}{}".format(task,timestamp,text)

    if file:
        with open('log.txt','a') as logFile:
            logFile.write(total + "\n")

    if not silent:
        with printLock:
            stdout.write(total + "\n")
            stdout.flush()
    return total
