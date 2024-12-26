from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

# Replace with your actual API key
groq_api_key = "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"

# Initialize the ChatGroq model
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)
parser = StrOutputParser()

# Define the system prompt template
system_template = "Translate the following into {language}: "
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Build the LangChain chain
chain = prompt_template | model | parser

# Create the FastAPI app
app = FastAPI(
    title="Langchain Server",
    description="Simple Langchain server using Langchain runnable interfaces",
    version="1.0.0"
)

# Add the chain as a route to the FastAPI app
add_routes(
    app,
    chain,
    path="/chain"
)

# Main entry point for running the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
