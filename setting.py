
#Reads the key-value pair from .env file and adds them to environment variable
# .env file must be listed on .gitignore

from dotenv import load_dotenv
load_dotenv()

load_dotenv(verbose=True)

# # OR, explicitly providing path to '.env'
# from pathlib import Path  # Python 3.6+ only
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)
