import json
from datetime import datetime

import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import ipdb



# generate the object to write on the sheet
# def sheet_init(BOARD_NAME):

#     json_key = json.load(open('G_Sheets_Credential.json'))
#     scope = ['https://spreadsheets.google.com/feeds']
#     credentials = SignedJwtAssertionCredentials(
#         json_key['client_email'],
#     	json_key['private_key'].encode(), 
#     	scope
#     	) # get email and key from creds
#     file = gspread.authorize(credentials) # authenticate with Google
#     sheet = file.open(BOARD_NAME).sheet1 # open sheet
#     return sheet

# write on sheet
def write(mapper, issue, w, PROJECT_NAME):

    # for map_key in mapper:
    #     cell = mapper[map_key] + str(line_controler)


    #     if(map_key == 'status'):
    #         if issue['fields']['status']['statusCategory']['key']:
    #             sheet.update_acell(cell, issue['fields']['status']['statusCategory']['key'])

    #     elif(map_key == 'key'):
    #         if issue[map_key]:
    #             sheet.update_acell(cell, issue[map_key]) 

    
    #     else:
    #         if issue['fields'][map_key]:
    #             if(map_key == 'Sprint'):
    #                 Str = issue['fields']['Sprint'][len(issue['fields']['Sprint']) - 1]
    #                 sprint = Str[Str.find("name=") + len("name="):Str.find(",goal=")]
    #                 sheet.update_acell(cell, sprint)

    #             elif(map_key == 'created' or map_key == 'updated'):
    #                 date = datetime.strptime(issue['fields'][map_key][0:10], '%Y-%m-%d')
    #                 sheet.update_acell(cell, date)

    #             elif(map_key == 'issuetype' or map_key == 'resolution'):
    #                 sheet.update_acell(cell, issue['fields'][map_key]['name'])

    #             else:
    #                 sheet.update_acell(cell, issue['fields'][map_key])

    #try:
        #Str = issue['fields']['Sprint'][len(issue['fields']['Sprint']) - 1]
        #sprint = Str[Str.find("name=") + len("name="):Str.find(",goal=")]
    #except:
        #sprint = ''

    try:
        resolution = issue['fields']['resolution']['name']
    except:
        resolution = 'none'


    w.writerow({
        'project':PROJECT_NAME,
        'key':issue['key'],
        'status':issue['fields']['status']['statusCategory']['key'],
        'Épico':issue['fields']['Épico'],
        'labels':issue['fields']['labels'],
        'created':datetime.strptime(issue['fields']['created'][0:10], '%Y-%m-%d'),
        'updated':datetime.strptime(issue['fields']['updated'][0:10], '%Y-%m-%d'),
        'summary':issue['fields']['summary'],
        'resolution':resolution,
        'issuetype':issue['fields']['issuetype']['name'],
        #'history':issue['fields']['history'],
        #'logged':issue['fields']['logged'],
    })



