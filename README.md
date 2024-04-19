# Chat ArXiv - Backend

This repository contains the backed functionality of the Chat ArXiv Bot interface.

Chat ArXiv is an attempt to create a chat bot using a Retrieval Augmented Generation (RAG) model to interact with the ArXiv Preprint Server.

This is an ongoing development and we expect it to significantly change over time.

## TO DO:

1. Setup Development Environment:
[x] Install dependencies like llama-index, FastAPI, uvicorn, pytest etc.
[x] Set up a basic project structure - `app/`, `tests/`, `models/`, `schemas/`, `database/`.
2. Data Ingestion and Creation of Vector Database:
[] Set up a local instance of Weaviate in Docker to begin development.
[] Download the latest dump of arXiv metadata (title, authors, year, abstract). Currently, we will not use the papers.
[] Evaluate and identify a suitable text embbedding model than can be locally used with llama index.
[] Create chunks from the arXiv metadata, create the embeddings of these chunks and insert them into the vector database.
3. Create API endpoints
[] GET /search: Endpoint to query the vector database.
[] GET /document/{id}: To query the ArXiv API to fetch a particular paper.
[] POST /feedback: To collect user feedback on anything in the product.
[] GET /stats: To provide statistical data on the usage of the API, common queries, user engagement etc. Evaluate monitoring tools like Prometheus and visualization tools like Grafana for this purpose.
[] POST /update-index: To trigger updates to the vector database to add new documents or update existing ones.
[] GET /suggest/{query}: To provide autocomplete suggestions or similar queries as the user types.
4. API Endpoint Documentation:
[] Evaluate Swagger UI.
5. Incorporate API Rate Limiting
[] Choose a rate limiting strategy - Fixed Window, Sliding Window Log, or Token Bucket.
[] Integrate SlowAPI with FastAPI for rate limiting.
[] Define rate limits for each of the endpoints
6. Testing
[] Unit Tests
[] Integration Tests
[] Functional Tests
[] Security Tests