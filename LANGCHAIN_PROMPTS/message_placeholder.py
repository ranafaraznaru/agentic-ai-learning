# A message place holder in langchain is a special placeholder used inside a chatprompttemplate to dynamically insert 
# chat history or a list of messages at runtime
# Simple words its history of user previous messages, so if user came in future we can load chat history from database

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

#chat template 
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}'),
])

chat_history = []
#load chat history 
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print (chat_history)
# create prompt
prompt = chat_template.invoke({'chat_history':chat_history,'query':'where is my refund?'})

print (prompt)