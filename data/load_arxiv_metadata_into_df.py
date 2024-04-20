import csv
import json
import gzip
from dotenv import load_dotenv
import os
from utils.custom_logger import setup_logger

logger = setup_logger(__name__)

load_dotenv()
DATA_DIR = os.environ.get("DATA_DIR")


def load_metadata(fname):
    with gzip.open(fname, "rt", encoding="utf-8") as fin:
        for line in fin:
            yield json.loads(line)


keys = [
    "id",
    "submitter",
    "authors",
    "title",
    "comments",
    "journal-ref",
    "doi",
    "abstract",
    "report-no",
]
fname = os.path.join(DATA_DIR, "arxiv-data", "arxiv-metadata-oai-2024-04-19.json.gz")
fname_to_save = os.path.join(
    DATA_DIR, "arxiv-data", "arxiv-metadata-oai-2024-04-19.csv"
)
with open(fname_to_save, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(keys)

    for idx, json_object in enumerate(load_metadata(fname)):
        writer.writerow([json_object.get(key, "") for key in keys])
        if idx % 1000 == 0:
            logger.info(f"Written {idx+1} entries to arxiv-metadata-oai-2024-04-19.csv")
