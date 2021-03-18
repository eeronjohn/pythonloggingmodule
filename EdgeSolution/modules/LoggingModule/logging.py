import sched, time
from datetime import datetime


s = sched.scheduler(time.time, time.sleep)
def do_task(sc): 
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Logging something...')
    print('Current time is', current_time)
    # do your stuff
    s.enter(5, 1, do_task, (sc,))

s.enter(5, 1, do_task, (s,))
s.run()