def newCampaign():
    groups = [Group(name='testgroup')]
    page = Page(name='Linkedin')
    template = Template(name='Linkedin')
    smtp = SMTP(name='LinkedIN')
    url = 'http://192.168.1.20'
    campaign = Campaign(name='Example Campaign', groups=groups, page=page, template=template, smtp=smtp)
    campaign = api.campaigns.post(campaign)


newCmpgnBut = Button(self, text="NEW CAMPAIGN", command=newCampaign(), bg='black', fg='white')
newCmpgnBut.pack()