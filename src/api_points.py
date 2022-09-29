from flask import Flask, render_template, request, jsonify, make_response
from gophish import Gophish, models, api
from gophish.models import *
from jinja2 import TemplateNotFound

app = Flask(__name__)
API_KEY = '3e35419d03ca86bd6dfa5e89f0e27a08d2832a7e452686c9068216a112e224a2'
BASE_URL = 'https://localhost:3333'
API = Gophish(API_KEY, host=f'{BASE_URL}', verify=False)


class Campaigns:

    def __init__(self):
        pass

    # Test API
    @staticmethod
    def test_api():
        print('Test api')
        # return make_response(API.smtp)

    # Reset API Key
    @staticmethod
    def reset_api_key():
        print(f'Reset the API Key')

    # Retrieve all campaigns
    @staticmethod
    def retrieve_all_campaign():
        # Get a list of all the campaigns
        campaign_names = []
        for campaign in API.campaigns.get():
            campaign_names.append(campaign.name)
        return make_response(jsonify(campaign_names), 200)

    # Retrieve one campaign
    @staticmethod
    def retrieve_single_campaign(campaign_id):
        # Get a one campaign
        campaign = API.campaigns.get(campaign_id=campaign_id)
        if not campaign:
            return jsonify({"msg": "No Campaigns at the moment", "status": "400"})
        return make_response(campaign, 200)

    # Create a new Campaign
    @staticmethod
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
    @staticmethod
    def delete_campaign(campaign_id: int):
        # Delete a campaign
        API.campaigns.delete(campaign_id=campaign_id)

    # Get campaign summary.
    @staticmethod
    def get_campaign_summary(campaign_id=None):
        if campaign_id:
            summaries = API.campaigns.summary()
            print(summaries)
        else:
            summary = API.campaigns.summary(campaign_id=campaign_id)
            print(summary)


def main():
    camp = Campaigns()
    camp.retrieve_all_campaign()


if __name__ == '__main__':
    main()
