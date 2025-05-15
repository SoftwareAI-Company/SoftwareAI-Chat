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
    print(f"CodeCheckoutFrontEnd: {input_data.FrontEndContent}")

              
def CodeCheckoutFrontEnd(
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
    checkout_payment_selected_js = checkout_payment_selected
    checkout_payment_button_js = checkout_payment_button

    agent_ids = ['Checkout']
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

from AgentsWorkFlow.Saas.Code.FrontEnd.NavigationJS.Integration import CodeNavigationJSFrontEnd

class FrontEndData(BaseModel):
    FrontEndContent: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: FrontEndData):
    print(f"CodeCheckoutFrontEnd: {input_data.FrontEndContent}")

              
def CodeCheckoutFrontEnd(
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
    checkout_payment_selected_js = checkout_payment_selected
    checkout_payment_button_js = checkout_payment_button

    session_id_CodeNavigationJSFrontEnd = "teste_handoff_CodeNavigationJSFrontEnd"
    agent_, handoff_obj_CodeNavigationJSFrontEnd = CodeNavigationJSFrontEnd(
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
                    )
# ---
# ## 🧰 Ferramentas Disponíveis

# Quando gerar os arquivos esperados, você tem acesso às ferramentas `autosave`, que **devem ser usadas obrigatoriamente** para o salvamento do arquivo criado (se houver mais de um arquivo use a ferramenta uma vez para cada arquivo)
# ### 📥 autosave
# - **path:** localizacao esperada do arquivo
# - **code:** conteúdo completo gerado


# ### 📥 `autoupload`  
#   - repo_name: nome do projeto armazenado no historico de conversas
#   - repo_owner: {repo_owner}  
#   - softwarepypath: {path_html}/checkout.html e {path_js}/checkout-payment-button.js (no caso de 2 arquivos utilize a ferramenta 1 vez para cada arquivo)
#   - token: {githubtoken}

    agent_ids = ['Checkout']
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
        handoffs=[handoff_obj_CodeNavigationJSFrontEnd],
    )


    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=FrontEndData,
    )
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
    return agent, handoff_obj