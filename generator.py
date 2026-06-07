from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)

def generate_response(query, retrieved_chunks):
    if not retrieved_chunks:
        return {
            "answer": "I don't have enough information in the reviews to answer that question.",
            "sources": []
        }

    context = "\n\n".join(
        f"[Review from {chunk['professor']}]:\n{chunk['review']}"
        for chunk in retrieved_chunks
    )

    sources = list(set(chunk["professor"] for chunk in retrieved_chunks))

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            temperature=0.0,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an assistant that helps NJIT students choose BME professors. "
                        "Answer the user's question using ONLY the student reviews provided below. "
                        "Do not use any outside knowledge or make assumptions beyond what the reviews say. "
                        "Always cite which professor the information comes from. "
                        "If the reviews do not contain enough information to answer the question, "
                        "say exactly: 'I don't have enough information in the reviews to answer that.'"
                    )
                },
                {
                    "role": "user",
                    "content": f"Question: {query}\n\nStudent Reviews:\n{context}"
                }
            ]
        )
        return {
            "answer": response.choices[0].message.content,
            "sources": sources,
            "chunks": retrieved_chunks,
        }
    except Exception as e:
        return {
            "answer": f"Error calling LLM: {str(e)}",
            "sources": sources,
            "chunks": retrieved_chunks
        }