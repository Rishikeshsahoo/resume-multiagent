"""
Test script for the planner agent
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add parent directories to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.agents.planner_agent.planner_agent import planner_agent

def test_planner_agent():
    """Test the planner agent with a PDF file"""
    print("\n" + "="*60)
    print("TESTING PLANNER AGENT")
    print("="*60)
    
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("\nERROR: GOOGLE_API_KEY not found in environment variables")
        print("Please set your GOOGLE_API_KEY in .env file")
        return False
    
    try:
        # Initialize the agent
        print("\n[1] Initializing planner agent...")
        agent = planner_agent()
        print("SUCCESS: Agent initialized successfully")
        print(f"Agent type: {type(agent)}")
        
        # Test PDF file path (relative to project root)
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        pdf_path = os.path.join(project_root, "Resume.pdf")
        
        if not os.path.exists(pdf_path):
            print(f"\nERROR: PDF file not found at {pdf_path}")
            return False
        
        print(f"\n[2] Testing with PDF: {os.path.basename(pdf_path)}")
        
        # Invoke the agent
        print("\n[3] Invoking agent to extract text from PDF...")
        result = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"Please read the PDF file at '{pdf_path}' and extract all the text from it."
                }
            ]
        })
        
        print("\n" + "="*60)
        print("AGENT RESPONSE")
        print("="*60)
        
        # Print the result
        if result and "messages" in result:
            for message in result["messages"]:
                if hasattr(message, 'content'):
                    print(f"\n{message.content}")
                else:
                    print(f"\n{message}")
        else:
            print(result)
        
        print("\n" + "="*60)
        print("SUCCESS: Test completed!")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_planner_agent()
    exit(0 if success else 1)
