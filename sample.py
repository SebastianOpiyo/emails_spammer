from gophish import Gophish, models, api
# from gophish.models import *
from flask import jsonify
import requests


API_KEY = '4cd6dbec0d8a329c69e2d73499465786cb5fbcc8d717241a6d2698ac660e9eb4'
BASE_URL= 'http://localhost:3333'
api = Gophish(API_KEY, host=f'{BASE_URL}', verify=False)


# newCmpgnBut = Button(self, text="NEW CAMPAIGN", command=newCampaign(), bg='black', fg='white')
# newCmpgnBut.pack()

def retrieve_all_campaign():
    # Get a list of all the campaigns
    for campaign in api.campaigns.get():
        print(campaign.name)
        

if __name__ == "__main__":
    retrieve_all_campaign()