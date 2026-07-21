import os
from uuid import uuid4

from callback.msal_app import create_msal_app

CRM_URL = os.environ['CRM_URL']


def create_login_url() -> str:
    app = create_msal_app()

    # [STATE] state, Microsoft will return this to the callback, for tracking the session of the login
    state = str(uuid4())

    auth_code_flow = app.initiate_auth_code_flow(
        scopes=[f'{CRM_URL}/.default'],
        redirect_uri='http://localhost:8000/login/callback',
        state=state,
    )

    # [AUTH_CODE_FLOW] save this database or somewhere, this will be needed in the callback
    print(f"auth_code_flow ======================> {auth_code_flow}")
    print(f"auth_code_flow['auth_uri'] ======================> {auth_code_flow['auth_uri']}")
    return auth_code_flow['auth_uri']


if __name__ == '__main__':
    create_login_url()
