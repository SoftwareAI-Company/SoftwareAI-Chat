from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel

from modules.modules import *


class inputdata(BaseModel):
  input_data_Content: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: inputdata):
    print(f"CodeUploadGit: {input_data.input_data_Content}")
    # response = requests.post("http://localhost:5000/agent/refund", json={"input": input_data.reason})
    # reply = response.json().get("reply")
              
def CodeUploadGit(session_id, appcompany,
                        path_ProjectWeb,
                        path_html,
                        path_js,
                        path_css,
                        doc_md,
                        Keys_path,
                        githubtoken,
                        repo_owner,

                    ):

# ### 📥 `autoupload`  
#   - repo_name: nome do projeto armazenado no historico de conversas
#   - repo_owner: {repo_owner}  
#   - softwarepypath: {path_html}/checkout.html e {path_js}/checkout-payment-button.js (no caso de 2 arquivos utilize a ferramenta 1 vez para cada arquivo)
#   - token: {githubtoken}

# ###📦 autogetlocalfilecontent  
# Para obter o conteúdo **completo** do arquivo index para que seja possivel o desenvolvimento das modificacoes
# autogetlocalfilecontent:
# - preferred_name: "index.html"
# - fallback_names: ["index.html"]
# - search_dir: {path_html}

# ### 📦 autocreaterepo
# Para Criar o Repositorio do projeto no git
# autocreaterepo:
# - **description:** Máximo 250 caracteres (resumo do projeto)
# - **githubtoken:** {githubtoken}
# - **private:** false
# - **repo_name:** nome do projeto slugificado
# - **repo_owner:** {repo_owner}

# ###📦 autolistlocalproject  
# Para obter os caminhos dos arquivos e seus conteudos do projeto local (no nosso caso precisamos apenas dos caminhos para usar em autoupload)
# autolistlocalproject:
# - path_project: {path_ProjectWeb}

# ### 📦 autoupload
# - **repo_name:** nome do projeto 
# - **repo_owner:** {repo_owner}
# - **softwarepypath:** a lista de caminhos dos arquivos a ser enviado
# - **token:** {githubtoken}



    agent_ids = ['Git']
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
        # handoffs=[handoff_obj_CodeUploadGit],
    )


    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=inputdata,
    )
    return agent, handoff_obj