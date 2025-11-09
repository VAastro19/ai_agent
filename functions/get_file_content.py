# python
import os

MAX_CHARS = 10000

def get_file_content(working_directory, filepath):
    try:
        wd = os.path.abspath(working_directory)
        target = os.path.join(wd, filepath)
        if not target.startswith(wd + os.sep):
            return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'

        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{filepath}"'

        with open(target, "r", encoding="utf-8") as f:
            data = f.read(MAX_CHARS + 1)
            if len(data) > MAX_CHARS:
                data = data[:-1] + f'[...File "{filepath}" truncated at 10000 characters]'
        return data
    except Exception as e:
        return f"Error: {e}"