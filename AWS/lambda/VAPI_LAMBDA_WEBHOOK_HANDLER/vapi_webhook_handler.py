import json
import os
import boto3
from datetime import datetime
from zoneinfo import ZoneInfo

ses = boto3.client("ses", region_name=os.environ.get("SES_REGION", "eu-north-1"))

def lambda_handler(event, context):

    print("=== EVENT RECEIVED ===")

    print_event(event)
    body = json.loads(event.get("body") or "{}")
    message_type = get_message_type(body)
    print(f"Message type: {message_type}")
    if message_type == "end-of-call-report":
        transcript = extract_transcript(body)
        print_transcript(transcript)
        send_transcript_email(transcript)

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

def print_transcript(transcript):
    print("-- Transcript:")
    print(transcript)
    print("-- End Transcript")

def extract_transcript(body):
    transcript = (
        body.get("message", {})
            .get("artifact", {})
            .get("transcript")
    )
    return transcript

def send_transcript_email(transcript):
    email_from = os.environ["EMAIL_FROM"]
    email_to = os.environ["EMAIL_TO"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = ses.send_email(
        Source=email_from,
        Destination={
            "ToAddresses": [email_to]
        },
        Message={
            "Subject": {
                "Data": "Vapi Call Transcript - " + timestamp
            },
            "Body": {
                "Text": {
                    "Data": transcript
                }
            }
        }
    )
    print(f"SES response: {json.dumps(response, default=str)}")