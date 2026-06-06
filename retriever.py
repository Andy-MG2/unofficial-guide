import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL, N_RESULTS

#Create Chroma Collection
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function = ef,
    metadata={"hnsw:space": "cosine"},
)


def get_collection():
    '''Returns ChromaDB collection'''
    return collection

def embed_and_store(chunks):
    '''
    Embeds a list of chunks and stores them in the vector db
    
    _collection.add() takes three parallel lists built from the chunks
    returned by chunk_document():
      - documents : raw text strings — ChromaDB's embedding function converts
                    these to vectors automatically using sentence-transformers
      - metadatas : one dict per chunk, stored alongside the vector so that
                    retrieve() can know which professor reviews came from
      - ids       : the unique chunk_id strings used to identify each entry

    ChromaDB handles embeddings manually here automatically
    
    '''
    collection.add(
        documents = [c["review"] for c in chunks],
        metadatas=[{"professor": c["professor"]} for c in chunks],
        ids = [c["chunk_id"] for c in chunks],
    )
    print(f"Stored {collection.count()} total chunks in the vector database.")

def retrieve(query, n_results=N_RESULTS):
    '''
    finds the most relevant chunks for the users query
    
    Return a list of dicts, each with:
        - "reviews": the review text
        - "professor" : the professor name (pull this from metadatas)
        - "distance" : the similarity score (lower = more similar for cosine)
    '''
    if collection.count() == 0:
        return[]
    
    results = collection.query(
        query_texts = [query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    #Really low thresholds returned no answers, even for simple qeustions directly in the rules.
    thresh = 0.9

    output = []
    for i in range(len(documents)):
        if distances[i] < thresh:  # lower = more similar, so filter HIGH distances
            output.append({
                "review": documents[i],
                "professor": metadatas[i]["professor"],  # metadatas[i] is a dict, need ["professor"
                "distance": distances[i],
            })

    return output


#Test
# from ingest import load_documents, chunk_document

# def test_retrieval():
#     # load and chunk
#     documents = load_documents()
#     all_chunks = []
#     for doc in documents:
#         chunks = chunk_document(doc["text"], doc["professor"])
#         all_chunks.extend(chunks)
#     print(f"Total chunks to embed: {len(all_chunks)}")

#     # embed only if collection is empty
#     collection = get_collection()
#     if collection.count() == 0:
#         print("Embedding chunks into ChromaDB...")
#         embed_and_store(all_chunks)
#     else:
#         print(f"Collection already has {collection.count()} chunks, skipping embed.")

#     # test 3 queries
#     test_queries = [
#         "Is Bryan Pfister a laid back professor?",
#         "What do students say about Amir Miri's BME 680 course?",
#         "Which BME professor is most recommended for not caring about students?",
#     ]

#     for query in test_queries:
#         print(f"\n{'='*60}")
#         print(f"QUERY: {query}")
#         print(f"{'='*60}")
#         results = retrieve(query)
#         if not results:
#             print("No results returned.")
#         for r in results:
#             print(f"\nProfessor : {r['professor']}")
#             print(f"Distance  : {r['distance']:.4f}")
#             print(f"Review    : {r['review'][:300]}")
#             print("-" * 40)

# if __name__ == "__main__":
#     test_retrieval()