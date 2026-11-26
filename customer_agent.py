import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
import db_service

# Load environment configuration
load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")


# Define Tools with mandatory Docstrings
@tool
def get_order_status(order_id: str):
    """Get the current status of an e-commerce order based on the given order ID."""
    return db_service.get_order_status(order_id)

@tool
def cancel_order(order_id: str):
    """Cancel an e-commerce order based on the given order ID."""
    return db_service.cancel_order(order_id)

# Tool Registry Setup
tools = {
    get_order_status.name: get_order_status,
    cancel_order.name: cancel_order
}

# Initialize OpenAI LLM & Bind Tools
llm = ChatOpenAI(model="nvidia/nemotron-3-ultra-550b-a55b:free", api_key=api_key , base_url="https://openrouter.ai/api/v1")
llm_with_tools = llm.bind_tools(list(tools.values()))

def customer_support(question: str):
    """
    Two-Step Agentic AI Workflow:
    Step 1: First LLM call performs tool selection based on user question and docstrings.
    Step 2: Backend executes the tool(s) and sends results back to LLM for final natural language generation.
    """
    # 1st LLM Invocation: Tool selection
    response = llm_with_tools.invoke(question)
    
    # If no tool execution is required, return standard response directly
    if not response.tool_calls:
        return response.content
    
    # Execute selected tool(s)
    tool_results = []
    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        
        selected_tool = tools.get(tool_name)
        if selected_tool:
            # Run tool operation against MySQL database
            result = selected_tool.invoke(tool_args)
            tool_results.append({
                "tool_name": tool_name,
                "result": result
            })
    
    # 2nd LLM Invocation: Generate final natural language response based on tool results
    final_prompt = f"""
    Customer Question: {question}
    Tool Results: {tool_results}
    
    Instructions:
    Provide a clear, helpful response to the customer based strictly on the tool execution results.
    """
    
    final_response = llm.invoke(final_prompt)
    return final_response.content
