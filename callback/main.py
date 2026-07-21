import os

from fastapi import FastAPI, Request, Query
from starlette.responses import RedirectResponse

from callback.msal_app import create_msal_app

CRM_URL = os.environ['CRM_URL']
msal_app = create_msal_app()
app = FastAPI()


@app.get("/login/callback")
async def callback(
    request: Request,
    state: str = Query(...),
    code: str = Query(None),
):
    # (STATE) Session of the login
    print(f"state ======================> {state}")

    # If login is successful, `code` will be provided in the query params otherwise, None
    print(f"code ======================> {code}")

    # 1 -- Verify result of the integration/login
    query_params = dict(request.query_params)
    print(f"query_params ======================> {query_params}")

    # 2 -- If with error, fail fast
    if query_params.get('error'):
        print(f"error ======================> {query_params['error']}")
        print(f"error_description ======================> {query_params['error_description']}")
        return RedirectResponse(url="https://www.google.com?is_connected=False")

    # 3 -- No error, Do magic.
    # Do something special.. whatever

    # 3.1 --- Validate state from database to get the
    # [AUTH_CODE_FLOW] fetch the auth_code_flow from your database
    auth_code_flow: dict = {}

    # 3.2 --- Request access token using code
    result = msal_app.acquire_token_by_auth_code_flow(
        auth_code_flow=auth_code_flow,
        auth_response={'code': code, 'state': state},
        scopes=[f'{CRM_URL}/.default'],
    )
    access_token = result['access_token']
    print(f"access_token ======================> {access_token}")
    # 3.3 --- Save access token to database

    # 4 -- Where to next???
    return RedirectResponse(url=f"https://www.google.com?is_connected=True")
