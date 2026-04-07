### What is a Tool?

A tool is just a Python function (or API) that is packaged in a way the LLM can understand and call when needed.

LLMs (like GPT) are great at:

- Reasoning
- Language generation

But they can’t do things like:

- Access live data (weather, news)
- Do reliable math
- Call APIs
- Run code
- Interact with a database

---

### How Tools Fit into the Agent Ecosystem

An AI agent is an LLM-powered system that can autonomously think, decide, and take actions using external tools or APIs to achieve a goal.

- **LLM:** Reasoning & Decision Making
- **Tools:** Action

---

### Built-in Tools

A built-in tool is a tool that LangChain already provides for you — it’s pre-built, production-ready, and requires minimal or no setup. You don’t have to write the function logic yourself; you just import and use it.

| Tool Name            | Capability                    |
| -------------------- | ----------------------------- |
| DuckDuckGoSearch     | Run Web search via DuckDuckGo |
| WikipediaQuery       | Run Wikipedia summary         |
| PythonREPLTool       | Run raw Python code           |
| ShellTool            | Run shell commands            |
| RequestsGetTool      | Make HTTP GET requests        |
| GmailSendMessageTool | Send emails via Gmail         |
| SlackSendMessageTool | Post message to Slack         |
| SQLDatabaseQueryTool | Run SQL queries               |

### Custom Tools

A custom tool is a tool that you define yourself.

Use them when:

You want to call your own APIs.

You want to encapsulate business logic.

You want the LLM to interact with your database, product, or app.

### Custom Tools

A custom tool is a tool that you define yourself. Use them when you want to call your own APIs, encapsulate business logic, or interact with your specific database/app.

#### Ways to Create Custom Tools

1. **Using the `@tool` decorator**
   - Simplest way; requires a docstring and type hints.

2. **Using `StructuredTool.from_function`**
   - Provides more control over name, description, and schema.

3. **Subclassing `BaseTool`**
   - Most powerful; supports state management and complex logic.

### Structured Tool Definition:

A Structured Tool in LangChain is a special type of tool where the input to the tool follows a structured schema, typically defined using a Pydantic model.

### BaseTool Definition:

BaseTool is the abstract base class for all tools in LangChain.
It defines the core structure and interface that any tool must follow, whether it's a simple one-liner or a fully customized function.

All other tool types like @tool, StructuredTool are built on top of BaseTool

### Toolkits

A toolkit is just a collection (bundle) of related tools that serve a common purpose — packaged together for convenience and reusability.

In LangChain:

A toolkit might be: GoogleDriveToolKit

And it can contain the following tools:

GoogleDriveCreateFileTool: Upload a file

GoogleDriveSearchTool: Search for a file by name/content

GoogleDriveReadFileTool: Read contents of a file
