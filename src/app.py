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
def testapi():
    """Test the base API end point."""
    from api_points import test_api
    test_api()


# INITIATE WEB APP

@click.command()
@click.option('--host', default='0.0.0.0', help="Starts the web server.")
@click.option('--port', default=5000, type=int)
def web(host: str, port: int):
    """Start the web server."""
    from web import app
    app.run(host=host, port=port)


# RESET API KEY & FIX AUTH ISSUES
@click.command()
def resetApiKey():
    """Reset the API KEY"""
    from api_points import reset_api_key
    reset_api_key()


# CAMPAIGNS

@click.command()
def getAllCampaigns():
    """Get a list of all the campaigns"""
    from api_points import retrieve_all_campaign
    retrieve_all_campaign()


@click.command()
@click.option('--campaign_id', prompt="Enter Campaign ID:", help="Pass campaign ID")
def getSingleCampaign(campaign_id):
    """ Get one campaign"""
    from api_points import retrieve_single_campaign
    retrieve_single_campaign(int(campaign_id))


@click.command()
@click.option('--camp_name', prompt="Enter Campaign Name:", help="New campaign name")
@click.option('--group_name', prompt="Enter Existing Group Name:", help="Existing Group name")
@click.option('--page_name', prompt="Enter Existing Page Name:", help="Existing Page name")
@click.option('--template_name', prompt="Enter Template Name:", help="Existing Template name")
@click.option('--smtp', prompt="Enter Existing SMTP Name:", help="Existing SMTP")
@click.option('--url', prompt="Enter URL:", help="Enter Phishing URL")
def createNewCampaign(camp_name, group_name, page_name, template_name, smtp, url):
    """Create a new campaign"""
    from api_points import create_email_campaign
    create_email_campaign(camp_name=camp_name, group_name=group_name, page_name=page_name,template_name=template_name,
                          smtp_name=smtp, url=url)


@click.command()
@click.option('--campaign_id', prompt="Enter Campaign ID:", help="Pass campaign ID")
def getCampaignSummary(campaign_id):
    """Get campaign summary."""
    from api_points import get_campaign_summary
    get_campaign_summary(campaign_id)


@click.command()
def getCampaignsSummaries():
    """Get campaign summary."""
    from api_points import get_campaigns_summaries
    get_campaigns_summaries()


@click.command()
@click.option('--campaign_id', prompt="Enter Campaign ID:", help="Pass campaign ID")
def deleteCampaign(campaign_id):
    """Delete a campaign"""
    from api_points import delete_campaign
    delete_campaign(campaign_id)


@click.command()
@click.option('--campaign_id', prompt="Enter Campaign ID:", help="Pass campaign ID")
def markCampaignComplete(campaign_id):
    """Mark Campaign as complete."""
    from api_points import mark_campaign_complete
    mark_campaign_complete(campaign_id)


# GROUPS

@click.command()
def getGroups():
    """Get all groups"""
    from api_points import get_groups
    get_groups()


@click.command()
@click.option('--group_id', prompt="Enter Group ID:", help="Pass Group ID")
def getGroupById(group_id):
    """Get a group by Id"""
    from api_points import get_group_by_id
    get_group_by_id(group_id)


@click.command()
@click.option('--name', prompt="Enter Group Name:", help="Group name")
@click.option('--email', prompt="Enter Target Email:", help="Email for the target")
@click.option('--first_name', prompt="Enter Target First Name:", help="Target first name")
@click.option('--last_name', prompt="Enter Target Last Name:", help="Target last name")
@click.option('--position', prompt="Enter Target position:", help="Target position")
def createGroup(email, first_name, last_name, position, name):
    """Create a group"""
    target = list()
    from api_points import create_group, add_target
    add_target(target, email, first_name, last_name, position)
    create_group(name, target)


