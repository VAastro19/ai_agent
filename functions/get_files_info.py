# python
import os

def get_files_info(working_directory, directory="."):
    try:
        wd = os.path.abspath(working_directory)
        target = os.path.join(wd, directory)
        if not target.startswith(wd + os.sep) and target != wd:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target):
            return f'Error: "{directory}" is not a directory'

        entries = []
        for name in os.listdir(target):
            path = os.path.join(target, name)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            entries.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(entries)
    except Exception as e:
        return f"Error: {e}"