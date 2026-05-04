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
