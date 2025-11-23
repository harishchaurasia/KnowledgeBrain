# app/llm.py

#subprocess is used to run the LLM model as we invoke ithe model via the CLI. It allows us to interact with the model as if it were a process.
import subprocess


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

