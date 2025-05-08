from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel

from modules.modules import *
from modules.Egetoolsv2 import *
from modules.EgetMetadataAgent import *


from AgentsWorkFlow.Saas.Code.BackEnd.webhook.Integration import CodeFlaskBackEndSprint10Agent


class FrontEndData(BaseModel):
    FrontEndContent: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: FrontEndData):
    print(f"CodeFlaskBackEndapi_create_checkoutAgent: {input_data.FrontEndContent}")
    # response = requests.post("http://localhost:5000/agent/refund", json={"input": input_data.reason})
    # reply = response.json().get("reply")
              
def CodeFlaskBackEndapi_create_checkoutAgent(                                
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


    session_id_CodeFlaskBackEndSprint10Agent = "teste_handoff_CodeFlaskBackEndSprint10Agent"
    agent_, handoff_obj_CodeFlaskBackEndSprint10Agent = CodeFlaskBackEndSprint10Agent(                                
                                session_id, 
                                appcompany,
                                path_ProjectWeb,
                                path_html,
                                path_js,
                                path_css,
                                doc_md,
                                Keys_path,

                      )

   
    createcheckout = '''
```python
@app.route('/api/create-checkout', methods=['POST'])
@limiter.limit("10 per minute")
def create_checkout():
    data = request.get_json()
    try:
        # Calcula a data de expiração: data atual + 31 dias
        expiration_time = datetime.now() + timedelta(days=31)

        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                "price": SUBSCRIPTION_PRICE_ID,  # Usando o ID do preço definido no .env
                "quantity": 1
            }],
            mode="subscription",  # Modo de assinatura
            payment_method_types=["card"],
            success_url=f"{API_BASE_URL}/checkout/sucess",  
            cancel_url=f"{API_BASE_URL}/checkout/cancel",  
            metadata={
                "email": data.get("email"),
                "password": data.get("password"),
                "SUBSCRIPTION_PLAN": "premium",
                "TIMESTAMP": expiration_time.isoformat()
            },
        )
        logger.info("Sessão criada: %s", checkout_session.id)
        return jsonify({"sessionId": checkout_session.id})
    except Exception as e:
        logger.info("Erro ao criar a sessão de checkout: %s", str(e))
        return jsonify({"error": str(e)}), 500
```

    '''

    agent_ids = ['api_login']
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
        handoffs=[handoff_obj_CodeFlaskBackEndSprint10Agent],
    )




    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=FrontEndData,
    )
    return agent, handoff_obj