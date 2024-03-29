import os
import subprocess
from appsignal import Appsignal
from dotenv import load_dotenv
load_dotenv()

revision = None

try:
    revision = subprocess.check_output(
        "git log --pretty=format:'%h' -n 1", shell=True
    ).strip()
except subprocess.CalledProcessError:
  pass

appsignal = Appsignal(
    active=True,
    name="fastapi-render-appsignal",    
    # https://docs.appsignal.com/python/configuration/options.html#option-push_api_key
    push_api_key=os.getenv("APPSIGNAL_API_KEY"),
	revision=revision
)

