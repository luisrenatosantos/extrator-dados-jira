import sys
import csv

import ipdb

import settings
import jira_obj
import writer
from datetime import datetime


date_pattern = '%Y-%m-%dT%H:%M:%S.%f%z'


def get_dict(d_origin, fields):
    return {v: d_origin.get(k) for k, v in fields.items()}


issues = jira_obj.obj_generator(settings.PROJECTS_NAME)
with open('Metricas.csv', 'w') as csvfile:
    fieldnames = []
    fieldnames.extend(settings.CSV_FIELDS.values())
    fieldnames.extend(settings.CHANGELOG_FIELDS.values())
    #fieldnames.extend(metrics_fields)

    w = csv.DictWriter(csvfile, fieldnames=fieldnames)
    w.writeheader()
    #ipdb.set_trace()
    for issue in issues.values():
        issue.update(issue['fields'])
        issue['issuetype'] = issue['issuetype']['name']
        issue['labels'] = ','.join(issue['labels'])
        issue['customfield_11310'] = issue['customfield_11310'] if issue['customfield_11310'] else '-'
        issue_d = get_dict(issue, settings.CSV_FIELDS)

        changelogs = issue.get('changelog')

        if changelogs:
            for changelog in changelogs:
                changelog_d = get_dict(changelog, settings.CHANGELOG_FIELDS) 
                date = changelog_d['data']
                date = datetime.strptime(date, date_pattern)
                changelog_d['data'] = date.strftime('%Y-%m-%d %H:%M')
                changelog_d.update(issue_d)
                w.writerow(changelog_d)
        else:
                w.writerow(issue_d)
    