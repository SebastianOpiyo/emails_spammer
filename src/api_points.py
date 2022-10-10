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
        click.secho('CAMPAIGNS', bold=True, fg='green', underline=True)
        click.secho('ID: {}, Name: {}'.format(campaign.id, campaign.name), fg='blue')


# Retrieve one campaign
def retrieve_single_campaign(campaign_id: int):
    """ Get one campaign"""
    try:
        data = API.campaigns.get(campaign_id=campaign_id)
        if data:
            click.secho('No Campaign with that ID Yet', blink=True, bold=True, fg='red')
        for campaign in data:
            click.secho('CAMPAIGN', bold=True, fg='green', underline=True)
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
            click.secho('Campaign Summary', bold=True, fg='green', underline=True)
            click.secho('Summary: {}'.format(summary), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_campaigns_summaries():
    """Get campaigns summaries."""
    try:
        summaries = API.campaigns.summary()
        if summaries:
            click.secho('Campaign Summaries', bold=True, fg='green', underline=True)
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
            click.secho('Groups', bold=True, fg='green', underline=True)
            for group in groups:
                click.secho('Group Name: {} \nUser Targets: {}'.format(group.name, len(group.targets)), fg='blue')
                click.secho('{}'.format('*' * 20))
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_group_by_id(group_id: int):
    """Get a group by Id"""
    try:
        group = API.groups.get(group_id=group_id)
        if group:
            click.secho('Group', bold=True, fg='green')
            click.secho('Group Name: {} \nUser Targets: {}'.format(group.name, len(group.targets)), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def add_target(targets: list, email: str, first_name: str, last_name: str, position: str):
    result = User(first_name=first_name, last_name=last_name, email=email, position=position)
    targets.append(result)
    click.secho('Target Added', fg='yellow')
    click.secho(f"Do you want to add more target? [y/n]", nl=False, bold=True, fg='bright_blue')
    char = click.getchar()
    click.echo()
    if char == 'y':
        click.secho(f"\nAdd Target:", fg='green')
        add_target(targets, email, first_name, last_name, position)
        click.secho(f"Target Update: {targets}")
    elif char == 'n':
        click.secho(f"Target Before Abort: {targets}\n")
        click.secho(f"Abort!:", fg='red')
    else:
        click.secho(f"Invalid input :(", fg='red')


def create_group(name: str, target: list):
    """Create a group"""
    group = Group(name=name, targets=target)

    try:
        API.groups.post(group)
        if True:
            click.secho('Group Created Successfully!', fg='green')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def update_group(group_id, name, target):
    """Update a group."""
    try:
        group = API.groups.get(group_id=group_id)
        edit_group = Group(name=name, target=target)
        if group:
            API.groups.put(edit_group)
            click.secho('Group Updated Successfully!', fg='green')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def delete_group(group_id: int):
    """Delete a group."""
    try:
        API.groups.delete(group_id=group_id)
        click.secho('Group With ID {} Deleted Successfully'.format(group_id), bold=True, fg='green')
    except Exception as e:
        click.secho('Group not deleted', bold=True, fg='yellow')
        click.secho('Error: {}'.format(e), bold=True, fg='red')


# TEMPLATES
def get_all_templates():
    try:
        templates = API.templates.get()
        if templates:
            click.secho('Groups', bold=True, fg='green', underline=True)
            for template in templates:
                click.secho('Template Name: {} \nTemplate ID: {}'.format(template.name, len(template.id)), fg='blue')
                click.secho('{}'.format('*' * 20))
    except Exception as e:
        click.secho('Error: {}'.format(e))



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


def delete_template(template_id: int):
    try:
        API.templates.delete(template_id=template_id)
        click.secho('Template With ID {} Deleted Successfully'.format(template_id), bold=True, fg='green')
    except Exception as e:
        click.secho('Template not deleted', bold=True, fg='yellow')
        click.secho('Error: {}'.format(e), bold=True, fg='red')


# LANDING PAGES
def get_landing_pages():
    """Get all the landing pages"""
    try:
        pages = API.pages.get()
        if pages:
            click.secho('Pages', bold=True, fg='green', underline=True)
            for page in pages:
                click.secho('Page Name: {} \nPage ID: {}'.format(template.name, len(template.id)), fg='blue')
                click.secho('{}'.format('*' * 20))
    except Exception as e:
        click.secho('Error: {}'.format(e))

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


def delete_landing_page(page_id: int):
    try:
        API.pages.delete(page_id=page_id)
        click.secho('Page With ID {} Deleted Successfully'.format(page_id), bold=True, fg='green')
    except Exception as e:
        click.secho('Page not deleted', bold=True, fg='yellow')
        click.secho('Error: {}'.format(e), bold=True, fg='red')

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


def delete_profile(smtp_id: int):
    try:
        API.smtp.delete(smtp_id=smtp_id)
        click.secho('Profile With ID {} Deleted Successfully'.format(smtp_id), bold=True, fg='green')
    except Exception as e:
        click.secho('Profile not deleted', bold=True, fg='yellow')
        click.secho('Error: {}'.format(e), bold=True, fg='red')