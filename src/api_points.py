import logging
from gophish import Gophish, models, api
from gophish.models import *
from jinja2 import TemplateNotFound
import json
import requests
import click
import urllib3

urllib3.disable_warnings()

API_KEY = '3e35419d03ca86bd6dfa5e89f0e27a08d2832a7e452686c9068216a112e224a2'
BASE_URL = 'https://127.0.0.1:3333/api/'
API = Gophish(API_KEY, host=f'{BASE_URL}', verify=False)


# TEST API
def test_api():
    """Testing the API end point to ensure all is working fine."""
    result = requests.get(f'{BASE_URL}/templates/?api_key={API_KEY}', verify=False)
    data = json.loads(result.content)
    click.echo('Test Result \n')
    click.echo({"header_type": [result.headers['content-type']]})
    click.echo(f"result: {data}")


# RESET API KEY
def reset_api_key():
    """TODO: To be worked on."""
    result = requests.post(f'{BASE_URL}/reset/?api_key={API_KEY}', verify=False)
    data = json.dumps(result.content)
    click.echo(f'New API Key: {data}')


# CAMPAIGNS
# Retrieve all campaigns
def retrieve_all_campaign():
    """Get a list of all the campaigns"""
    result = requests.get(f'{BASE_URL}/campaigns/?api_key={API_KEY}', verify=False)
    click.echo({"result": [result.content], "Status Code": {result.status_code}})


# Retrieve one campaign
def retrieve_single_campaign(campaign_id):
    """ Get one campaign"""
    result = requests.get(f'{BASE_URL}/campaigns/:{campaign_id}?api_key={API_KEY}', verify=False)
    click.echo({"result": [result.content]})


# Create a new Campaign
def create_email_campign():
    """TODO: To be worked on."""
    groups = [Group(name='Existing Group')]
    page = Page(name='Existing Page')
    template = Template(name='Existing Template')
    smtp = SMTP(name='Existing Profile')
    url = 'http://phishing_server'
    campaign = Campaign(
        name='Example Campaign', groups=groups, page=page,
        template=template, smtp=smtp, url=url)

    post_result = requests.post(f'{BASE_URL}/pages/?api_key={API_KEY}', verify=False, data=campaign)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def get_campaign_summary(campaign_id):
    """Get campaign summary."""
    result = requests.get(f'{BASE_URL}/campaigns/:{campaign_id}/summary?api_key={API_KEY}', verify=False)
    click.echo(f'API Summary result!')
    click.echo({"summary": result.content, "status code": result.status_code})


def delete_campaign(campaign_id: int):
    """Delete a campaign"""
    result = requests.delete(f'{BASE_URL}/campaigns/:{campaign_id}?api_key={API_KEY}', verify=False)
    click.echo({"Delete msg": result.content, "status code": result.status_code})


def mark_campaign_complete(campaign_id: int):
    # TODO: Check this one out
    result = requests.post(f'{BASE_URL}/campaigns/:{campaign_id}/complete?api_key={API_KEY}', verify=False)
    click.echo({"Complete campaign": result.content, "status code": result.status_code})


# GROUPS
def get_groups():
    """Get groups"""
    result = requests.get(f'{BASE_URL}/groups?api_key={API_KEY}', verify=False)
    click.echo({"Groups": result.content, "status code": result.status_code})


def get_group_by_id(group_id:int):
    """Get a group by Id"""
    result = requests.get(f'{BASE_URL}/groups/:{group_id}?api_key={API_KEY}', verify=False)
    click.echo({"Groups": result.content, "status code": result.status_code})


