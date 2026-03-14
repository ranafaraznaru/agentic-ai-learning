Some LLms can return the strcutured output but open source some are not that well trained and fine tuned so to work with them
we have to use output pasers

Output Parsers in LangChain help convert raw LLM responses into structured formats like JSON, CSV, Pydantic models, and more. They ensure consistency, validation, and ease of use in applications.

There are widely used 4 types of output parsers:
(1) StrOutputParser
(2) Json output parsers
(3) Structured output parsers
(4) Pydantic output parsers

There are other output parsers are also available with langchain but we will use above mentioned output parsers.

## StrOutputParser

The StrOutputParser is the simplest output parser in LangChain. It is used to parse the output of a Language Model (LLM) and return it as a plain string.

## Structured output parsers

StructuredOutputParser is an output parser in LangChain that helps extract structured JSON data from LLM responses based on predefined field schemas.

It works by defining a list of fields (ResponseSchema) that the model should return, ensuring the output follows a structured format.
