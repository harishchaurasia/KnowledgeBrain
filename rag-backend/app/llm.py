# app/llm.py

#subprocess is used to run the LLM model as we invoke ithe model via the CLI. It allows us to interact with the model as if it were a process.
import subprocess
from app.query import retrieve_relevant_chunks


def build_prompt(question: str, chunks: list[dict]) -> str:
        """
    Builds a grounded prompt including:
    - retrieved context chunks
    - citation numbers
    - question
    - strict grounding instructions
    """

    contextBlock = ""

    for idx, item in enumerate(chunks):
        chunk_text = item["text"]
        source = item["metadata"]["source"]
        context_block += f"[{idx+1}] (Source: {source})\n{chunk_text}\n\n"


    prompt = f"""
        You are a helpful assistant. Use ONLY the context below to answer the question.

        If the answer is not completely contained in the provided context, say:
        "I don't know based on the provided documents."

        Context:
        {context_block}

        Question:
        {question}

        Answer (include citation numbers like [1], [2]):
    """
    
    return prompt



def call_llm(prompt: str) -> str:
    """
    Calls the LLM with the given prompt and returns the response.
    """

    ## subprocess runs: echo prompt | ollama run model
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        capture_output=True
    )

    # return result.stdout.decode("utf-8").strip()
    return result.stdout.decode("utf-8")


def answer_question(question: str, top_k:int=3) -> dict:
        """
    Full LLM answering pipeline:
    - retrieve relevant chunks
    - build RAG prompt
    - call LLM
    - return answer + sources
    """

    #Retrieving chunks
    chunks = retrieve_relevant_chunks(question, top_k)

    #Building grounded prompt
    prompt = build_prompt(question, chunks)

    #Getting LLM answer
    answer = call_llm(prompt)

    return {
        "answer": answer,
        "sources": chunks
    }
