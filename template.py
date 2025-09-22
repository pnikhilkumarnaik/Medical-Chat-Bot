import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s ]: %(message)s')
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/promte.py",
    ".env",
    "setup.py",
    "research/MadicalChatBot.ipynb",
    "store_index.py"
    "app.py",
    "static",
    "templates/chat.html",

]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}") 