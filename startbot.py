#!/usr/bin/env python
# coding: utf-8

# In[21]:


## if coding is VS Code .py
## below code should be in one pythonbotprogram.py(bot program)
# 1. Create a class for the bot
# 2. Create function to send all the activity
# echo bot
## when user type hi, the response will also be hi


from botbuilder.core import TurnContext

class bot:
    async def on_turn(self, turn_context:TurnContext):
        await turn_context.send_activity(turn_context.activity.text)
        
