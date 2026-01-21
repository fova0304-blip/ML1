from fastapi import FastAPI 

app = FastAPI()

@app.post("/health")
def health_check_api():
    return 

@app.post("/predict")
def predict_api():
    return 