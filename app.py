from flask import Flask, render_template, request
from gophish import Gophish, models, api
from gophish.models import *
from jinja2 import TemplateNotFound



app = Flask(__name__)
API_KEY = '4cd6dbec0d8a329c69e2d73499465786cb5fbcc8d717241a6d2698ac660e9eb4'
BASE_URL= 'https://localhost:3333/api/templates'
api = Gophish(API_KEY, host=f'{BASE_URL}', verify=False)


# Dashboard
@app.route("/")
def dashboard():
    return render_template('dashboard.html')


# Reset API Key
def reset_api_key():
    print(f'Reset the API Key')



def api_request(request):
    '''Returns the data from a request (eg /groups)'''
    url = f'{BASE_URL}{request}?token={API_KEY}'
    req = requests.get(url)

    if not req.content:
        return None

    # We only want the data associated with the "response" key
    return json.loads(req.content)['response']



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
@app.route("/createNewCampaign")
def create_email_campign():
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
    if campaign_id: 
        summaries = api.campaigns.summary()
        print(summaries)
    else:
        summary = api.campaigns.summary(campaign_id=campaign_id)
        print(summary)
    