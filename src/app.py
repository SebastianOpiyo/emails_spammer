from importlib.metadata import entry_points
import logging
import click

from flask import Flask, render_template, request
from gophish import Gophish, models, api
from gophish.models import *
from setuptools import setup


#   SETUP TOOL
# setup(
#     name="emailspammer",
#     version='0.1',
#     py_modules=['app']
#     install_requires=[
#         'Click',
#     ],
#     entry_points='''
#         [console_scripts]
#         emailspammer=app:cli
#     ''')


# COMMANDS GROUP FUNCTION

@click.group()
def main():
    """........Running the Email Spammer Application \n
    * To view the dashboard on the web page run... 'python app.py web\n' 
    * To view all commands available run...'python app.py --help'\n
    
    """
    pass


# TEST API ENDPOINT 

@click.command()
# @click.option('--versbose', is_flag=True, help="Will print verbose message")
def testapi():
    from api_points import test_api
    test_api()


# INITIATE WEB APP

@click.command()
@click.option('--host', default='0.0.0.0', help="Starts the web server.")
@click.option('--port', default=5000, type=int)
def web(host: str, port: int):
    from web import app
    app.run(host=host, port=port)


# RESET API KEY & FIX AUTH ISSUES
@click.command()
@click.option('--h', help='Reset or renew API key')
def resetapikey():
    from api_points import reset_api_key
    reset_api_key()


# CAMPAIGNS

@click.command()
def getAllCampaigns():
    """Get a list of all the campaigns"""
    from api_points import retrieve_all_campaign
    retrieve_all_campaign()


@click.command()
@click.option('-h', help="Get a single campaign")
@click.option('--campaignId', help="Get a single campaign")
def getSingleCampaign(campaignId):
    """ Get one campaign"""
    from api_points import retrieve_single_campaign
    retrieve_single_campaign(campaignId)


@click.command()
@click.option('-h', help="Create a new campaign")
def createNewCampaign():
    """Create a new campaign"""
    from api_points import create_email_campign
    create_email_campign()
    
    
@click.command()
@click.option('-h', help="Get campaign summary.")
def getCampaignSummary():
    """Get campaign summary."""
    from api_points import get_campaign_summary
    get_campaign_summary()
    

@click.command()
@click.option('-h', help="Delete a campaign")
def deleteCampaign():
    """Delete a campaign"""
    from api_points import delete_campaign
    delete_campaign()
    

@click.command()
@click.option('-h', help="Mark Campaign as complete")
def markCampaignComplete():
    """Mark Campaign as complete."""
    from api_points import mark_campaign_complete
    mark_campaign_complete()


# GROUPS

@click.command()
@click.option('-h', help="Get all Groups that exist")
def getGroups():
    """Get groups"""
    from api_points import get_groups
    get_groups()
    

@click.command()
@click.option('-h', help="Get Group by ID")
def getGroupById():
    """Get a group by Id"""
    from api_points import get_group_by_id
    get_group_by_id()
    

@click.command()
@click.option('-h', help="Create a Group")
def createGroup():
    """Create a group"""
    from api_points import create_group
    create_group()
    

@click.command()
@click.option('-h', help="Update a group")
def updateGroup():
    """Update a group."""
    from api_points import update_group
    update_group()
    
    
@click.command()
@click.option('-h', help="Delete a Group")
def deleteGroup():
    """Delete a group."""
    from api_points import delete_group
    delete_group()


# TEMPLATES

@click.command()
@click.option('-h', help="Get all Templates")
def getAllTempalates():
    """Get all templates"""
    from api_points import get_all_templates
    get_all_templates()
    

@click.command()
@click.option('-h', help="Get One template")
def getTemplateById():
    """Get template by ID"""
    from api_points import get_template_by_id
    get_template_by_id()
    
@click.command()
@click.option('-h', help="Create a new Template")
def createTemplate():
    """Create a template"""
    from api_points import create_template
    create_template()
    
@click.command()
@click.option('-h', help="Update tempalate")
def updateTemplate():
    """Update a template"""
    from api_points import update_template
    update_template()
    
@click.command()
@click.option('-h', help="Delete a Template")
def deleteTemplate():
    """Delete a template"""
    from api_points import delete_template
    delete_template()
    
@click.command()
@click.option('-h', help="Get all landing pages")
def getLandingPages():
    """Get landing page"""
    from api_points import get_landing_pages
    get_landing_pages()
    
@click.command()
@click.option('-h', help="Get One Landing Page")
def getLandingPageById():
    """Get a landing page by its ID"""
    from api_points import get_landing_page
    get_landing_page()
    

@click.command()
@click.option('-h', help="Create a Landing page")
def createLandingPage():
    """Create a landing page"""
    from api_points import create_landing_page
    create_landing_page()
    
    
@click.command()
@click.option('-h', help="Update landing page")
def updateLandingPage():
    """Update a landing page"""
    from api_points import modify_landing_page
    modify_landing_page()
    

@click.command()
@click.option('-h', help="Delete landing page")
def deletelandingPage():
    """Delete a landing page."""
    from api_points import delete_landing_page
    delete_landing_page()


# SENDING PROFILE 

@click.command()
@click.option('-h', help="Get all sending profile")
def getSendingProfile():
    """Get sending profile"""
    from api_points import get_sending_profile
    get_sending_profile()
    
@click.command()
@click.option('-h', help="Get Profile by ID")
def getProfileById():
    """Get a profile by ID"""
    from api_points import get_profile_by_id
    get_profile_by_id()
    
@click.command()
@click.option('-h', help="Create profile")
def createProfile():
    """Create a profile"""
    from api_points import create_profile
    create_profile()
    


@click.command()
@click.option('-h', help="Update profile")
def updateProfile():
    """Update a profile"""
    from api_points import update_profile
    update_profile()
    
@click.command()
@click.option('-h', help="Delete profile")
def deleteProfile():
    """Delete a profile"""
    from api_points import delete_profile
    delete_profile()
    
    
    
main.add_command(web)
main.add_command(testapi)
main.add_command(resetapikey)
main.add_command(getAllCampaigns)
main.add_command(getSingleCampaign)
main.add_command(createNewCampaign)
main.add_command(getCampaignSummary)
main.add_command(deleteCampaign)
main.add_command(markCampaignComplete)
main.add_command(getGroups)
main.add_command(getGroupById)
main.add_command(createGroup)
main.add_command(updateGroup)
main.add_command(deleteGroup)
main.add_command(getAllTempalates)
main.add_command(getTemplateById)
main.add_command(createTemplate)
main.add_command(updateTemplate)
main.add_command(deleteTemplate)
main.add_command(getLandingPages)
main.add_command(getLandingPageById)
main.add_command(createLandingPage)
main.add_command(updateLandingPage)
main.add_command(deletelandingPage)
main.add_command(getSendingProfile)
main.add_command(getProfileById)
main.add_command(createProfile)
main.add_command(updateProfile)
main.add_command(deleteProfile)


if __name__ == "__main__":
    main()
