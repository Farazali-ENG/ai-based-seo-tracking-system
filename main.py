from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import os, pickle
from datetime import date, timedelta
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from requests.exceptions import HTTPError

app = FastAPI()

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
REDIRECT_URI = "http://localhost:8000/oauth2callback"

@app.get("/authorize")
def authorize():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    auth_url, _ = flow.authorization_url(prompt='consent')
    return RedirectResponse(auth_url)

@app.get("/oauth2callback")
def oauth2callback(request: Request):
    if "code" not in request.query_params:
        return {"error": "Missing code in callback. Authorization failed or denied."}

    code = request.query_params["code"]
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    flow.fetch_token(code=code)
    creds = flow.credentials

    with open("token.pkl", "wb") as token_file:
        pickle.dump(creds, token_file)

    return {"message": "Authentication successful. Token saved."}


@app.get("/search-console/data")
def get_search_console_data(site_url: str):
    if not os.path.exists("token.pkl"):
        return {"error": "Not authenticated. Please visit /authorize first."}

    
    end_date = date.today()
    start_date = end_date - timedelta(days=30)

    creds = pickle.load(open("token.pkl", "rb"))
    service = build('searchconsole', 'v1', credentials=creds)

    request = {
    'startDate': start_date.isoformat(),
    'endDate': end_date.isoformat(),
    'dimensions': ['page'],  # Focus on data for individual blog pages
    'rowLimit': 50
}

    try:
        response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        return response
    except HTTPError as e:
        return {
            "error": "Failed to fetch Search Console data.",
            "details": str(e)
        }