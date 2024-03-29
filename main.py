# main.py
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
import appsignal
appsignal.start()

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
	return {"item_id": item_id}

FastAPIInstrumentor().instrument_app(app)
