from gophish import Gophish, models, api
from gophish.models import *
from jinja2 import TemplateNotFound
import json
import requests

API_KEY = '3e35419d03ca86bd6dfa5e89f0e27a08d2832a7e452686c9068216a112e224a2'
BASE_URL = 'https://127.0.0.1:3333/api/'
API = Gophish(API_KEY, host=f'{BASE_URL}', verify=False)


# TEST API
def test_api():
    """Testing the API end point to ensure all is working fine."""
    result = requests.get(f'{BASE_URL}/templates/?api_key={API_KEY}', verify=False)
    print('Test Result \n')
    print({"result": [result.content]})


# RESET API KEY
def reset_api_key():
    """TODO: To be worked on."""
    print(f'Reset the API Key')


# CAMPAIGNS
# Retrieve all campaigns
def retrieve_all_campaign():
    """Get a list of all the campaigns"""
    result = requests.get(f'{BASE_URL}/campaigns/?api_key={API_KEY}', verify=False)
    print({"result": [result.content], "Status Code": {result.status_code}})


# Retrieve one campaign
def retrieve_single_campaign(campaign_id):
    """ Get one campaign"""
    result = requests.get(f'{BASE_URL}/campaigns/:{campaign_id}?api_key={API_KEY}', verify=False)
    print({"result": [result.content]})


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
        template=template, smtp=smtp)

    campaign = API.campaigns.post(campaign)
    print(f'Campaign with ID: {campaign.id}, created successfuly.')


def get_campaign_summary(campaign_id):
    """Get campaign summary."""
    result = requests.get(f'{BASE_URL}/campaigns/:{campaign_id}/summary?api_key={API_KEY}', verify=False)
    print(f'API Summary result!')
    print({"summary": result.content, "status code": result.status_code})


def delete_campaign(campaign_id: int):
    """Delete a campaign"""
    result = requests.delete(f'{BASE_URL}/campaigns/:{campaign_id}?api_key={API_KEY}', verify=False)
    print({"Delete msg": result.content, "status code": result.status_code})


def mark_campaign_complete(campaign_id: int):
    result = requests.delete(f'{BASE_URL}/campaigns/:{campaign_id}/complete?api_key={API_KEY}', verify=False)
    print({"Complete campaign": result.content, "status code": result.status_code})


# GROUPS
def get_groups():
    """Get groups"""
    result = requests.get(f'{BASE_URL}/groups?api_key={API_KEY}', verify=False)
    print({"Groups": result.content, "status code": result.status_code})


def get_group_by_id(group_id:int):
    """Get a group by Id"""
    result = requests.get(f'{BASE_URL}/groups/:{group_id}?api_key={API_KEY}', verify=False)
    print({"Groups": result.content, "status code": result.status_code})


def create_group():
    """Create a group"""
    pass


def update_group():
    """Update a group."""
    pass


def delete_group(group_id:int):
    """Delete a group."""
    result = requests.delete(f'{BASE_URL}/groups/:{group_id}?api_key={API_KEY}', verify=False)
    print({"Groups": result.content, "status code": result.status_code})


# TEMPLATES
def get_all_templates():
    templates = [API.templates.get()]
    for template in templates:
        print(template)


def get_template_by_id():
    result = requests.delete(f'{BASE_URL}/groups/:{group_id}?api_key={API_KEY}', verify=False)
    print({"Groups": result.content, "status code": result.status_code})


def create_template():
    pass


def update_template():
    pass


def delete_template():
    pass


# LANDING PAGES
def get_landing_pages():
    """Get all the landing pages"""
    result = requests.get(f'{BASE_URL}/pages?api_key={API_KEY}', verify=False)
    print({"Landing Pages": result.content, "status code": result.status_code})


def get_landing_page(lp_id: int):
    """Get landing page by ID"""
    result = requests.get(f'{BASE_URL}/pages/{lp_id}?api_key={API_KEY}', verify=False)
    print({"One Landing Page": result.content, "status code": result.status_code})


def create_landing_page():
    # ask user for the input.
    # input data: id, name, html, capture_credentials, capture_passwords, redirect_url, modified_date
    pass


def modify_landing_page():
    # method: put
    # input data: id, name, html, capture_credentials, capture_passwords, redirect_url, modified_date
    pass

def delete_landing_page():
    pass

# SENDING PROFILE
def get_sending_profile():
    pass


def get_profile_by_id():
    pass


def create_profile():
    pass


def update_profile():
    pass


def delete_profile():
    pass

if __name__ == '__main__':
    # test_api()
    # retrieve_all_campaign()
    # retrieve_single_campaign(1)
    # get_campaign_summary(1)
    delete_campaign(1)
    # get_all_templates()
