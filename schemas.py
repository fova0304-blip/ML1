from pydantic import BaseModel, Field

'''
'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo',
'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio'
'''

class PredictRequest(BaseModel):
    age: int
    gender: int
    height: int
    weight: float 
    ap_hi: int
    ap_lo: int
    cholesterol: int
    gluc: int
    smoke: int
    alco: int
    active: int


class PredictResponse(BaseModel):
    probability: float 
    result : int
