
# import required libraries 
import uvicorn 
from fastapi import FastAPI
from joblib import load

# import ML Package
import joblib,os


# Model
the_model = joblib.load('a_model.joblib')

# init App
app = FastAPI()

# Routes
@app.get('/')
async def index():
    return {"text": "Simple ML Classifier"}

@app.get('/items/{name}')
async def get_items(name):
    return {"name":name}

@app.get('/predict/{x},{y},{z}')
async def predict(x:int,y:int,z:int):
    prediction = the_model.predict([[x,y,z]])
    return {"The predicted gender for the height x weight y and shoe size z is" : prediction[0]}


if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1", port=8000)


