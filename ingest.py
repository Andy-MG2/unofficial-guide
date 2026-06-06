import os 
from config import DOCS_PATH
documents = []
def load_documents():
    '''
    Load txt rate my professor files from rmp_data folder
    Returns list of document files
    '''
    
    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            professor_name = filename.replace(".txt", "").replace("_rmp", "").replace("_", " ").title()
            documents.append({
                "professor": professor_name,
                "filename": filename,
                "text": text,
            })
    print(f"Loaded {len(documents)} RMP professor documents: {[d['professor'] for d in documents]}")
    return documents


def chunk_document(text, professor_name):
    '''
    Splits document into chunks for embedding 

    Strategy:
        - Split into reviews themselves into chunks 
        - min size of 100 char
    Returns list of dictionaries with:
        - "review": the chunk of review
        - "professor": the name of the professor
        - "chunk_id": unique identifier, ex: "miriamir_0, miriamir_1"
        
    '''
    min_len = 100

    chunks = []
    counter = 0

    reviews = text.split("\n---\n")
    for review in reviews:
        review = review.strip()
        if review:
            chunks.append({
                "review": review,
                "professor": professor_name,
                "chunk_id": f"{professor_name}_{counter}",
            })
        counter+=1
    return chunks


#Test

# total_chunks = 0
# for i in range(len(documents)):
#     chunks = chunk_document(documents[i]["text"], documents[i]["professor"] )
#     print(chunks)
#     print()
#     for chunk in chunks:
#         total_chunks+=1

# print(f"\nTotal_CHUNKS: {total_chunks}")


