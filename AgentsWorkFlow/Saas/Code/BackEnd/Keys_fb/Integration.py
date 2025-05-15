from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel

from modules.modules import *


              
def CodeFlaskBackEnd_Keys_fb_STATIC(session_id, appcompany,
                                   user_credentials,
                                   firebase_db_url
                                   
                            ):
   
    path_ProjectWeb = "/app/LocalProject"
    os.chdir(path_ProjectWeb)
    path_html = f"templates"
    path_js = f"static/js"
    path_css = f"static/css"
    doc_md = f"doc_md"
    path_Keys = f"Keys"
    path_credentials = f"{path_Keys}/appcompany.json"

    with open(path_credentials, "w") as f:
        json.dump(user_credentials, f, indent=2)

    firebase_keys = f'''
firebase_json_path="{path_credentials}"
firebase_db_url='{firebase_db_url}'
    '''

    with open(f"{path_Keys}/keys.env", "a") as f:
        f.write(firebase_keys)

    user_code_init_firebase = '''
from firebase_admin import initialize_app, credentials
import os
from dotenv import load_dotenv, find_dotenv

def init_firebase():
    dotenv_path= os.path.join(os.path.dirname(__file__), "keys.env")
    load_dotenv(dotenv_path=dotenv_path)
    firebase_json_path = os.getenv("firebase_json_path")
    firebase_db_url = os.getenv("firebase_db_url")
    cred = credentials.Certificate(firebase_json_path)
    app = initialize_app(cred, {
        'databaseURL': firebase_db_url
    })
    return app


    '''

    with open(f"{path_Keys}/fb.py", "w") as f:
        f.write(user_code_init_firebase)


