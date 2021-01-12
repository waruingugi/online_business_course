import requests
import os
from celery import shared_task
from registration.sub_logger import logger


@shared_task
def add_to_email_list(name, email):
    """Send new subscriber details to sendpulse automation."""
    sendpulse_post_url = os.environ['SENDPULSE_POST_URL']

    post_data = {
        'Name': name, 'Email': email, 'Phone': ''
    }
    logger.info(f'tasks.add_to_email_list: Received data {post_data}')

    requests.post(sendpulse_post_url, data=post_data)
