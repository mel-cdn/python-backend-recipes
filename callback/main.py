from fastapi import FastAPI, Request, Query
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/login/callback")
async def callback(
    request: Request,
    state: str = Query(...),
    code: str = Query(None),
):
    print(f"state ======================> {state}")
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
    # 3.1 --- Validate state
    # 3.2 --- Request access token using code
    # 3.3 --- Save access token to database

    # 4 -- Where to next???
    return RedirectResponse(url=f"https://www.google.com?is_connected=True")
