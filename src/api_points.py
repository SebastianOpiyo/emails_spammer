from gophish import Gophish, models, api
from gophish.models import *
from jinja2 import TemplateNotFound
import json
import requests

API_KEY = '703d6d6d4f3c5fbc00861221333f5c3960f5971b3bebfc7928ce014e78dab579'
BASE_URL = 'https://172.16.30.99:3333/api/'
API = Gophish(API_KEY, host=f'{BASE_URL}', verify=False)


# TEST API
def test_api():
    """Testing the API end point to ensure all is working fine."""
    result = requests.get(f'{BASE_URL}/templates/?api_key={API_KEY}', verify=False)
    print('Test Result \n')
    print({"result": [result.content]})


# Reset API Key
def reset_api_key():
    print(f'Reset the API Key')


# Retrieve all campaigns
def retrieve_all_campaign():
    # Get a list of all the campaigns
    result = requests.get(f'{BASE_URL}/campaigns/?api_key={API_KEY}', verify=False)
    print({"result": [result.content]})


# Retrieve one campaign
def retrieve_single_campaign(campaign_id):
    # Get a one campaign
    campaign = API.campaigns.get(campaign_id=campaign_id)
    if not campaign:
        return jsonify({"msg": "No Campaigns at the moment", "status": "400"})
    return make_response(campaign, 200)


# Create a new Campaign
def create_email_campign():
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


# Delete campaign by ID
def delete_campaign(campaign_id: int):
    # Delete a campaign
    API.campaigns.delete(campaign_id=campaign_id)


# Get campaign summary.
def get_campaign_summary(campaign_id=None):
    if campaign_id:
        summaries = API.campaigns.summary()
        print(summaries)
    else:
        summary = API.campaigns.summary(campaign_id=campaign_id)
        print(summary)

# GROUPS

# TEMPLATES
def get_all_templates():
    templates = [API.templates.get()]
    for template in templates:
        print(template)
    # print(json.dumps(templates))

# LANDING PAGES

# SENDING PROFILE


if __name__ == '__main__':
    test_api()
    # get_all_templates()
