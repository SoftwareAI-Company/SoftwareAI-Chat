<<<<<<< HEAD
from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel


from modules.modules import *

class FrontEndData(BaseModel):
    FrontEndContent: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: FrontEndData):
    print(f"CodeDocumentationStaticjsAgent: {input_data.FrontEndContent}")

def CodeDocumentationStaticjsAgent(
                            session_id, 
                            appcompany,
                            path_ProjectWeb,
                            path_html,
                            path_js,
                            path_css,
                            doc_md,
                            Keys_path,
                        ):
   
    os.chdir(path_ProjectWeb)

    agent_ids = ['Staticjs']
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
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX}\n
        {instruction_formatado}        
        """,
        model=str(model),
        tools=Tools_Name_dict,
        # handoffs=[handoff_obj_CodeDocumentationTechnichAgent],
    )


    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=FrontEndData,
    )
=======
from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel


from modules.modules import *


from AgentsWorkFlow.Saas.Code.ProjectManager.Documentation.Technich.Integration import CodeDocumentationTechnichAgent


class FrontEndData(BaseModel):
    FrontEndContent: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: FrontEndData):
    print(f"CodeDocumentationStaticjsAgent: {input_data.FrontEndContent}")
    # response = requests.post("http://localhost:5000/agent/refund", json={"input": input_data.reason})
    # reply = response.json().get("reply")
              
def CodeDocumentationStaticjsAgent(
                            session_id, 
                            appcompany,
                            path_ProjectWeb,
                            path_html,
                            path_js,
                            path_css,
                            doc_md,
                            Keys_path,
                        ):
   
    os.chdir(path_ProjectWeb)


    agent_, handoff_obj_CodeDocumentationTechnichAgent = CodeDocumentationTechnichAgent(
                            session_id, 
                            appcompany,
                            path_ProjectWeb,
                            path_html,
                            path_js,
                            path_css,
                            doc_md,
                            Keys_path,
                        )


    agent_ids = ['Staticjs']
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
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX}\n
        {instruction_formatado}        
        """,
        model=str(model),
        tools=Tools_Name_dict,
        handoffs=[handoff_obj_CodeDocumentationTechnichAgent],
    )


    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=FrontEndData,
    )
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
    return agent, handoff_obj