# Conversation Chain for Home Assistant

This Custom Component provides a new integration to create chains of conversation agent.

### Example Use Case

Answer all requests with the built-in default agent. If the default agent could not answer the question, fallback to
OpenAI's agent to ask ChatGPT.

### How it works

The agent asks the first configured agent to handle the request. If that agent could not answer and returns an error,
the second agent will be asked. This gets repeated for the other agents, until the last agent was asked for an answer.
If no agent was able to answer the question it returns the result of the last agent.

## Installation

Add this repository as a new source in HACS.

## Configuration (UI only)

1. Create a new integration of "Conversation Chain"
2. Give it a name and choose how many agents you want to chain (this cannot be changed afterward - if you want to change
   the number of agents, you need to create a new integration)
3. Open the newly created integration and click "configure"
4. Configure the agent to use for each slot in the chain

## Usage

### Assist
You can easily use this agent as conversation agent in Assist.

### Service
You can call the built-in `conversation.process` service and use your chain-agent id.

```yaml
service: conversation.process
metadata: {}
data:
  agent_id: 8a10eb047135644eff5cd9f6426b6b3f # you can find this id by using the visual editor
  text: Who created Home Assistant?
```
