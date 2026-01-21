import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import os
import joblib

# 데이터 로딩후, 모델훈련전 나누기
df = pd.read_csv("cardio_train.csv",sep=";")
X = df.drop(["id","cardio"],axis=1)
y = df["cardio"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# 모델 파라미터 설정후, 모델 저장해줌
rf = RandomForestClassifier(
    n_estimators=400,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features="sqrt",
    n_jobs=-1,
    random_state=42,
    class_weight="balanced",
)
rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))

os.makedirs("model",exist_ok=True)
joblib.dump(rf, "model/train_model.joblib")
