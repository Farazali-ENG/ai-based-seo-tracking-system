from pytrends.request import TrendReq
from fastapi import FastAPI

app = FastAPI()
pytrends = TrendReq()

@app.get("/trends/keywords")
def get_trending_keywords(keyword: str):
    pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='US', gprop='')
    data = pytrends.interest_over_time()
    if not data.empty:
        trend_data = data[keyword].to_dict()
        return {"trend": trend_data}
    return {"message": "No data found"}
