from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel

from modules.modules import *



from AgentsWorkFlow.Saas.Code.BackEnd.api_login.Integration import CodeFlaskBackEndSprint8Agent

class FrontEndData(BaseModel):
    FrontEndContent: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: FrontEndData):
    print(f"CodeFlaskBackEndSprint7Agent: {input_data.FrontEndContent}")
    # response = requests.post("http://localhost:5000/agent/refund", json={"input": input_data.reason})
    # reply = response.json().get("reply")
              
def CodeFlaskBackEndSprint7Agent(                                
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

    session_id_CodeFlaskBackEndSprint8Agent = "teste_handoff_CodeFlaskBackEndSprint8Agent"
    agent_, handoff_obj_CodeFlaskBackEndSprint8Agent = CodeFlaskBackEndSprint8Agent(                                
                                session_id, 
                                appcompany,
                                path_ProjectWeb,
                                path_html,
                                path_js,
                                path_css,
                                doc_md,
                                Keys_path,

                      )

   
    api_register = '''
```python
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    SUBSCRIPTION_PLAN = data.get("SUBSCRIPTION_PLAN")
    expiration = data.get("expiration")
    WEBHOOK_SECRET_flag = data.get("WEBHOOK_SECRET_flag")
    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400
    if not SUBSCRIPTION_PLAN:
        SUBSCRIPTION_PLAN = "free"
    if not expiration:
        expiration = "None"
    if SUBSCRIPTION_PLAN == "free":
        limit = "2 per day"
    elif SUBSCRIPTION_PLAN == "premium":
        limit = "50 per day"

    email_safe = email.replace('.', '_')
    ref = db.reference(f'users/{email_safe}', app=appcompany)
    if ref.get():
        if not WEBHOOK_SECRET_flag:
            return jsonify({"error": "Voce ja tem uma conta"}), 400
        
        if WEBHOOK_SECRET_flag == WEBHOOK_SECRET:
                
            api_key = generate_api_key(SUBSCRIPTION_PLAN)

            ref.update({
                "api_key": api_key
            })
            ref.update({
                "SUBSCRIPTION_PLAN": SUBSCRIPTION_PLAN
            })
            ref.update({
                "limit": limit
            })
            ref.update({
                "expiration": expiration
            })

            return jsonify({"message": "Upgrade realizado",
                            "email": email,
                            "password": password,
                            "SUBSCRIPTION_PLAN": SUBSCRIPTION_PLAN,
                            "limit": limit,
                            "expiration": expiration,
                            "api_key": api_key,
                        }), 409
            
    api_key = generate_api_key(SUBSCRIPTION_PLAN)

    ref.set({
        "email": email,
        "password": password,
        "SUBSCRIPTION_PLAN": SUBSCRIPTION_PLAN,
        "limit": limit,
        "expiration": expiration,
        "api_key": api_key,
        "stripe_account_id": "None",
        'created_at': datetime.now().isoformat()
        
    })
    return jsonify({
        "message": "Usuário registrado com sucesso",
        "email": email,
        "password": password,
        "SUBSCRIPTION_PLAN": SUBSCRIPTION_PLAN,
        "limit": limit,
        "expiration": expiration,
        "api_key": api_key,
        "stripe_account_id": "None",
        'created_at': datetime.now().isoformat()
        
        }), 200
```


    '''
   

    agent_ids = ['api_register']
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
        handoffs=[handoff_obj_CodeFlaskBackEndSprint8Agent],
    )



    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=FrontEndData,
    )
    return agent, handoff_obj