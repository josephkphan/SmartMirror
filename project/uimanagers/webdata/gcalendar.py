from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from project.resources import var, varloader
import datetime
import re


def get_credentials(flags):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/calendar-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    CLIENT_SECRET_FILE = var.file_paths['gcalendar_key']
    APPLICATION_NAME = 'Google Calendar API Python Quickstart'

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials




def get_calendar_events():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    credentials = get_credentials(flags)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    var.calendar_data = {}
    counter = 0
    if not events:
        print('No upcoming events found.')
    for event in events:
        print(event)
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start)

        summary_string = '--no title--'
        description_string = '--no description--'
        location_string = '--no location--'
        date_time_string = ''
        if 'summary' in event:
            summary_string = event['summary']
        if 'description' in event:
            description_string = event['description']
        if 'location' in event:
            location_string = event['location']
        if 'start' in event:
            date_time_string = event['start']['date']

        event_data = {}
        try:
            event_data['summary'] = summary_string
        except Exception as e:
            print(e)

        try:
            event_data['description'] = re.sub('\n', '', description_string)
        except Exception as e:
            print(e)

        try:
            event_data['location'] = location_string.split(',')[0]
        except Exception as e:
            print(e)

        try:
            event_data['date'] = date_time_string[0:10]
        except Exception as e:
            print(e)

        try:
            event_data['start_time'] = date_time_string[11:16]
        except Exception as e:
            print(e)

        var.calendar_data[str(counter)] = event_data
        counter += 1
    varloader.save_data_to_json_file(var.calendar_data, var.file_paths['calendar_data'])

# sudo pip install --upgrade google-api-python-client
