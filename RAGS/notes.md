RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses.

Benefits of using RAG

Use of up-to-date information

Better privacy

No limit of document size

Rag based applications have 4 important components

(1) Document Loaders
(2) Text Splitters
(3) Vector Databases
(4) Retrievers

There are four kind of document loaders
(1) TextLoader
(2) PyPDFLoader
(3) WebBasedLoader
(4) CSVLoader

Document Loaders
Definition: Components in LangChain used to load data from various sources into a standardized format (usually as Document objects).

Purpose: Once loaded, these objects can be used for chunking, embedding, retrieval, and generation.

Example Structure:

Document(
page_content="The actual text content",
metadata={"source": "filename.pdf", ...}
)

TextLoader
Definition: A simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document objects.

Use Case: Ideal for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a LangChain pipeline.

Limitation: Works only with .txt files.

PyPDFLoader
PyPDFLoader is a document loader in LangChain used to load content from PDF files and convert each page into a Document object.

Example Output:

[
Document(page_content="Text from page 1", metadata={"page": 0, "source": "file.pdf"}),
Document(page_content="Text from page 2", metadata={"page": 1, "source": "file.pdf"}),
...
]
