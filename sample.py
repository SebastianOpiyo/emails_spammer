from gophish import Gophish, models, api
# from gophish.models import *
import requests


API_KEY = '4cd6dbec0d8a329c69e2d73499465786cb5fbcc8d717241a6d2698ac660e9eb4'
BASE_URL= 'https://localhost:3333'
api = Gophish(API_KEY, host=f'{BASE_URL}', verify=False)

# def newCampaign():
#     groups = [Group(name='testgroup')]
#     page = Page(name='Linkedin')
#     template = Template(name='Linkedin')
#     smtp = SMTP(name='LinkedIN')
#     url = 'http://192.168.1.20'
#     campaign = Campaign(name='Example Campaign', groups=groups, page=page, template=template, smtp=smtp)
#     campaign = api.campaigns.post(campaign)


# newCmpgnBut = Button(self, text="NEW CAMPAIGN", command=newCampaign(), bg='black', fg='white')
# newCmpgnBut.pack()

def retrieve_all_campaign():
    # Get a list of all the campaigns
    for campaign in api.campaigns.get():
        print(campaign.name)
        

if __name__ == "__main__":
    retrieve_all_campaign()