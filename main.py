import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) > 1:
        flags = []
        for arg in sys.argv:
            if arg.startswith("--"): flags.append(arg)
            elif arg != sys.argv[0]: prompt = arg
        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
        response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    else:
        print("Error: prompt not provided!")
        sys.exit(1)

    if "--verbose" in flags:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)

if __name__ == "__main__":
    main()
