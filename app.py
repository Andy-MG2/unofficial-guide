import streamlit as st
from ingest import load_documents, chunk_document
from retriever import embed_and_store, retrieve, get_collection
from generator import generate_response

st.set_page_config(page_title="NJIT BME Unofficial Guide", page_icon="🎓")
st.title("🎓 NJIT BME Unofficial Guide")
st.caption("Ask anything about BME professors at NJIT based on real student reviews.")

@st.cache_resource
def setup():
    documents = load_documents()
    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc["text"], doc["professor"])
        all_chunks.extend(chunks)
    collection = get_collection()
    if collection.count() == 0:
        embed_and_store(all_chunks)
    return True

setup()

query = st.text_input("Ask a question about a BME professor or course:")

if st.button("Ask") and query:
    with st.spinner("Searching reviews..."):
        chunks = retrieve(query)
        chunks = retrieve(query)
        result = generate_response(query, chunks)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Sources")
    if result["sources"]:
        for source in result["sources"]:
            st.write(f"• {source}")
    else:
        st.write("No sources retrieved.")