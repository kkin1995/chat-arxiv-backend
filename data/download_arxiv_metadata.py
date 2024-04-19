from arxiv_public_data.oai_metadata import all_of_arxiv
from dotenv import load_dotenv
import os

load_dotenv()
DATA_DIR = os.environ.get("DATA_DIR")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

all_of_arxiv()
