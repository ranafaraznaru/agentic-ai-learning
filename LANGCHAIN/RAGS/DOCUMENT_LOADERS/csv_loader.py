from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path= 'temperature.csv')

data = loader.load()

print(len(data))
print(data[1])
