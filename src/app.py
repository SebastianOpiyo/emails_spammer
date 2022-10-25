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
@click.option('--template_id', prompt="Enter Template ID:", help="Pass Template ID to Fetch")
def getTemplateById(template_id):
    """Get template by ID"""
    from api_points import get_template_by_id
    get_template_by_id(int(template_id))


@click.command()
@click.option('--name', prompt="Enter template Name:", help="New Group name")
@click.option('--html', prompt="Enter HTML string:", help="HTML code for the page(Optional)")
@click.option('--text', prompt="Enter Text if NO HTML:", help="Send as Email Text")
@click.option('--time', prompt="Enter Time :", help="Time for template launch")
def createTemplate(name, html, text, time):
    """Create a template"""
    from api_points import create_template
    create_template(name, html, text, time)


@click.command()
@click.option('--template_id', prompt="Enter template ID:", help="ID for template to update")
@click.option('--name', prompt="Enter template Name:", help="New Group name")
@click.option('--html', prompt="Enter HTML string:", help="HTML code for the page(Optional)")
@click.option('--text', prompt="Enter Text if NO HTML:", help="Send as Email Text")
@click.option('--time', prompt="Enter Time :", help="Time for template launch")
def updateTemplate(template_id, name, html, text, time):
    """Update a template"""
    from api_points import update_template
    update_template(template_id, name, html, text, time)


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
@click.option('--page_id', prompt="Enter Landing Page ID:", help="Landing Page ID to Delete")
def getLandingPageById(page_id):
    """Get a landing page by its ID"""
    from api_points import get_landing_page
    get_landing_page(int(page_id))


@click.command()
@click.option('--name', prompt="Enter Landing Page Name:", help="New landing page name")
@click.option('--html', prompt="Enter Page HTML:", help="HTML code for the page(Optional)")
@click.option('--redirect_url', prompt="Enter Redirect URL:", help="URL to direct targets to after they submit data")
@click.option('--capture_credentials', prompt="Capture Credentials: True/False[Default: False]:",
              help="Whether or not landing page should capture credentials")
@click.option('--capture_passwords', prompt="Capture Passwords True/False[Default: False]:",
              help="Whether or not landing page should capture passwords")
def createLandingPage(name, html, redirect_url, capture_credentials, capture_passwords):
    """Create a landing page"""
    capture_passwords, capture_credentials = False, False
    if capture_passwords == "True":
        capture_passwords = True
    if capture_credentials == "True":
        capture_credentials = True

    from api_points import create_landing_page
    create_landing_page(name, html, redirect_url, capture_credentials, capture_passwords)


@click.command()
@click.option('--page_id', prompt="Enter Landing Page ID:", help="ID for the page to be modified")
@click.option('--name', prompt="Enter Landing Page Name:", help="New landing page name")
@click.option('--html', prompt="Enter Page HTML:", help="HTML code for the page(Optional)")
@click.option('--redirect_url', prompt="Enter Redirect URL:", help="URL to direct targets to after they submit data")
@click.option('--capture_credentials', prompt="True/False[Default: False]:",
              help="Whether or not landing page should capture credentials")
@click.option('--capture_passwords', prompt="True/False[Default: False]:",
              help="Whether or not landing page should capture passwords")
def updateLandingPage(page_id, name, html, redirect_url, capture_credentials, capture_passwords):
    """Update a landing page"""
    from api_points import modify_landing_page
    modify_landing_page(page_id, name, html, redirect_url, capture_credentials, capture_passwords)


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
@click.option('--smtp_id', prompt="Enter Profile ID:", help="Pass Profile ID to Delete")
def getProfileById(smtp_id):
    """Get a profile by ID"""
    from api_points import get_profile_by_id
    get_profile_by_id(int(smtp_id))


@click.command()
@click.option('--name', prompt="Enter profile Name:", help="New Profile name")
@click.option('--interface_type', prompt="Enter Interface Type:",
              help="The Type of SMTP Connection(Unless otherwise, always use SMTP)")
@click.option('--from_address', prompt="Enter Email Address:", help="Address to send Emails from.")
@click.option('--host', prompt="Enter host:port of SMTP Server:", help="The host:port of SMTP Server")
@click.option('--ignore_cert_errors', prompt="Ignore SSL Cert: [True/False]",
              help="Ignore SSL Certificate validation Errors")
def createProfile(name, from_address, interface_type, host, ignore_cert_errors):
    """Create a profile"""
    from api_points import create_profile
    create_profile(name, interface_type, host, from_address, ignore_cert_errors)


@click.command()
@click.option('--profile_id', prompt="Enter profile ID:", help="ID of profile to update")
@click.option('--name', prompt="Enter profile Name:", help="New Profile name")
@click.option('--interface_type', prompt="Enter Interface Type:",
              help="The Type of SMTP Connection(Unless otherwise, always use SMTP)")
@click.option('--from_address', prompt="Enter Email Address Address:", help="Address to send Emails from.")
@click.option('--host', prompt="Enter HOST port of SMTP Server:", help="The host:port of SMTP Server")
@click.option('--ignore_cert_errors', prompt="Ignore SSL Cert: [True/False]",
              help="Ignore SSL Certificate validation Errors")
def updateProfile(profile_id, name, from_address, interface_type, host, ignore_cert_errors):
    """Update a profile"""
    from api_points import update_profile
    update_profile(profile_id, name, from_address, interface_type, host, ignore_cert_errors)


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
