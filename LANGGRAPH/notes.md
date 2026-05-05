### What is Generative AI

Generative AI refers to a class of artificial intelligence models that can create new content - such as text, images, audio,
code or video that resembles human-created data.

LLM based apps like ChatGPT, diffusion models for images, code generations LLMs like CodeLLama,
TTS models like ElevenLabs, Video gen models like sora

### Generative AI Vs Traditional AI

Traditional AI is about finding patterns in data and giving predictions.

Generative AI is about learning the distribution of data so that it can generate a new sample from it.

### Gen AI Problems

# Reactive

It means it give ans to the asked questions. It dont know what to ans next.

# No Memory

# Generic Advice

it dont have company related information.

# Cant take actions

### Rag based problems

# Reactive

# No memory

# Specific advice resolved as it have now company information in form of chunks

# Cant take actions

### Tool augmented chatbot

# Reactive

# No memory

# Specific advice resolved

# Can take actions now

# Cant Adapt

### Agentic AI chatbot

# Pro active

# Memory issue resolved it have context

# Specific Advice (as it have rag implement so can give advice)

# Can take actions (it have tools access)

# Can Adapt (identify the problem, give solution and implement it)

### Conclusion

Generative AI is about creating content, Agentic AI is about solving a goal.

Generative AI is reactive, Agentic AI is proactive (Autonomous)

Generative AI is a building block of Agentic AI

### Agentic AI definition

Agentic AI is a type of the AI that can take up a task or goal from a user
and then work torward completing it on its own, with minimal human guidance.
It plans, take actions, adapt to changes, and seek help only when necessary.

## key Characteristics

# Autonomous

Autonomy refers to the AI system’s ability to make decisions and take actions on its own to achieve a given goal, without needing step-by-step human instructions.

# Autonomy means function independently and achieve goal

Our AI recruiter is autonomous (We give it a goal, then it did planning and then achieved the goal, There was minimum human intercation)

It’s proactive (it takes decision on its own according to the situation)

Autonomy in multiple facets

a. Execution

b. Decision making

c. Tool usage

Autonomy can be controlled

a. Permission Scope - Limit what tools or actions the agent can perform independently. (Can screen candidates, but needs approval before rejecting anyone.)

b. Human-in-the-Loop (HITL) - Insert checkpoints where human approval is required before continuing. (Can I post this JD)

c. Override Controls - Allow users to stop, pause, or change the agent’s behaviour at any time. (pause screening command to halt resume processing.)

d. Guardrails / Policies - Define hard rules or ethical boundaries the agent must follow. (Never schedule interviews on weekends)

Autonomy can be dangerous

a. The application autonomously sends out job offers with incorrect salaries or terms.

b. The application shortlists candidates by age or nationality, violating anti-discrimination laws.

c. The applications spending extra on LinkedIn ads.

# Goal Oriented

Being goal-oriented means that the AI system operates with a persistent objective in mind and continuously directs its actions to achieve that objective, rather than just responding to isolated prompts.

Goals acts as a compass for Autonomy (Autonomy means function independently and achieve goal)

Goals can come with constraints (constraint means condition for example the dev should be only from pak)

Goals are stored in core memory (Every library have its own mechanism to handle memory)

JSON
{
"main_goal": "Hire a backend engineer",
"constraints": {
"experience": "2-4 years",
"remote": true,
"stack": ["Python", "Django", "Cloud"]
},
"status": "active",
"created_at": "2025-06-27",
"progress": {
"JD_created": true,
"posted_on": ["LinkedIn", "AngelList"],
"applications_received": 8,
"interviews_scheduled": 2
}
}
Goals can be altered

# Planning

Planning is the agent’s ability to break down a high-level goal into a structured sequence of actions or subgoals and decide the best path to achieve the desired outcome.

Step 1: Generating multiple candidate plans
Plan A: Post JD on LinkedIn, GitHub Jobs, AngelList

Plan B: Use internal referrals and hiring agencies

Step 2: Evaluate each plan
Efficiency (Which is faster?)

Tool Availability (Which tools are available)

Cost (Does it require premium tools?)

Risk (Will it fail if we get no applicants?)

Alignment with constraints (remote-only? budget?)

