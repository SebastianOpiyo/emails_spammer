from gophish import Gophish, models, api
# from gophish.models import *
from flask import jsonify
import requests


API_KEY = '703d6d6d4f3c5fbc00861221333f5c3960f5971b3bebfc7928ce014e78dab579'
BASE_URL= 'http://localhost:3333/api/'
api = Gophish(API_KEY, host=f'{BASE_URL}', verify=False)


# newCmpgnBut = Button(self, text="NEW CAMPAIGN", command=newCampaign(), bg='black', fg='white')
# newCmpgnBut.pack()

def retrieve_all_campaign():
    # Get a list of all the campaigns
    for campaign in api.campaigns.get():
        print(campaign.name)
        

if __name__ == "__main__":
    retrieve_all_campaign()