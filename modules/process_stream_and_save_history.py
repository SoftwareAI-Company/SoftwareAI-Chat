<<<<<<< HEAD



from softwareai_engine_library.Chat.stream.process_stream import process_stream


async def process_stream_and_save_history(
                            type_stream,
                            agent_,
                            message,
                            WEBHOOK_URL,
                            session_id,
                            user_email,
                            number,
                            appcompany
                            
                            
                            ):
    await process_stream(type_stream, 
                        agent_, 
                        message, 
                        WEBHOOK_URL,
                        session_id,
                        user_email,
                        appcompany
                                        
                    )
    print(f"🤖Sistema {number}")
    return {"sucess": "True"}
=======



from softwareai_engine_library.Chat.stream.process_stream import process_stream


async def process_stream_and_save_history(
                            type_stream,
                            agent_,
                            message,
                            WEBHOOK_URL,
                            session_id,
                            user_email,
                            number,
                            appcompany
                            
                            
                            ):
    await process_stream(type_stream, 
                        agent_, 
                        message, 
                        WEBHOOK_URL,
                        session_id,
                        user_email,
                        appcompany
                                        
                    )
    print(f"🤖Sistema {number}")
    return {"sucess": "True"}
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
        