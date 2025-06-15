from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from qdrant_client import QdrantClient

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
qdrant_client = QdrantClient(path="./qdrant_data")

vectorstore = Qdrant(
    client=qdrant_client,
    collection_name="ml_course",
    embeddings=embedding_model,
)

retriever = vectorstore.as_retriever()
llm = Ollama(model="llama3")
rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def explain_misunderstood_concepts(misunderstood: list[tuple[str, dict]]) -> dict:
    explanations = {}
    for concept, question in misunderstood:
        prompt = (
            f"Explain the concept of '{concept}' in machine learning using real-world examples and illustrations. "
            f"Also, explain the following quiz question:\n\n"
            f"Question: {question['question']}\n"
            f"Options: {', '.join(question['options'])}\n"
            f"Clarify what the question means and implies. Then provide the correct answer "
            f"('{question['answer']}') and explain why it is correct."
        )
        result = rag_chain.invoke(prompt)
        key = f"{concept}|||{question['question']}"
        explanations[key] = result
    return explanations

