import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# folder = '1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL'


# # Download files
# file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
# for index, file in enumerate(file_list):
# 	print(index+1, 'file downloaded : ', file['title'])
# 	file.GetContentFile(file['title'])




# def get_file_list(folder_id):
#     gauth = GoogleAuth()
#     drive = GoogleDrive(gauth)

#     # Download files
#     file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
#     return file_list
	


from llama_index.readers.google import GoogleDriveReader
# from llama_index.readers.google import GoogleDriveReader

# loader = GoogleDriveReader()
# def load_data(folder_id: str):
# 	docs = loader.load_data(folder_id=folder_id)
# 	# for doc in docs:
# 	# 	doc.id_ = doc.metadata["file_name"]
# 		# doc.id_ = doc.metadata["bharat_text"]
# 	return docs


# docs = load_data(folder_id="1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL")
# print(docs)











from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    download_loader,
    RAKEKeywordTableIndex,
)

from llama_index.llms.openai import OpenAI

import openai

# import os
# from dotenv import load_dotenv

# load_dotenv()  # Load the .env file

# openai.api_key = os.getenv('OPENAI_API_KEY') 
# OPENAI_API_KEY="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"

# openai.api_key = "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"
os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(temperature=0, model="gpt-3.5-turbo")

# reader = SimpleDirectoryReader(input_files=["data/bharat_text.pdf"])


# data = reader.load_data()


# index = VectorStoreIndex.from_documents(docs)

# query_engine = index.as_query_engine(streaming=True, similarity_top_k=3)

# response = query_engine.query(
#     "What is Section 138?"
#     " page reference after each statement."
# )

# response.print_response_stream()

# for node in response.source_nodes:
#     print("-----")
#     text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
#     print(f"Text:\t {text_fmt} ...")
#     print(f"Metadata:\t {node.node.metadata}")
#     print(f"Score:\t {node.score:.3f}")
    










import streamlit as st
# from llama_index import VectorStoreIndex, ServiceContext, Document
# from llama_index.llms import OpenAI
from llama_index.llms.openai import OpenAI
import openai
# from llama_index import SimpleDirectoryReader

st.set_page_config(page_title="Intelligent Document Finder with Llama Index", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
# openai.api_key = st.secrets.openai_key
st.title("Chat with the your documents, powered by LlamaIndex 💬🦙")

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about your documents's content!"},
    ]





# loader = GoogleDriveReader()
# def load_data(folder_id: str):
# 	docs = loader.load_data(folder_id=folder_id)
# 	# for doc in docs:
# 	# 	doc.id_ = doc.metadata["file_name"]
# 		# doc.id_ = doc.metadata["bharat_text"]
# 	return docs



loader = GoogleDriveReader()
@st.cache_resource(show_spinner=False)
def load_data(folder_id: str):
    with st.spinner(text="Loading and indexing your docs – hang tight! This should take 1-2 minutes."):
        # reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = loader.load_data(folder_id=folder_id)
        # docs = reader.load_data()
        # service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on query handling and your job is to answer questions. Assume that all questions are related to loaded documents. Keep your answers perfect and based on facts – do not hallucinate features."))
        # index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        # return index
    return docs

docs = load_data(folder_id="1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL")

# index = load_data()
index = VectorStoreIndex.from_documents(docs)

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
