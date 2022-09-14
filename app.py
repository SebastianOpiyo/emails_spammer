from flask import Flask
from gophish import Gophish, models, api
from gophish.models import *


app = Flask(__name__)
api_key = 'API_KEY'
api = Gophish(api_key, verify=False)


@app.route("/")
def home():
    return "<p>Hello Gophish Clone</p>"

# Retrieve all campaigns
def retrieve_all_campaign():
    # Get a list of all the campaigns
    for campaign in api.campaigns.get():
        print(campaign.name)

# Retrieve one campaign
def retrieve_asingle_campaign(campaign_id):
    # Get a one campaign
    return api.campaigns.get(campaign_id=campaign_id)

# Create a new Campaign
def create_email_campaign():
    groups = [Group(name='Existing Group')]
    page = Page(name='Existing Page')
    template = Template(name='Existing Template')
    smtp = SMTP(name='Existing Profile')
    url = 'http://phishing_server'
    campaign = Campaign(
        name='Example Campaign', groups=groups, page=page,
        template=template, smtp=smtp)

    campaign = api.campaigns.post(campaign)
    print(f'Campaign with ID: {campaign.id}, created successfuly.')


# Delete campaign by ID
def delete_campaign(campaign_id:int):
    # Delete a campaign
    api.campaigns.delete(campaign_id=campaign_id)

# Get campaign summary.
def get_campaign_summary(campaign_id=None):
    # get summary of a campaign
    if campaign_id:
        summaries = api.campaigns.summary()
        print(summaries)
    else:
        summary = api.campaigns.summary(campaign_id=campaign_id)
        print(summary)
    



'''
Attributes for sending the email:
---------------------------------
id (int) The result ID
first_name (str) The first name
last_name (str) The last name
email (str) The email address
position (str) The position (job role)
ip (str) The last seen IP address
latitude (float) The latitude of the ip
longitude (float) The longitude of the ip
status (str) The users status in the campaign
'''

