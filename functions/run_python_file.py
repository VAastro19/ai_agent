# run_python_file.py
import os, subprocess
from google.genai import types

def run_python_file(working_directory, filepath, args=[]):
    try:
        wd = os.path.abspath(working_directory)
        target = os.path.join(wd, filepath)
        if not target.startswith(wd + os.sep):
            return f'Error: Cannot execute "{filepath}" as it is outside the permitted working directory'
        if not os.path.exists(target):
            return f'Error: File "{filepath}" not found.'
        if not target.endswith(".py"):
            return f'Error: "{filepath}" is not a Python file.'
        
        result = subprocess.run(["python3", filepath] + args, cwd=wd, text=True, timeout=30, capture_output=True)
        
        if result.stdout == "" and result.stderr == "":
            output = f"No output produced."
        else:
            output = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\n"
            if result.returncode != 0:
                output += f"Process exited with code {result.returncode}"

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs subprocess on a python file, and returns stdout, stderr, and returncode if it is different from 0.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to run.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Additional arguments provided for the python program, default=[]",
            ),
        },
    ),
)