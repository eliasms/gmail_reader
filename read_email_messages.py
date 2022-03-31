from __future__ import print_function
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Get Messages
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute() 
    messages = results.get('messages', [])

    # if not labels
    if not messages:
        print ('No messages found.')
    # Filter message and get content
    else:
        query_msg = service.users().messages().list(
            userId='me',
            q="Código de segurança da conta da Microsoft",
            maxResults=1).execute()
        messages_content = query_msg.get("messages")[0]
        id_msg = messages_content['id']
        msg = service.users().messages().get(userId='me', id=id_msg).execute()
        snippet = msg['snippet']

        print("Snippet:")
        print(snippet)

if __name__ == '__main__':
    main()