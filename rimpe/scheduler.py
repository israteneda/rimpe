from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

schedule = BlockingScheduler()
settings = get_project_settings()
process = CrawlerProcess(settings)

# @sched.scheduled_job("interval", seconds=3)
# def timed_job():
#     process.crawl(RimpeSpider)
#     process.start()
#     print("This job is run every three seconds.")


@schedule.scheduled_job("cron", day_of_week="mon-sun", hour=00, minute=00)
def scheduled_job():
    print("This job is executed every day at midnight.")


schedule.start()