Step 3: Select the best plan with the help of:
Human-in-the-loop input (e.g., “Which of these options do you prefer?”)

A pre-programmed policy (e.g., “Favor low-cost channels first”)

# Reasoning

Reasoning is the cognitive process through which an agentic ai system interprets information, draws conclusions, and makes decisions — both while planning ahead and while executing actions in real time.

Reasoning During Planning:
Goal decomposition - Break down abstract goals into concrete steps

Tool selection - Decide which tools will be needed for which steps

Resource estimation - Estimate time, dependencies, risks

Reasoning During Execution:
Decision-making - Choosing between options (3 candidates match → schedule 2 best, reject 1)

HITL handling - Knowing when to pause and ask for help (Unsure about salary range)

Error handling - Interpreting tool/API failures and recovering

# Adaptability

Adaptability is the agent's ability to modify its plans, strategies, or actions in response to unexpected conditions — all while staying aligned with the goal.

Failures (Calendar API)

External feedback (Less no of applications)

Changing goals (Hiring a freelancer)

# Context Awareness

Context awareness is the agent’s ability to understand, retain, and utilize relevant information from the ongoing task, past interactions, user preferences, and environmental cues to make better decisions throughout a multi-step process.

Types of context

a. The original goal

b. Progress till now + Interaction history (Job description was finalized and posted to LinkedIn & GitHub Jobs)

c. Environment state (Number of applicants so far = 8 or LinkedIn promotion ends in 2 days)

d. Tool responses (Resume parser -> "Candidate B has 3 years Django + AWS experience or Calendar API -> "No conflicts at 2 PM Wednesday)

e. User specific preferences (Prefers remote-first candidates or Likes receiving interview questions in a Google Doc)

f. Policy or Guardrails (Do not send offer without explicit user approval or Never use platforms that require paid ads unless approved)

Context awareness is implemented through memory

Short term memory (current session memory)

Long term memory

### Components

# Brain (LLM)

Goal Interpretation: Understands user instructions and translates them into objectives.

Planning: Breaks down high-level goals into subgoals and ordered steps.

Reasoning: Makes decisions, resolves ambiguity, and evaluates trade-offs.

Tool Selection: Chooses which tool(s) to use at a given step.

Communication: Generates natural language outputs for humans or other agents.

# Orchestrator (Executor)

Task Sequencing: Determines the order of actions (step 1 → step 2 → ...).

Conditional Routing: Directs flow based on context (e.g., if failure, retry or escalate).

Retry Logic: Handles failed tool calls or reasoning attempts with backoff.

Looping & Iteration: Repeats steps (e.g., keep checking job apps until 10 are received).

Delegation: Decides whether to hand off work to tools, LLM, or human.

# Tools

External Actions: Perform API calls (e.g., post a job, send an email, trigger onboarding).

Knowledge Base Access: Retrieve factual or domain-specific information using RAG or search tools to ground responses.

# Memory

Short-Term Memory: Maintains the active session's context — recent user messages, tool calls, and immediate decisions.

Long-Term Memory: Persists high-level goals, past interactions, user preferences, and decisions across sessions.

State Tracking: Monitors progress: what's completed, what's pending (e.g., "JD posted", "Offer sent").

# Supervisor (HITL, Human + Agent)

Approval Requests (HITL): Agent checks with human before high-risk actions (e.g., sending offers).

Guardrails Enforcement: Blocks unsafe or non-compliant behavior.

Edge Case Escalation: Alerts humans when uncertainty/conflict arises.

### Challenges in using langchain

## Control Flow Complexity

Conditional branch

Loops

Jumps

## Handling State

States are basically in form of key and value pairs and langchain dont offer anything to store and track these key value pairs.
it have memory which it store during conversation but it cant handle state so we have to do this manually.
In langgraph during creation of gaph we create a state object, which can be made with pydantic and typeddic. Every node have access
to this dictionary. Every node have access to the state and its changes.

## Event Driven Execution (External interaction)

We have two kind of workflows
(1) Sequential
(2) Event Driven
Langchain basically designed for sequential chains, to handle even driven execution we need to write alot of glue code.
Langgraph have this even driven ability and it can resume the workflow where it was stopped. We can save state into memory or external memory. To save our state we can use checkpointer.

## Fault Tolerance (System can work again if it was shutdown due to a fault)

