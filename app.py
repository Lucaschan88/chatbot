## if coding is VS code .py
## below code should be in one python program2.py (flask program)

from flask import Flask, request, Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
import asyncio

## for those who are using vscode/pycharm
### from pythonbotprogram import bot
from startbot import bot
### end.........

#app = Flask(__name__)
app = web.Application(middlewares=[aiohttp_error_middleware])
loop = asyncio.get_event_loop()

botadaptersettings = BotFrameworkAdapterSettings("bc04e3a3-3d14-4e9b-9f4a-a94c11eadbf5","32b914a3-62e2-49b1-9583-ac801c16b768")
botadapter = BotFrameworkAdapter(botadaptersettings)

### calling the class create above
ebot = bot()

## route for the bot 
# @app.route("/api/messages",methods=["POST"])
@app.router.add_post("/api/messages", messages)

def messages():
    if "application/json" in request.headers["content-type"]:
        jsonmessage = request.json
    else:
        return Response(status=415)
    
    activity = Activity().deserialize(jsonmessage)
 
    async def turn_call(turn_context):
        await ebot.on_turn(turn_context)
 
    task = loop.create_task(botadapter.process_activity(activity,"",turn_call))
    loop.run_until_complete(task)
 

#if __name__ == '__main__':
#    app.run('localhost',3978)

if __name__ == "__main__":
    try:
        web.run_app(APP, host="localhost", port=CONFIG.PORT)

    except 
        Exception as error:
            raise error





    
    
