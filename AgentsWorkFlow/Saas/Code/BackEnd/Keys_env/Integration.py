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
    print(f"CodeFlaskBackEndKeysenvAgent: {input_data.FrontEndContent}")
              
def CodeFlaskBackEndKeysenvAgent(session_id, appcompany,
                                path_ProjectWeb,
                                path_html,
                                path_js,
                                path_css,
                                doc_md,
                                Keys_path,
                                user_code_init_env,
                            ):
   
    os.chdir(path_ProjectWeb)


    # session_id_CodeFrontEndDecisionDashboard = "teste_handoff_CodeFrontEndDecisionDashboard"
    # agent_, handoff_obj_CodeFrontEndDecisionDashboard = CodeFrontEndDecisionDashboard(session_id_CodeFrontEndDecisionDashboard, appcompany)

# {RECOMMENDED_PROMPT_PREFIX}\n
# ---

# Ao final de sua execução, utilize o Handoffs transfer_to_code_front_end_dashboard_sprint_14_agent
# Ao final de sua execução, Encaminhe o usuário para o agente de Code Front End Dashboard Sprint 14 Agent
# prossiga com a criacao do dashboard da aplicacao 
# Encaminhe ao agente Code Front End Dashboard Sprint 14 Agent 
# ---

# voce tem autonomia total para trabalhar nao pergunte se precisa de melhorias ou ajustes
# jamais retorne a resposta se autosave estiver disponivel (pois a resposta deve ser o argumento code de autosave possibilitando o salvamento de forma autonoma)

# ---


    agent_ids = ['Keys_env']
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
        # handoffs=[handoff_obj_CodeFrontEndDecisionDashboard],
    )


    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=FrontEndData,
    )
    return agent, handoff_obj