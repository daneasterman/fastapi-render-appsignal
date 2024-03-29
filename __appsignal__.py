import os
from appsignal import Appsignal
from dotenv import load_dotenv
load_dotenv()

appsignal = Appsignal(
    active=True,
    name="fastapi-render-appsignal",    
    # https://docs.appsignal.com/python/configuration/options.html#option-push_api_key
    push_api_key=os.getenv("APPSIGNAL_API_KEY")
)
