import json

def lambda_handler(event, context):

    print("=== EVENT RECEIVED ===")

    print_event(event)
    body = json.loads(event.get("body") or "{}")
    message_type = get_message_type(body)
    print(f"Message type: {message_type}")
    if message_type == "end-of-call-report":
        print_transcript(body)

    print("=== END EVENT ===")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Lambda!'
        })
    }

def print_event(event):
    print("-- Event Dump:")
    print(json.dumps(event))
    print("-- End Event Dump")

def get_message_type(body):
    return body.get("message", {}).get("type")

def print_transcript(body):
    print("-- Transcript:")
    print(extract_transcript(body))
    print("-- End Transcript")

def extract_transcript(body):
    transcript = (
        body.get("message", {})
            .get("artifact", {})
            .get("transcript")
    )
    return transcript