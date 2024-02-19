from langchain.text_splitter import RecursiveCharacterTextSplitter
def chunk_texts(combined_lists, chunk_size, chunk_overlap, min_chunk, extra_filter):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                   chunk_overlap=chunk_overlap,
                                                   length_function=len)

    chunked_docs = []
    for text in combined_lists:
        if len(text) > min_chunk:
            chunked_texts = text_splitter.split_text(text)
            for chunk in chunked_texts:
                chunked_docs.append(chunk)

    filtered_docs = []
    for i in chunked_docs:
      if len(i) > extra_filter:
        filtered_docs.append(i)
    return chunked_docs
