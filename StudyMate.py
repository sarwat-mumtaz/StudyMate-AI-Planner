#!/usr/bin/env python
# coding: utf-8

# # ==============================
# # 📚 StudyMate - Your AI Study Planner
# # ==============================
# 
# #  Imports

# In[41]:


import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
#Load API Key
openai.api_key  = os.getenv('OPENAI_API_KEY')


# In[45]:


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


# In[46]:


# ---- Define Study Planner Bot ----
context = [ {'role':'system', 'content':"""
You are StudyBot, an automated assistant to create personalized study plans.
You first greet the student, then ask about:
1) Subjects they want to study
2) Available study hours per day
3) Exam or goal deadline (if any)
4) Preferred study style (long sessions, short sessions, with breaks)
5) Any specific priorities (like weak topics)


You then generate a structured study plan with:
- Daily schedule (subjects & time slots)
- Break times
- Weekly summary
- Motivation tips


Keep the conversation short, friendly, and encouraging.
"""} ]


# In[47]:


# ---- Panel UI ----
pn.extension()


panels = [] # collect display


# In[49]:


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role':'assistant', 'content':f"{response}"})

    panels.append(pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(pn.Row('Assistant:', pn.pane.Markdown(response, width=600, 
                                                       style={'background-color': '#F6F6F6'})))

    return pn.Column(*panels)


# In[50]:


# Input + Button
inp = pn.widgets.TextInput(value="Hi", placeholder='Enter your study details here…')
button_conversation = pn.widgets.Button(name="Plan My Studies")


interactive_conversation = pn.bind(collect_messages, button_conversation)


# In[51]:


# Dashboard
dashboard = pn.Column(
inp,
pn.Row(button_conversation),
pn.panel(interactive_conversation, loading_indicator=True, height=300),
)


# Display dashboard
dashboard


# 

# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[ ]:




