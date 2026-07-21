import os
from uuid import uuid4

from msal import ConfidentialClientApplication

APP_ID = os.environ['APP_ID']
APP_SECRET = os.environ['APP_SECRET']


def create_login_url() -> str:
    app = ConfidentialClientApplication(
        client_id=APP_ID,
        authority=f'https://login.microsoftonline.com/common',
        client_credential=APP_SECRET,
    )

    state = str(uuid4())

    auth_code_flow = app.initiate_auth_code_flow(
        scopes=[f'https://mycrm.crm6.dynamics.com/.default'],
        redirect_uri='http://localhost:8000/login/callback',
        state=state,
    )

    print(f"auth_code_flow ======================> {auth_code_flow}")
    print(f"auth_code_flow['auth_uri'] ======================> {auth_code_flow['auth_uri']}")
    return auth_code_flow['auth_uri']


if __name__ == '__main__':
    create_login_url()
