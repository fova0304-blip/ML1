from fastapi import FastAPI 
from model import proba_result
from schemas import PredictRequest, PredictResponse

app = FastAPI()

@app.post("/check")
def check_api():
    return {
        "test": "good"
    }

@app.post("/predict")
def predict_api(body:PredictRequest)->PredictResponse:
    # health_status={
    #     "age": body.age,
    #     "gender": body.gender,
    #     "height": body.height,
    #     "weight": body.weight,
    #     "ap_hi": body.ap_hi,
    #     "ap_lo": body.ap_lo,
    #     "cholesterol": body.cholesterol,
    #     "gluc": body.gluc,
    #     "smoke": body.smoke,
    #     "alco": body.alco,
    #     "active": body.active,
    # } 
    proba,result = proba_result(body)
    return {
        "probability": proba,
        "result": result
    }