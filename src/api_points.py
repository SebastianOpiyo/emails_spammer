import json
import requests
import click
import urllib3
from datetime import datetime
from gophish import Gophish, models, api
from gophish.models import *

urllib3.disable_warnings()

API_KEY = '3e35419d03ca86bd6dfa5e89f0e27a08d2832a7e452686c9068216a112e224a2'
BASE_URL = 'https://127.0.0.1:3333/api/'
API = Gophish(API_KEY, verify=False)


# TEST API
def test_api():
    """Testing the API end point to ensure all is working fine."""
    result = requests.get(f'{BASE_URL}/templates/?api_key={API_KEY}', verify=False)
    data = json.loads(result.content)
    click.echo('Test Result \n')
    click.echo({"header_type": [result.headers['content-type']]})
    click.echo(f"Test Response: {data}, \nStatus Code: {result.status_code}")


# RESET API KEY
def reset_api_key():
    """TODO: To be worked on."""
    result = requests.post(f'{BASE_URL}/reset/?api_key={API_KEY}', verify=False)
    data = json.dumps({'result': result.content.decode('utf-8')})
    click.echo(f"NEW API KEY: {data}, \nStatus Code: {result.status_code}")


# CAMPAIGNS
# Retrieve all campaigns
def retrieve_all_campaign():
    """Get a list of all the campaigns"""
    data = API.campaigns.get()
    if not data:
        click.secho('No Campaigns Created Yet', blink=True, bold=True, fg='red')
    for campaign in data:
        click.secho('CAMPAIGNS', bold=True, fg='green')
        click.secho('ID: {}, Name: {}'.format(campaign.id, campaign.name), fg='blue')


# Retrieve one campaign
def retrieve_single_campaign(campaign_id: int):
    """ Get one campaign"""
    try:
        data = API.campaigns.get(campaign_id=campaign_id)
        if data:
            click.secho('No Campaign with that ID Yet', blink=True, bold=True, fg='red')
        for campaign in data:
            click.secho('CAMPAIGN', bold=True, fg='green')
            click.secho('ID: {}, Name: {}'.format(campaign.id, campaign.name), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e), blink=True, bold=True, fg='red')


# Create a new Campaign
def create_email_campaign(camp_name: int, group_name: str, page_name: str, template_name: str,
                          smtp_name: str, url: str):
    groups = [Group(name=group_name)]
    page = Page(name=page_name)
    template = Template(name=template_name)
    smtp = SMTP(name=smtp_name)
    campaign = Campaign(
        name=camp_name, groups=groups, page=page,
        template=template, smtp=smtp, url=url)

    try:
        campaign = API.campaigns.post(campaign)
        if campaign:
            click.secho('Campaign ID: {}, Name: {} created successfully'.format(campaign.id, campaign.name), fg='green')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def get_campaign_summary(campaign_id):
    """Get campaign summary."""
    try:
        summary = API.campaigns.summary(campaign_id=campaign_id)
        if summary:
            click.secho('Campaign Summary', bold=True, fg='green')
            click.secho('Summary: {}'.format(summary), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_campaigns_summaries():
    """Get campaigns summaries."""
    try:
        summaries = API.campaigns.summary()
        if summaries:
            click.secho('Campaign Summaries', bold=True, fg='green')
            for summary in summaries:
                click.secho('Summary: {}'.format(summary), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def delete_campaign(campaign_id: int):
    """Delete a campaign"""
    try:
        API.campaigns.delete(campaign_id=campaign_id)
        click.secho('Campaign With ID {} Deleted Successfully'.format(campaign_id), bold=True, fg='red')
    except Exception as e:
        click.secho('Campaign not deleted', bold=True, fg='yellow')
        click.secho('Error: {}'.format(e), bold=True, fg='red')


def mark_campaign_complete(campaign_id: int):
    """Mark campaign as Complete."""
    try:
        API.campaigns.complete(campaign_id=campaign_id)
        click.secho('Campaign With ID {} Completed Successfully'.format(campaign_id), bold=True, fg='red')
    except Exception as e:
        click.secho('Campaign not marked as complete', bold=True, fg='yellow')
        click.secho('Error: {}'.format(e), bold=True, fg='red')


# GROUPS
def get_groups():
    """Get groups"""
    try:
        groups = API.groups.get()
        if groups:
            click.secho('Groups', bold=True, fg='green')
            for group in groups:
                click.secho('Group Name: {} \nUser Targets: {}'.format(group.name, len(group.targets)), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_group_by_id(group_id: int):
    """Get a group by Id"""
    result = requests.get(f'{BASE_URL}/groups/:{group_id}?api_key={API_KEY}', verify=False)
    data = json.dumps({'data': result.content.decode('utf-8')})
    click.echo(f"Group Data: {data}, \nStatus Code: {result.status_code}")


@click.option('--email', prompt="Enter Target Email:", help="Email for the target")
@click.option('--first_name', prompt="Enter Target First Name:", help="Target first name")
@click.option('--last_name', prompt="Enter Target Last Name:", help="Target last name")
@click.option('--position', prompt="Enter Target position:", help="Target position")
def add_target(targets: list, email: str, first_name: str, last_name: str, position: str):
    result = User(first_name=first_name, last_name=last_name, email=email, position=position)
    targets.append(result)
    click.secho('Target Added', fg='yellow')


def create_group(email, first_name, last_name, position, name):
    """Create a group"""
    # TODO: Cater for extra information for extra targets.

    data = {
        "name": name,
        "modified_date": datetime.now(),
        "target": [{
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "position": position
        }]
    }
    post_data = json.dumps(data, indent=4, sort_keys=True, default=str)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    post_result = requests.post(url=f'{BASE_URL}/groups/?api_key={API_KEY}', json=post_data, verify=False,
                                headers=headers)
    res_data = json.dumps({'data': post_result.content.decode('utf-8')})
    click.echo({"Response": res_data, "Status Code": post_result.status_code})


def update_group(group_id, name, email, first_name, last_name, position):
    """Update a group."""
    # Ask for the group ID

    data = {
        "name": name,
        "modified_date": json.dumps(datetime.now(), indent=4, sort_keys=True, default=str),
        "target": [{
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "position": position
        }]
    }
    post_result = requests.post(f'{BASE_URL}/groups/:{group_id}?api_key={API_KEY}', verify=False, data=data)
    click.echo({"Response": post_result.content, "Status Code": post_result.status_code})


def delete_group(group_id: int):
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
    from_address = input(f'Enter Redirect URL:')
    ingnore_cert_errors = input(f'Enter Redirect URL:')
    headers = input(f'Enter Redirect URL:')
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
    from_address = input(f'Enter Redirect URL:')
    ingnore_cert_errors = input(f'Enter Redirect URL:')
    headers = input(f'Enter Redirect URL:')
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
