<<<<<<< HEAD
from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel
# IMPORT SoftwareAI Libs 
from softwareai_engine_library.Inicializer._init_core_ import *
#########################################



from modules.modules import *


class Data(BaseModel):
  Content: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: Data):
  print(f"CodeRequirementsAndTimeline: {input_data.Content}")

def CodeRequirementsAndTimeline(
    session_id,
    user_email,
    path_ProjectWeb,
    path_html,
    path_js,
    path_css,
    doc_md,
    Keys_path,
    ):

   
    os.chdir(path_ProjectWeb)

    agent_ids = ['Timeline']
    agents_metadata = EgetMetadataAgent(agent_ids)


    name = agents_metadata[f'{agent_ids[0]}']["name"]
    model = agents_metadata[f'{agent_ids[0]}']["model"]
    instruction = agents_metadata[f'{agent_ids[0]}']["instruction"]
    try:
      tools = agents_metadata[f'{agent_ids[0]}']["tools"]
      Tools_Name_dict = Egetoolsv2(list(tools))
    except:
      pass

    instruction_formatado = format_instruction(instruction, locals())
    agent = Agent(
        name=str(name),
        instructions=f"""
        {instruction_formatado}        
        """,
        model=str(model),
        tools=Tools_Name_dict,
        # handoffs=[handoff_obj_codeindexfrontEnd],
    )

    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=Data,
    )
=======
from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel
# IMPORT SoftwareAI Libs 
from softwareai_engine_library.Inicializer._init_core_ import *
#########################################



from modules.modules import *


class Data(BaseModel):
  Content: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: Data):
  print(f"CodeRequirementsAndTimeline: {input_data.Content}")

def CodeRequirementsAndTimeline(
    session_id,
    user_email,
    path_ProjectWeb,
    path_html,
    path_js,
    path_css,
    doc_md,
    Keys_path,
    ):

   
    os.chdir(path_ProjectWeb)

    agent_ids = ['Timeline']
    agents_metadata = EgetMetadataAgent(agent_ids)

    name = agents_metadata['Timeline']["name"]
    model = agents_metadata['Timeline']["model"]
    instruction = agents_metadata['Timeline']["instruction"]
    tools = agents_metadata['Timeline']["tools"]

    Tools_Name_dict = Egetoolsv2(list(tools))
    agent = Agent(
        name=str(name),
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX}\n
        {instruction}        
        """,
        model=str(model),
        tools=Tools_Name_dict,
        # handoffs=[handoff_obj_codeindexfrontEnd],
    )

    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=Data,
    )
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
    return agent, handoff_obj