import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import get_files_info ,schema_get_files_info
from functions.call_function import call_function
def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read the content of a file
    - Write to a file (Create or update)
    - Run a python file with optional arguments

    When user asks about the code project - they are referring to the working directory . So you should start by looking at the project's files and figuring out 
    how to run the project and how to run the tests. You will always want to test the tests and the actual project to verify that behavior is working

    All paths you provide should be relative to the working directory. 
    You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    if len(sys.argv) <2 :
        print("A promt is needed ")
        sys.exit(1)

    verbose_flag = False 

    if len(sys.argv) == 3 and sys.argv[2] =="--verbose" :
        verbose_flag = True

    prompt = sys.argv[1]

    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]


    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
        )
    
    max_iterations = 200
    for i in range (0,max_iterations):
        response = client.models.generate_content(model="gemini-2.0-flash-001",contents=messages,config=config)

        if response is None or response.usage_metadata is None:
            print("Response is malformed")
            return 
        
        if verbose_flag:
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens:{response.usage_metadata.prompt_token_count}")
            print(f"Response tokens:{response.usage_metadata.candidates_token_count}")


        if response.candidates :
            for candidate in response.candidates :
                if candidate is None or candidate.content is None :
                    continue
                messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls :
                result = call_function(function_call_part,verbose_flag)
                messages.append(result)
                
        else:
            print(response.text)





main()


# print(get_files_info("calculator","pkg"))