Langchain doesnt have fault tolerance feature, langchain meant to built for short running tasks. Meanwhile langgraph can handle
long running workflows and their is higher probability of occurance of a fault. Langgchain can resume the workflow where it was before
crash using retry logic.
For big fault langgraph have recovery option.

## Human in the loop

In short term workflow we can ask human for permission and workflow can wait but in long workflows it will keep eating resources if we use langchain. or we can make two chains and then ask for permission from human, once permission granted then we can start second chain but it will need alot of glue code need to be wrote

## Nested Workflows

## Observability

refers to how easily you can monitor, debug, and understand what your workflow is doing at runtime.
We can achieve this using langsmith with langchain but langsmith dont work with glue code.

### Conclusion

1. What is LangGraph?
   LangGraph is an orchestration framework that enables you to build stateful, multi-step, and event-driven workflows using large language models (LLMs). It's ideal for designing both single-agent and multi-agent agentic AI applications.

Think of LangGraph as a flowchart engine for LLMs — you define the steps (nodes), how they're connected (edges), and the logic that governs the transitions. LangGraph takes care of state management, conditional branching, looping, pausing/resuming, and fault recovery — features essential for building robust, production-grade AI systems.

2. When to Use What?
   Use LangChain when you're building simple, linear workflows — like a prompt chain, summarizer, or a basic retrieval system.

Use LangGraph when your use case involves complex, non-linear workflows that need:

Conditional paths

Loops

Human-in-the-loop steps

Multi-agent coordination

Asynchronous or event-driven execution

3. Should We Still Use LangChain?
   Yes. LangGraph is built on top of LangChain — it doesn’t replace it.

You’ll still use LangChain components like:

ChatOpenAI (LLMs)

PromptTemplate

Retrievers

DocumentLoaders

Tools, etc.

LangGraph handles workflow orchestration, while LangChain provides the building blocks for each step in that workflow.

### What is LangGraph

LangGraph is an orchestration framework for building intelligent, stateful, and multi-step LLM workflows.

It enables advanced features like parallelism, loops, branching, memory, and resumability — making it ideal for agentic and production-grade AI applications.

It models your logic as a graph of nodes (tasks) and edges (routing) instead of a linear chain.

### LangGraph Core Concepts

## LLM Workflows

Workflows are basically series of tasks to achieve a goal. A task which need LLM during execution to completed can be called LLM Workflow.

(1) LLM workflows are a step by step process using which we can build complex LLM applications.

(2) Each step in a workflow performs a distinct task — such as prompting, reasoning, tool calling, memory access, or decision-making.

(3) Workflows can be linear, parallel, branched, or looped, allowing for complex behaviours like retries, multi-agent communication, or tool-augmented reasoning.

(4) Common workflows

(4.1) Prompt Chaining

When you have a complex task, you convert it into subtasks. Here you build a chain and interact with multiple LLm, you share previous LLM output with next LLM.

(4.2) Routing
In routing workflow you understand task and decide who will execute the task.
For example LLM recieve sales related query then LLM will decide to which LLM this query should be sent as there can be multiple deparments so query should be went to related LLM. The LLM responsible for sending query to related LLM to query is called router.

(4.3) Parallelization
In this you convert a task into multiple sub-tasks and execute them at once, then merge their results and look for final outcome.

For example you are making a content moderation workflow for youtube, you check uploaded video with multiple angels,
is video is appropriate ? does it have adult content ? is the video following community guidelines ? then we look at finan outcome of all LLMs and behalf of that we tak final decision. All LLMs will send their outcome to aggregator and then aggregator will make dicsion to flag the video or let it upload.

(4.4) Orchestrator Workers

This workflow is also similar to parallelization but the difference is here we dont know which LLM will handle which part of workflow.
There is orchestrator which decides on the basis of the query which LLM will perform specific task and at the the end there is a synthesizer which will give output.

(4.5) Evaluator Optimizer

In this workflow we have a LLM call generator which for example create a blog on specific topic then LLM call Evaluator which have specific criteria given by us which checks if the blog meet with our expectations if yes then it accept it and if it reject then it also provide feedback then LLM call generator generate another blog. Basically this entire process work in form of iteration and it keep going until unless it dont generate expected result.
