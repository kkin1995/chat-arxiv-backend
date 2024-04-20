from arxiv_public_data.oai_metadata import load_metadata
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
DATA_DIR = os.environ.get("DATA_DIR")

arxiv_data = load_metadata(
    os.path.join(DATA_DIR, "arxiv-data", "arxiv-metadata-oai-2024-04-19.json.gz")
)
df = pd.DataFrame(arxiv_data)

df.to_csv(os.path.join(DATA_DIR, "arxiv-data", "arxiv-metadata-oai-2024-04-19.csv"))
