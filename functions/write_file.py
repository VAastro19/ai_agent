import os
from google.genai import types

def write_file(working_directory, filepath, content):
    try:
        wd = os.path.abspath(working_directory)
        target = os.path.join(wd, filepath)
        if not target.startswith(wd + os.sep):
            return f'Error: Cannot write "{filepath}" as it is outside the permitted working directory'

        parent = os.path.dirname(target)
        os.makedirs(parent, exist_ok=True)

        with open(target, "w") as f:
            f.write(content)

        return f"Successfully wrote to \"{filepath}\" ({len(content)} characters written)"

    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write data to the specified file, overwriting existing files and creating new ones in case none exist",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to write. Create if it does not exist",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Data to write into the file",
            ),
        },
    ),
)

