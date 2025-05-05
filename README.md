# Google Search Console API

This repository provides a FastAPI-based REST API to fetch performance data from Google Search Console using OAuth 2.0.

It returns search queries and related SEO metrics like clicks, impressions, CTR, and position — all for the last 30 days.

---

## 📊 Endpoint

### `GET /search-console/data?site_url=https://yourdomain.com`

Fetches top search queries from Google Search Console for the past 30 days.

#### Response Format:
```json
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
  "responseAggregationType": "byProperty"
}

## ✅ Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
- Internet connection (pytrends fetches live data)
---
## 🔧 Setup Instructions

### Option 1: Standard Setup
#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/trends-keywords-api.git
cd trends-keywords-api
```
#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
#### 3. Run the API
```bash
uvicorn app:app --reload
```
The API will be available at: [http://127.0.0.1:8000/trends/keywords?keyword=seo](http://127.0.0.1:8000/trends/keywords?keyword=seo)

### Option 2: Docker Setup
#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/trends-keywords-api.git
cd trends-keywords-api
```
#### 2. Build the Docker Image
```bash
docker build -t seo-tracking-app .
```
#### 3. Run the Docker Container
```bash
docker run -d -p 8000:8000 --name seo-tracker seo-tracking-app
```
The API will be available at: [http://localhost:8000/trends/keywords?keyword=seo](http://localhost:8000/trends/keywords?keyword=seo)

#### 4. Docker Management Commands
```bash
# View running containers
docker ps

# View container logs
docker logs seo-tracker

# Stop the container
docker stop seo-tracker

# Restart the container
docker start seo-tracker

# Remove the container
docker rm seo-tracker
```
---
## 🛠️ Testing in Postman
1. Run your server (either with uvicorn or Docker)
2. Open Postman:
   - Method: `GET`
   - URL: `http://127.0.0.1:8000/trends/keywords?keyword=seo`
3. You should see a JSON response with time-series trend data.
---
## 📖 requirements.txt
```
fastapi
uvicorn
pytrends
```
---
