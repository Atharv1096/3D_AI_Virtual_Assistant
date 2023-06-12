from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace these with your own values
SERVICE_ACCOUNT_FILE = 'strong-arbor-380716-bb47f7e2b9ca.json'
USER_EMAIL = 'kulkarniatharv73@gmail.com'

# Load the service account credentials
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/calendar'],
)

# Impersonate the user
creds = creds.with_subject(USER_EMAIL)

service = build('calendar', 'v3', credentials=creds)

event = {
    'summary': 'Test Event',
    'location': 'Somewhere',
    'description': 'A test event',
    'start': {
        'dateTime': '2023-05-09T09:00:00',
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': '2023-05-09T17:00:00',
        'timeZone': 'Asia/Kolkata',
    },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print(f'Event created: {event.get("htmlLink")}')
