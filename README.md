# Google Search Console API

This repository provides a FastAPI-based REST API to fetch performance data from Google Search Console using OAuth 2.0.

It returns search queries and related SEO metrics like clicks, impressions, CTR, and position — all for the last 30 days.

---

## 📊 Endpoint

### `GET /search-console/data?site_url=https://yourdomain.com`

Fetches top search queries from Google Search Console for the past 30 days.

#### Response Format:

{
  "rows": [
    {
      "keys": ["example keyword"],
      "clicks": 100,
      "impressions": 1200,
      "ctr": 0.083,
      "position": 2.5
    },
    ...
  ],
  "responseAggregationType": "byPage"
}


###  ✅ Prerequisites
Python 3.8+

Docker (optional, for containerized deployment)

Internet connection (to fetch live data from Google Search Console)


### 🔧 Setup Instructions
Option 1: Standard Setup
1. Clone the Repository

git clone https://github.com/yourusername/trends-keywords-api.git
cd trends-keywords-api

Install Dependencies
pip install -r requirements.txt

Run the API
uvicorn main:app --reload


## APIs
### 1. /authorize
This endpoint initiates the OAuth2 authorization process by redirecting the user to Google's consent screen.

Method: GET

Description:

When you visit this endpoint, you will be redirected to Google’s OAuth2 consent screen.

The user will be prompted to grant permission for the app to access Google Search Console data on their behalf. Only authorized users with appropriate permissions can use this endpoint to access the Search Console data.

Permissions: The user must have "Owner" or "Full" permissions for the site in Google Search Console to successfully authorize and retrieve data.

After successful authorization, a token is generated that can be used for subsequent API requests.

Example Request:
GET http://localhost:8000/authorize
Response: Redirects to Google’s OAuth2 consent screen.

### 2. /oauth2callback
This endpoint handles the callback from Google's OAuth2 consent screen. After the user grants permission, Google will redirect them here with an authorization code.

Method: GET

Parameters:

code: The authorization code sent by Google.

Description:

The code is exchanged for an access token, which is then saved as token.pkl on the local machine.

This token is used for future API requests to Google Search Console.

Example Request:
GET http://localhost:8000/oauth2callback?code=authorization_code
Response: A message indicating whether the authentication was successful or not.

{
  "message": "Authentication successful. Token saved."
}


### 3./search-console/data
This endpoint retrieves search analytics data from Google Search Console for a given site URL.

Method: GET

Parameters:

site_url: The URL of the website for which the search analytics data is requested.

Description:

Fetches search analytics data for the past 30 days, with a limit of 50 rows.

Requires successful OAuth2 authentication (i.e., a valid token.pkl file).

The data is aggregated by page for the specified site URL.

Example Request:
GET http://localhost:8000/search-console/data?site_url=https://theshroomgroove.com

Response: Returns search analytics data for the specified site URL.

Example Response:
{
  "rows": [
    {
      "keys": ["query"],
      "clicks": 100,
      "impressions": 5000,
      "ctr": 2.0,
      "position": 10.0
    },
    ...
  ],
  "responseAggregationType": "byPage"
}
### Docker Setup
This application is also containerized using Docker. You can use Docker to build and run the app in an isolated environment.

Build the Docker Image:
In the project directory (where the Dockerfile is located), run:

docker build -t seo-optimization .

Run the Docker Container:
Once the image is built, you can run the container:
docker run -d -p 8000:8000 seo-optimization

This will run the FastAPI app inside a Docker container and make it accessible at http://localhost:8000.

Access the API:
Once the Docker container is running, you can access the app at http://localhost:8000. Follow the same steps to authenticate and use the API as described in the API documentation above.

Troubleshooting
OAuth2 Errors:
If you encounter any errors during the OAuth2 flow (like invalid_grant or access issues), ensure that your client_secret.json is correctly configured and your app is authorized for development use in the Google Cloud Console.

Ensure that the user has appropriate permissions (Owner or Full access) in Google Search Console for the site.

Docker Issues:
Ensure Docker is installed and running.

If you encounter issues with Docker, check that the Docker daemon is properly configured to build and run containers.
