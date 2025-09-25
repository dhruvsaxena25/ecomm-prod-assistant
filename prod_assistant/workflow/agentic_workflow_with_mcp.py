from typing import Annotated, Sequence, TypedDict, Literal
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from prompt_library.prompts import PROMPT_REGISTRY, PromptType
from retriever.retrieval import Retriever
from utils.model_loader import ModelLoader
from langgraph.checkpoint.memory import MemorySaver
import asyncio
from evaluation.ragas_eval import evaluate_context_precision, evaluate_response_relevancy
from langchain_mcp_adapters.client import MultiServerMCPClient



class AgenticRAG:
    """Agentic RAG pipeline using LangGraph."""
    
    class AgentState(TypedDict):
        messages: Annotated[Sequence[BaseMessage], add_messages]
        
    def __init__(self,):
        
        self.retriever_obj = Retriever()
        self.model_loader = ModelLoader()
        self.llm = self.model_loader.load_llm()
        self.checkpointer = MemorySaver()
        
        # MCP Client Init
        self.mcp_client = MultiServerMCPClient(
            {
                "product_retriever": {
                "command": "python",
                "args": ["prod_assistant/mcp_servers/product_search_server.py"],  # absolute path recommended
                "transport": "stdio"
                },  
            }
        )
        # Load MCP tools
        
        self.mcp_tools = ""
        
        
    