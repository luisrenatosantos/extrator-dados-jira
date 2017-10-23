import os


#Alterar para os dados do seu projeto
JIRA_USER = ''
JIRA_PASSWORD = ''
PROJECTS_NAME = 'ADS'

options = {
    'server': 'https://magazineluiza.atlassian.net',
    }

DESIRED_FIELDS=','.join((
    'status',
    'customfield_11310',
    'labels',
    'summary',
    'issuetype',
    'changelog',
    #'logged',
))

CSV_FIELDS = {
    'key': 'id',
    'summary': 'descricao',
    'customfield_11310': 'epico',
    'labels': 'labels',
    'issuetype': 'tipo',
}

CHANGELOG_FIELDS = {
    'from': 'Status inicial',
    'to': 'Status pos mudanca',
    'date': 'data'
}

METRICS_FIELDS = {
    'time': 'tempo',
}

CUSTOM_FIELDS_TRANSLATION = {
    'customfield_11310': 'Épico',
}

MAPPER = {
    'key':'A',
    'status':'B',
    'Épico':'C',
    'labels':'D',
    'created':'E',
    'updated':'F',
    'summary':'G',
    'resolution':'H',
    'issuetype':'I',
    #'history':'J',
    #'logged':'L',
}

FIELD_NAMES = [
    'project',
    'key',
    'status',
    'Épico',
    'labels',
    'created',
    'updated',
    'summary',
    'resolution',
    'issuetype',
    #'history',
    #'logged',
]