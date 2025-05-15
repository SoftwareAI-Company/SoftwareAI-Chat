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
    print(f"Navigation JS FrontEnd: {input_data.FrontEndContent}")
    # response = requests.post("http://localhost:5000/agent/refund", json={"input": input_data.reason})
    # reply = response.json().get("reply")
              
def CodeNavigationJSFrontEnd(
                        session_id, 
                        appcompany,
                        path_ProjectWeb,
                        path_html,
                        path_js,
                        path_css,
                        doc_md,
                        Keys_path,
                        checkout_payment_button,
                        checkout_payment_selected,
                    ):
   

    os.chdir(path_ProjectWeb)
    path_Keys = Keys_path


    agent_ids = ['NavigationJS']
    agents_metadata = EgetMetadataAgent(agent_ids)

    name = agents_metadata['NavigationJS']["name"]
    model = agents_metadata['NavigationJS']["model"]
    instruction = agents_metadata['NavigationJS']["instruction"]
    try:
        tools = agents_metadata['NavigationJS']["tools"]
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
        # handoffs=[handoff_obj_CodeDocumentationStaticjsAgent],
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
from modules.Egetoolsv2 import *
from modules.EgetMetadataAgent import *


# from AgentsWorkFlow.Saas.Code.BackEnd.Sprint6.Integration import CodeFlaskBackEndSprint6Agent

class FrontEndData(BaseModel):
    FrontEndContent: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: FrontEndData):
    print(f"Navigation JS FrontEnd: {input_data.FrontEndContent}")
    # response = requests.post("http://localhost:5000/agent/refund", json={"input": input_data.reason})
    # reply = response.json().get("reply")
              
def CodeNavigationJSFrontEnd(
                        session_id, 
                        appcompany,
                        path_ProjectWeb,
                        path_html,
                        path_js,
                        path_css,
                        doc_md,
                        Keys_path,
                        checkout_payment_button,
                        checkout_payment_selected,
                    ):
   

    os.chdir(path_ProjectWeb)
    path_Keys = Keys_path


# ### 📥 autoupload  
#   - repo_name: nome do projeto armazenado no historico de conversas
#   - repo_owner: {repo_owner}  
#   - softwarepypath: {path_html}/checkout.html e {path_js}/checkout-payment-button.js (no caso de 2 arquivos utilize a ferramenta 1 vez para cada arquivo)
#   - token: {githubtoken}

# ### 1️⃣ Executar `autogetstructure`  
# Para compreender onde estao os arquivos mencionados com base na **estrutura completa de diretórios e arquivos** do repositório retornados pela ferramenta.
# autogetstructure:
# - branch_name: main
# - repo_name:  nome do projeto armazenado no historico de conversa
# - repo_owner: {repo_owner}
# - github_token: {githubtoken}
# - path: pasta a ser procurada (caso queira obter todas a estrutura de pasta basta deixar assim "")

# ### 2️⃣ Executar `autogetfilecontent`  
# Para obter o conteúdo **completo** do arquivo mencionado (Se mencionado mais de um execute a ferramenta na quantidade dos arquivos mencionados nos Objetivos)
# autogetfilecontent:
# - branch_name: main
# - repo_name:  nome do projeto armazenado no historico de conversa
# - companyname: {repo_owner}
# - file_path: <caminho/relativo/para/arquivo.extencao>
# - github_token: {githubtoken}

# {RECOMMENDED_PROMPT_PREFIX}\n
# ---

# Ao final de sua execução, utilize o Handoffs transfer_to_code_initial_flask_back_end_agent.
# Ao final de sua execução, Encaminhe o usuário para o agente de Code Initial Flask BackEnd Agent
# prossiga com a geração do código BackEnd específico para a aplicacao 
# voce tem autonomia total para trabalhar nao pergunte se precisa de melhorias ou ajustes
# jamais retorne a resposta se autosave estiver disponivel (pois a resposta deve ser o argumento code de autosave possibilitando o salvamento de forma autonoma)

# ---


    agent_ids = ['NavigationJS']
    agents_metadata = EgetMetadataAgent(agent_ids)

    name = agents_metadata['NavigationJS']["name"]
    model = agents_metadata['NavigationJS']["model"]
    instruction = agents_metadata['NavigationJS']["instruction"]
    try:
        tools = agents_metadata['NavigationJS']["tools"]
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
        # handoffs=[handoff_obj_CodeDocumentationStaticjsAgent],
    )

    
    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=FrontEndData,
    )
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
    return agent, handoff_obj