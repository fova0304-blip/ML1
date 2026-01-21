'''
model.py:
입력값을 ML 모델이 이해할 수 있는 형태로 바꾸고,
모델의 출력값을 다시 의미 있는 값으로 돌려준다
'''
from schemas import PredictRequest
import joblib
from pydantic import BaseModel

model = joblib.load("model/train_model.joblib")

def proba_result(data:PredictRequest):
    X=[[
        data.age,
        data.gender,
        data.height,
        data.weight,
        data.ap_hi,
        data.ap_lo,
        data.cholesterol,
        data.gluc,
        data.smoke,
        data.alco,
        data.active
    ]]

    proba = float(model.predict_proba(X)[0][1])
    result = int(model.predict(X)[0])
    return proba,result

# [ [x,y] ] -> 2차원으로 리턴하니 [:,1] -> y즉 병이 있을확률을 리턴
# probability = model.predict_proba(PredictRequest)[:,1] 
# result = model.predict(PredictRequest)


