import json
import requests
import click
import urllib3
from datetime import datetime
from gophish import Gophish
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

# USER MANAGEMENT
# Signup and User Management
def get_users():
    result = requests.get(f'{BASE_URL}/users/?api_key={API_KEY}', verify=False)
    data = json.loads(result.content)
    click.echo('Users Data \n')
    click.echo({"header_type": [result.headers['content-type']]})
    click.echo(f"Users: {data}, \nStatus Code: {result.status_code}")


def get_user(user_id:int):
    """Get user details given user ID"""
    result = requests.get(f'{BASE_URL}/users/{user_id}/?api_key={API_KEY}', verify=False)
    data = json.loads(result.content)
    click.echo('User Data \n')
    click.echo({"header_type": [result.headers['content-type']]})
    click.echo(f"User Data: {data}, \nStatus Code: {result.status_code}")


def create_user(username:str, password:str, role:str):
    user_data = {
        "username":username,
        "password":password,
        "role": role
    }

    try:
        post_user = requests.post(url=f'{BASE_URL}/users/?api_key={API_KEY}', data=user_data,verify=False)
        if post_user:
            click.secho(f'User created successfully,\n Status code:{post_user.status_code}', fg='green')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def modify_user():
    pass


def delete_user():
    pass

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
            collection = summary.stats.as_dict()
            click.echo(collection)
            click.secho('Campaign Summary', bold=True, fg='green', underline=True)
            click.secho('Summary: {}'.format(collection["name"]), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_campaigns_summaries():
    """Get campaigns summaries."""
    try:
        summaries = API.campaigns.summary()
        if summaries:
            collection = summaries.as_dict()
            click.echo(collection)
            click.secho('Campaign Summaries', bold=True, fg='green', underline=True)
            for k, v in collection:
                click.secho('Summary: {} {}'.format(k, v), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_campaign_stats():
    """Get campaign stats."""
    try:
        summary = API.campaigns.summary()
        if summary:
            stats = summary.as_dict()["stats"]
            return stats
    except Exception as e:
        return 'Error: {}'.format(e)


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
                click.secho('Template Name: {} \nTemplate ID: {}'.format(template.name, template.id), fg='blue')
                click.secho('{}'.format('*' * 20))
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_template_by_id(template_id: int):
    try:
        template = API.templates.get(template_id=template_id)
        if template:
            click.secho('Group', bold=True, fg='green')
            click.secho('Group Name: {}\n'.format(template.name), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def create_template(name: str, html: str, text: str, time: datetime):
    template = Template(
        name=name,
        html=html,
        text=text,
        time=time
    )
    try:
        template = API.templates.post(template)
        if True:
            click.secho('Template Name: {} Created Successfully!'.format(template.name), fg='green')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def update_template(template_id, name: str, html: str, text: str, time: datetime):

    try:
        # Check existence
        API.templates.get(template_id=template_id)
        if True:
            template = Template(
                name=name,
                html=html,
                text=text,
                time=time
            )
            try:
                template = API.templates.put(template)
                if True:
                    click.secho('Template Name: {} Created Successfully!'.format(template.name), fg='green')
            except Exception as e:
                click.secho("Error: {}".format(e), blink=True, fg='red')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


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
                click.secho('Landing Page Name: {} \nPage ID: {}'.format(page.name, page.id), fg='blue')
                click.secho('{}'.format('*' * 20))
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_landing_page(lp_id: int):
    """Get landing page by ID"""
    try:
        page = API.pages.get(page_id=lp_id)
        if page:
            click.secho('landing Page', bold=True, fg='green')
            click.secho('Group Name: {}\n'.format(page.name), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def create_landing_page(name: str, html: str, redirect_url: str, capture_credentials: bool, capture_passwords: bool):

    page = Page(
        name=name,
        html=html,
        capture_credentials=capture_credentials,
        capture_passwords=capture_passwords,
        redirect_url=redirect_url,
    )
    try:
        page = API.pages.post(page)
        if True:
            click.secho('Template Name: {} Created Successfully!'.format(page.name), fg='green')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def modify_landing_page(page_id, name, html, redirect_url, capture_credentials, capture_passwords):
    try:
        # Check existence
        API.pages.get(page_id=page_id)
        if True:
            page = Page(
                name=name,
                html=html,
                capture_credentials=capture_credentials,
                capture_passwords=capture_passwords,
                redirect_url=redirect_url,
            )
            try:
                update_page = API.pages.put(page)
                if True:
                    click.secho('Template Name: {} Created Successfully!'.format(update_page.name), fg='green')
            except Exception as e:
                click.secho("Error: {}".format(e), blink=True, fg='red')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def delete_landing_page(page_id: int):
    try:
        API.pages.delete(page_id=page_id)
        click.secho('Page With ID {} Deleted Successfully'.format(page_id), bold=True, fg='green')
    except Exception as e:
        click.secho('Page not deleted', bold=True, fg='yellow')
        click.secho('Error: {}'.format(e), bold=True, fg='red')


# SENDING PROFILE

def get_sending_profile():
    try:
        profiles = API.smtp.get()
        if profiles:
            click.secho('Profiles', bold=True, fg='green', underline=True)
            for smtp in profiles:
                click.secho('Profile Name: {} \nProfile ID: {}'.format(smtp.name, smtp.id), fg='blue')
                click.secho('{}'.format('*' * 20))
    except Exception as e:
        click.secho('Error: {}'.format(e))


def get_profile_by_id(smtp_id: int):
    try:
        profile = API.smtp.get(smtp_id=smtp_id)
        if profile:
            click.secho('Profile', bold=True, fg='green')
            click.secho('Profile Name: {}\n'.format(profile.name), fg='blue')
    except Exception as e:
        click.secho('Error: {}'.format(e))


def create_profile(name: str, interface: str, host: str, from_address: str, ignore_cert_errors: bool):
    cert = False
    if ignore_cert_errors == "True":
        cert = True
    # from_address = "John Doe <ifo@shobarafoods.biz>"
    profile = SMTP(name=name)
    profile.interface_type = interface
    profile.host = host
    profile.from_address = from_address
    profile.ignore_cert_errors = cert
    prof = API.smtp.post(profile)

    try:
        if prof:
            click.secho('Profile Created Successfully!', fg='green')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def update_profile(profile_id, name, from_address, interface_type, host, ignore_cert_errors):
    try:
        # Check existence
        API.smtp.get(smtp_id=profile_id)
        if True:
            prof = SMTP(
                name=name,
                from_address=from_address,
                interface_type=interface_type,
                host=host,
                ignore_cert_errors=ignore_cert_errors,
            )
            try:
                update_profile = API.smtp.put(prof)
                if True:
                    click.secho('Profile Name: {} Updated Successfully!'.format(update_profile.name), fg='green')
            except Exception as e:
                click.secho("Error: {}".format(e), blink=True, fg='red')
    except Exception as e:
        click.secho("Error: {}".format(e), blink=True, fg='red')


def delete_profile(smtp_id: int):
    try:
        API.smtp.delete(smtp_id=smtp_id)
        click.secho('Profile With ID {} Deleted Successfully'.format(smtp_id), bold=True, fg='green')
    except Exception as e:
        click.secho('Profile not deleted', bold=True, fg='yellow')
        click.secho('Error: {}'.format(e), bold=True, fg='red')