import os
from dotenv import load_dotenv

base_dir = os.path.dirname(__file__)
env_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path=env_path)

MANAGEMENT_SERVER = os.getenv("MANAGEMENT_SERVER")
SERVER1 = os.getenv("SERVER1")
SERVER2 = os.getenv("SERVER2")
