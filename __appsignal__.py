import os
import subprocess
from appsignal import Appsignal
from dotenv import load_dotenv
load_dotenv()

revision = subprocess \
    .run(["git", "log", "--pretty=format:%h", "-n 1"], stdout=subprocess.PIPE) \
    .stdout \
    .decode("utf-8")

appsignal = Appsignal(
    active=True,
    name="fastapi-render-appsignal",    
    # https://docs.appsignal.com/python/configuration/options.html#option-push_api_key
    push_api_key=os.getenv("APPSIGNAL_API_KEY"),
	revision=revision
)