@click.command()
@click.option('--group_id', prompt="Enter Group ID:", help="Pass Group ID")
@click.option('--name', prompt="Enter Group Name:", help="Edit Group name")
@click.option('--email', prompt="Enter Target Email:", help="Edit Email for the target")
@click.option('--first_name', prompt="Enter Target First Name:", help="Edit Target first name")
@click.option('--last_name', prompt="Enter Target Last Name:", help="Edit Target last name")
@click.option('--position', prompt="Enter Target position:", help="Edit Target position")
def updateGroup(group_id, name, email, first_name, last_name, position):
    """Update a group."""
    target = list()
    from api_points import update_group, add_target
    add_target(target, email, first_name, last_name, position)
    update_group(int(group_id), name, target)


@click.command()
@click.option('--group_id', prompt="Enter Group ID:", help="Pass Group ID to Delete")
def deleteGroup(group_id):
    """Delete a group."""
    from api_points import delete_group
    delete_group(int(group_id))


# TEMPLATES

@click.command()
def getAllTemplates():
    """Get all templates"""
    from api_points import get_all_templates
    get_all_templates()


@click.command()
def getTemplateById():
    """Get template by ID"""
    from api_points import get_template_by_id
    get_template_by_id()


@click.command()
def createTemplate():
    """Create a template"""
    from api_points import create_template
    create_template()


@click.command()
def updateTemplate():
    """Update a template"""
    from api_points import update_template
    update_template()


@click.command()
@click.option('--template_id', prompt="Enter Template ID:", help="Pass Template ID to Delete")
def deleteTemplate(template_id):
    """Delete a template"""
    from api_points import delete_template
    delete_template(int(template_id))


@click.command()
def getLandingPages():
    """Get landing page"""
    from api_points import get_landing_pages
    get_landing_pages()


@click.command()
def getLandingPageById():
    """Get a landing page by its ID"""
    from api_points import get_landing_page
    get_landing_page()


@click.command()
def createLandingPage():
    """Create a landing page"""
    from api_points import create_landing_page
    create_landing_page()


@click.command()
def updateLandingPage():
    """Update a landing page"""
    from api_points import modify_landing_page
    modify_landing_page()


@click.command()
@click.option('--page_id', prompt="Enter Page ID:", help="Pass Page ID to Delete")
def deleteLandingPage(page_id):
    """Delete a landing page."""
    from api_points import delete_landing_page
    delete_landing_page(int(page_id))


# SENDING PROFILE 

@click.command()
def getSendingProfile():
    """Get sending profile"""
    from api_points import get_sending_profile
    get_sending_profile()


@click.command()
def getProfileById():
    """Get a profile by ID"""
    from api_points import get_profile_by_id
    get_profile_by_id()


@click.command()
def createProfile():
    """Create a profile"""
    from api_points import create_profile
    create_profile()


@click.command()
def updateProfile():
    """Update a profile"""
    from api_points import update_profile
    update_profile()


@click.command()
@click.option('--smtp_id', prompt="Enter SMTP ID:", help="Profile ID to Delete")
def deleteProfile(smtp_id):
    """Delete a profile"""
    from api_points import delete_profile
    delete_profile(int(smtp_id))


main.add_command(web)
main.add_command(testapi)
main.add_command(resetApiKey)
main.add_command(getAllCampaigns)
main.add_command(getSingleCampaign)
main.add_command(createNewCampaign)
main.add_command(getCampaignSummary)
main.add_command(getCampaignsSummaries)
main.add_command(deleteCampaign)
main.add_command(markCampaignComplete)
main.add_command(getGroups)
main.add_command(getGroupById)
main.add_command(createGroup)
main.add_command(updateGroup)
main.add_command(deleteGroup)
main.add_command(getAllTemplates)
main.add_command(getTemplateById)
main.add_command(createTemplate)
main.add_command(updateTemplate)
main.add_command(deleteTemplate)
main.add_command(getLandingPages)
main.add_command(getLandingPageById)
main.add_command(createLandingPage)
main.add_command(updateLandingPage)
main.add_command(deleteLandingPage)
main.add_command(getSendingProfile)
main.add_command(getProfileById)
main.add_command(createProfile)
main.add_command(updateProfile)
main.add_command(deleteProfile)

if __name__ == "__main__":
    main()
