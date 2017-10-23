from jira import JIRA
from jira.client import JIRA
import re
import ipdb
import json

import settings

def obj_generator(BOARD_NAME):
    # Creating the object jira
    #jira = JIRA(options=settings.options, basic_auth = (settings.JIRA_USER, settings.JIRA_PASSWORD))
    #issues = jira.search_issues('project='+ BOARD_NAME,startAt=0, maxResults=1000, fields=settings.DESIRED_FIELDS, json_result=True)
    # interating through jira object and applying the dict
    #for issue in issues['issues']:
    	
    #        for key in issue['fields']:
    #            if key in settings.CUSTOM_FIELDS_TRANSLATION:
    #                new = settings.CUSTOM_FIELDS_TRANSLATION[key]
    #                issue['fields'][new] = issue['fields'].pop(key)

    #return issues


    #jira = JIRA(options=settings.options, basic_auth = (settings.JIRA_USER, settings.JIRA_PASSWORD))
    #issues = jira.search_issues('project='+ BOARD_NAME,startAt=0, maxResults=10000, fields=settings.DESIRED_FIELDS, json_result=True)
    #ipdb.set_trace()
    #keys = [issue['key'] for issue in issues['issues']]

    #for key in keys:  
        #issue = jira.issue(key , expand='changelog')
        #changelog = issue.changelog
        #for history in changelog.histories:
            #for item in history.items:
                #if item.field == 'status':
                    #print ('Date:' + history.created + ' From:' + item.fromString + ' To:' + item.toString)
    #return null
    #return issue


    jira = JIRA(options=settings.options, basic_auth = (settings.JIRA_USER, settings.JIRA_PASSWORD))
    issues = jira.search_issues('project='+ BOARD_NAME,startAt=0, maxResults=100, fields=settings.DESIRED_FIELDS, json_result=True)
    #ipdb.set_trace()

    issues = issues['issues']
    issues = {issue['key']:issue for issue in issues}

    for key, issue in issues.items():  
        issue_data = jira.issue(key, expand='changelog')
        for history in issue_data.changelog.histories:
            for item in history.items:
                if item.field == 'status':
                    if 'changelog' in issue:
                        issue['changelog'].append({
                            'date': history.created,
                            'from': item.fromString,
                            'to': item.toString
                        })
                    else:
                        issue['changelog'] = [{
                            'date': history.created,
                            'from': item.fromString,
                            'to': item.toString
                        }]
    return issues