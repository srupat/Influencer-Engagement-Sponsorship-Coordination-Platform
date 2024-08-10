from application.jobs.workers import celery
from datetime import datetime
from celery.schedules import crontab
from application.send_email import send_email
from application.data.models import *
import logging

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, send_reminders.s(), name='Send an email to influencers every minute')

@celery.task()
def send_reminders():
    subject = 'Reminder: You have pending ad requests'
    body = 'Please check your account for pending ad requests.'
    emails = query_influencers_with_pending_requests()
    for email in emails:
        send_email(subject, body, email)
    logging.info("Task completed: send_reminders")
        
def query_influencers_with_pending_requests():
    ad_requests = AdRequest.query.filter(AdRequest.is_pending == 1)
    influencers_ids = set()
    for request in ad_requests:
        influencers_ids.add(request.influencer_id)
    print(influencers_ids)
    influencer_emails = []
    for id in influencers_ids:
        print(id)
        influencer = Influencer.query.get(id)
        user = User.query.filter(User.username == influencer.name).first()
        influencer_emails.append(user.email)
    print(influencer_emails)
    return influencer_emails