def create_group():
    """Create a group"""
    name = input(f'Name of Group:')
    modified_date = input(f'Enter Date:')  # use date.now()
    email = input(f'Email of Target:')
    first_name = input(f'First Name:')
    last_name = input(f'Last Name:')
    position = input(f'Position:')

    data = {
        "name": name,
        "modified_date": modified_date,
        "target": [{
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "position": position
        }]
    }
    post_result = requests.post(f'{BASE_URL}/groups/?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def update_group():
    """Update a group."""
    # Ask for the group ID
    group_id = input(f'Enter Group ID:')
    name = input(f'Name of Group:')
    modified_date = input(f'Enter Date:')  # use date.now()
    email = input(f'Email of Target:')
    first_name = input(f'First Name:')
    last_name = input(f'Last Name:')
    position = input(f'Position:')

    data = {
        "name": name,
        "modified_date": modified_date,
        "target": [{
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "position": position
        }]
    }
    post_result = requests.post(f'{BASE_URL}/groups/:{group_id}?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def delete_group(group_id:int):
    """Delete a group."""
    result = requests.delete(f'{BASE_URL}/groups/:{group_id}?api_key={API_KEY}', verify=False)
    click.echo({"Groups": result.content, "status code": result.status_code})


# TEMPLATES
def get_all_templates():
    result = requests.get(f'{BASE_URL}/templates/?api_key={API_KEY}', verify=False)
    click.echo({"Landing Pages": result.content, "status code": result.status_code})


def get_template_by_id():
    temp_id = input(f'Enter template ID')
    result = requests.get(f'{BASE_URL}/templates/:{temp_id}?api_key={API_KEY}', verify=False)
    click.echo({"Groups": result.content, "status code": result.status_code})


def create_template():
    # Template attributes:  id, name, subject, text, html, modified_date, attachments
    name = input(f'Name of Group:')
    subject = input(f'Subject:')
    text = input(f'Text:')
    html = input(f'Html:')
    attachments = input(f'upload attachment:')
    modified_date = input(f'Enter Date:')  # use date.now()


    data = {
        "name": name,
        "subject": subject,
        "text": text,
        "html": html,
        "modified_date": modified_date,
        "attachments": attachments
    }
    post_result = requests.post(f'{BASE_URL}/templates/?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})



def update_template():
    temp_id = input(f'Enter tempalate ID')
    name = input(f'Name of Group:')
    subject = input(f'Subject:')
    text = input(f'Text:')
    html = input(f'Html:')
    attachments = input(f'upload attachment:')
    modified_date = input(f'Enter Date:')  # use date.now()


    data = {
        "name": name,
        "subject": subject,
        "text": text,
        "html": html,
        "modified_date": modified_date,
        "attachments": attachments
    }
    post_result = requests.put(f'{BASE_URL}/templates/{temp_id}?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def delete_template():
    temp_id = input(f'Enter template ID')
    result = requests.delete(f'{BASE_URL}/templates/:{temp_id}?api_key={API_KEY}', verify=False)
    click.echo({"Groups": result.content, "status code": result.status_code})


# LANDING PAGES
def get_landing_pages():
    """Get all the landing pages"""
    result = requests.get(f'{BASE_URL}/pages?api_key={API_KEY}', verify=False)
    click.echo({"Landing Pages": result.content, "status code": result.status_code})


def get_landing_page(lp_id: int):
    """Get landing page by ID"""
    result = requests.get(f'{BASE_URL}/pages/{lp_id}?api_key={API_KEY}', verify=False)
    click.echo({"One Landing Page": result.content, "status code": result.status_code})


def create_landing_page():
    name = input(f'Name of Landing Page:')
    html = input(f'HTML of Landing Page:')
    capture_credentials = input(f'Capture Landing page Credentials (Asw: True/False):')
    capture_password = input(f'Capture Password on Landing page (Asw: True/False):')
    redirect_url = input(f'Enter Redirect URL:')
    modified_date = input(f'Enter Date:')  # use date.now()

    data = {
        "name": name,
        "html": html,
        "capture_credentials": capture_credentials,
        "capture_passwords": capture_password,
        "redirect_url": redirect_url,
        "modified_date": modified_date
    }
    post_result = requests.post(f'{BASE_URL}/pages/?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def modify_landing_page():
    name = input(f'Name of Landing Page:')
    html = input(f'HTML of Landing Page:')
    capture_credentials = input(f'Capture Landing page Credentials (Asw: True/False):')
    capture_password = input(f'Capture Password on Landing page (Asw: True/False):')
    redirect_url = input(f'Enter Redirect URL:')
    modified_date = input(f'Enter Date:')  # use date.now()

    data = {
        "name": name,
        "html": html,
        "capture_credentials": capture_credentials,
        "capture_passwords": capture_password,
        "redirect_url": redirect_url,
        "modified_date": modified_date
    }
    post_result = requests.put(f'{BASE_URL}/pages/?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def delete_landing_page():
    lp_id = input(f'Enter template ID')
    result = requests.delete(f'{BASE_URL}/pages/{lp_id}?api_key={API_KEY}', verify=False)
    click.echo({"Delete": result.content, "status code": result.status_code})


# SENDING PROFILE

def get_sending_profile():
    result = requests.get(f'{BASE_URL}/smtp?api_key={API_KEY}', verify=False)
    click.echo({"Profile": result.content, "status code": result.status_code})


def get_profile_by_id():
    prof_id = input(f'Enter profile ID: ')
    result = requests.get(f'{BASE_URL}/smtp/:{prof_id}?api_key={API_KEY}', verify=False)
    click.echo({"Profile": result.content, "status code": result.status_code})


def create_profile():
    name = input(f'Name of profile:')
    username = input(f'Enter Username(Optional):')
    password = input(f'Enter password (Optional):')
    host = input(f'Capture Password on Landing page (Asw: True/False):')
    interface_type = input(f'Enter Redirect URL:')
    from_address= input(f'Enter Redirect URL:')
    ingnore_cert_errors = input(f'Enter Redirect URL:')
    headers= input(f'Enter Redirect URL:')
    modified_date = input(f'Enter Date:')  # use date.now()

    data = {
        "name": name,
        "username": username,
        "password": password,
        "host": host,
        "interface_type": interface_type,
        "from_address": from_address,
        "ingore_cert_errors": ingnore_cert_errors,
        "headers": headers,
        "modified_date": modified_date
    }
    post_result = requests.post(f'{BASE_URL}/smtp/?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def update_profile():
    prof_id = input(f'Enter profile ID')
    name = input(f'Name of profile:')
    username = input(f'Enter Username(Optional):')
    password = input(f'Enter password (Optional):')
    host = input(f'Capture Password on Landing page (Asw: True/False):')
    interface_type = input(f'Enter Redirect URL:')
    from_address= input(f'Enter Redirect URL:')
    ingnore_cert_errors = input(f'Enter Redirect URL:')
    headers= input(f'Enter Redirect URL:')
    modified_date = input(f'Enter Date:')  # use date.now()

    data = {
        "name": name,
        "username": username,
        "password": password,
        "host": host,
        "interface_type": interface_type,
        "from_address": from_address,
        "ingore_cert_errors": ingnore_cert_errors,
        "headers": headers,
        "modified_date": modified_date
    }
    post_result = requests.put(f'{BASE_URL}/smtp/{prof_id}/?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def delete_profile():
    prof_id = input(f'Enter profile ID: ')
    result = requests.delete(f'{BASE_URL}/smtp/:{prof_id}?api_key={API_KEY}', verify=False)
    click.echo({"Delete Profile": result.content, "status code": result.status_code})
