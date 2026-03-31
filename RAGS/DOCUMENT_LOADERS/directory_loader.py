from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader


loader = DirectoryLoader(
    path= ".",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print((docs))
# print(docs[0].page_content)
# print(docs[1].metadata)