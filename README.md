# Google Trends API
This repository provides a FastAPI-based REST API to fetch trending data for any keyword using the Google Trends API via the `pytrends` library.
---
## 📊 Endpoint
### `GET /trends/keywords?keyword=your_keyword`
Fetches hourly popularity scores for a given keyword over the past 7 days.
#### Response Format:
```json
{
  "trend": {
    "2025-03-14T04:00:00": 29,
    "2025-03-14T05:00:00": 43,
    ...
  }
}
```
---
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
## 📄 License
MIT License
