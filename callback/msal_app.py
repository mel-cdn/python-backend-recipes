import os

from msal import ConfidentialClientApplication

APP_ID = os.environ['APP_ID']
APP_SECRET = os.environ['APP_SECRET']


def create_msal_app() -> ConfidentialClientApplication:
    app = ConfidentialClientApplication(
        client_id=APP_ID,
        authority=f'https://login.microsoftonline.com/common',
        client_credential=APP_SECRET,
    )
    return app