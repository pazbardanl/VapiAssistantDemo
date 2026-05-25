# VapiAssistantDemo

A demo project showcasing an AI voice assistant built with [Vapi](https://vapi.ai), paired with an AWS Lambda webhook handler for backend integration. The assistant acts as an inbound FAQ bot for a freelancer, answering common questions about services and collecting lead information over the phone.

## Project structure

```
VapiAssistantDemo/
├── Assistant/
│   ├── system_prompt.txt    # Vapi assistant instructions and FAQ knowledge base
│   └── first_message.txt    # Opening greeting when a call connects
└── AWS/
    └── lambda/
        └── VAPI_LAMBDA_WEBHOOK_HANDLER/
            └── vapi_webhook_handler.py   # Lambda handler for Vapi webhooks
```

## Assistant

The voice assistant is configured to handle inbound calls as a friendly FAQ bot. It answers high-level questions about services, process, timelines, and pricing, and collects lead details (name, company, email, needs) when callers want to hire or speak with the freelancer directly.

| File | Purpose |
|------|---------|
| `Assistant/system_prompt.txt` | Defines tone, behavior, guardrails, and an FAQ knowledge base |
| `Assistant/first_message.txt` | The first thing the assistant says when a call starts |

Copy these into your Vapi assistant configuration (system prompt and first message fields) when setting up the demo.

## AWS Lambda webhook handler

`vapi_webhook_handler.py` is a minimal AWS Lambda function that receives Vapi webhook events, logs the full payload, and returns a 200 response. Use it as a starting point for custom backend logic—call routing, CRM updates, database writes, or other integrations triggered by Vapi events.

### Deploying the Lambda

1. Create a Lambda function in AWS (Python 3.x runtime).
2. Upload or paste the contents of `vapi_webhook_handler.py`.
3. Configure a Function URL or API Gateway endpoint.
4. In the Vapi dashboard, set the webhook URL to your Lambda endpoint.

The handler currently logs incoming events and responds with:

```json
{ "message": "Hello from Lambda!" }
```

Extend `lambda_handler` to process specific Vapi event types (e.g. `call-started`, `end-of-call-report`, tool calls) as needed.

## Prerequisites

- A [Vapi](https://vapi.ai) account and phone number or SIP setup
- An AWS account for deploying the webhook Lambda (optional, for backend integration)

## License

Demo project — use and adapt as needed.
