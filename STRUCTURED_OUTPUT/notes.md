# Structured output means gettings response in json instead of free text

# There are two ways one is llms have that and langchain helps to structure the output

# it calls with_structured_output second is output parsers its basically for the llms dont have structured output

"""
There are types of data formats in with_structured_output
(1) Type dictionary
TypedDict is a way to define a dictionary in Python where you specify what keys and values
should exist. It helps ensure that your dictionary follows a specific structure.

Why use TypedDict?

- It tells Python what keys are required and what types of values they should have.
- It does not validate data at runtime (it just helps with type hints for better coding).

-> simple TypedDict
-> Annotated TypedDict
-> Literal
-> More complex -> with pros and cons

(2) Pydantic
(3) Json schema
"""
