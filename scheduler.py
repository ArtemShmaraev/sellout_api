from apscheduler.schedulers.background import BackgroundScheduler
from parser.tasks import update_full_info


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_full_info, 'interval', hours=24)
    scheduler.start()
