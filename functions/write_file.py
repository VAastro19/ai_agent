import os

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



