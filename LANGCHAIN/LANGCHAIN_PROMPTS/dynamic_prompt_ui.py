from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import load_prompt



load_dotenv()
 
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")
model = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.7
)


st.header('research tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = load_prompt('template.json')

# fill the placeholders
# prompt = template.invoke({'paper_input':paper_input, 'style_input':style_input, 'length_input':length_input})

# if st.button('Summarize'):
#     result = model.invoke(prompt)
#     st.write(result.content)
# prompt = template.invoke({'paper_input':paper_input, 'style_input':style_input, 'length_input':length_input})

# Lets wrote above two invokes with the help of chain so code looks more clean > i am comment out the above code of lines



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input' : paper_input,
        "style_input" : style_input,
        'length_input' : length_input
    })
    st.write(result.content)