import csv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO
import smtplib
from application.jobs.workers import celery
from datetime import datetime
from celery.schedules import crontab
from application.send_email import send_email
from application.data.models import *
import logging

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, send_reminders.s(), name='Send an email to influencers every minute')
    sender.add_periodic_task(120.0, send_monthly_report.s(), name='Send monthly report to sponsors each month')


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

@celery.task()
def send_monthly_report():
    subject = 'Monthly report for this month'
    sponsors = query_sponsors()
    for sponsor in sponsors:
        report_html = generate_report_html(sponsor['id'])
        send_email(subject, report_html, sponsor['email'])
    logging.info("Task completed: send_monthly_report")

def query_sponsors():
    sponsors = Sponsor.query.all()
    info = []
    emails = set()      
    for sponsor in sponsors:
        user = User.query.filter(User.username == sponsor.name).first()        
        if user.email not in emails:
            sponsor_info = {'id': sponsor.id, 'email': user.email}
            emails.add(user.email)
            info.append(sponsor_info)    
    return info

def generate_report_html(sponsor_id):
    campaign_details = query_campaign_details(sponsor_id)
    campaign_details_html = ''.join([f"<p>{detail}</p>" for detail in campaign_details])

    report_html = f"""
    <html>
        <body>
            <h1>Monthly Activity Report</h1>
            <h2>Campaign Details</h2>
            {campaign_details_html}
            <h2>Advertisements Done</h2>
            <p>Number of advertisements: {query_advertisements_done(sponsor_id)}</p>
            <h2>Growth in Sales</h2>
            <p>Sales growth: {query_sales_growth()}%</p>
            <h2>Budget</h2>
            <p>Budget used: ${query_budget_used()}</p>
            <p>Budget remaining: ${query_budget_remaining()}</p>
        </body>
    </html>
    """
    return report_html

def query_campaign_details(sponsor_id):
    campaigns = Campaign.query.filter(Campaign.sponsor_id == sponsor_id).all()
    campaign_details = []
    for campaign in campaigns:
        campaign_details.append(f"Campaign name: {campaign.name}, Start date: {campaign.start_date}, End date: {campaign.end_date}")
    return campaign_details

def query_advertisements_done(sponsor_id):
    return 5

def query_sales_growth():
    return 15.5

def query_budget_used():
    return 100000

def query_budget_remaining():
    return 200000

@celery.task()
def export_campaigns_csv(sponsor_id):
    campaigns = get_campaigns_by_sponsor(sponsor_id)
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Name', 'Start Date', 'End Date', 'Budget', 'Visibility'])
    
    for campaign in campaigns:
        writer.writerow([
            campaign.name,
            campaign.start_date,
            campaign.end_date,
            campaign.budget,
            'Public' if campaign.is_public else 'Private'
        ])
    
    csv_content = output.getvalue()
    output.close()
    
    file_path = f'D:\\Srujan\\Code\\GitHub\\Influencer-Engagement-Sponsorship-Hub\\application\\jobs\\campaign_details_{sponsor_id}.csv'
    with open(file_path, 'w') as f:
        f.write(csv_content)

    send_email_alert(sponsor_id)
    
def get_campaigns_by_sponsor(sponsor_id):
    return Campaign.query.filter(Campaign.sponsor_id == sponsor_id).all()


def send_email_alert(sponsor_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "srujan.pat2004@gmail.com"
    smtp_password = "bnpl kxgb slnc qhyk"

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = sponsor_email
    msg['Subject'] = "Your Campaigns CSV Export is Ready"
    
    body = "Your campaigns CSV export is ready. Please find the attached file."
    msg.attach(MIMEText(body, 'plain'))
    
    filename = "D:\\Srujan\\Code\GitHub\\Influencer-Engagement-Sponsorship-Hub\\application\\jobs\\campaign_details_15.csv"

    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            
            part.add_header('Content-Disposition', f"attachment; filename={filename}")
            msg.attach(part)
    except Exception as e:
        logging.error(f"Failed to attach the file: {e}")
        return

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, sponsor_email, str(msg))
        logging.info(f"Email sent successfully to {sponsor_email}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
    finally:
        server.quit()
