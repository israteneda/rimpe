from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=10)
def timed_job():
    print('This job is run every ten seconds.')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=00, minute=30)
def scheduled_job():
    print('This job is run every day at 00 and 30 am.')

sched.start()
