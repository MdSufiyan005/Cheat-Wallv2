import json
import base64
import hashlib



def decode_json(encoded_str):
    # Decode from Base64
    decoded_bytes = base64.urlsafe_b64decode(encoded_str)  # No truncation or padding issues
    # Convert bytes back to JSON
    return json.loads(decoded_bytes.decode('utf-8'))

# Example usage
decoded_data = decode_json('eyJBcHBfTmFtZSI6ICJzZGdmYXNmZ2Rhc2ZkZzI0cjM0NSIsICJBY2Nlc3NfVG9rZW4iOiAiUDU5UiIsICJTdGFydF9UaW1lIjogIjIwMjUtMDMtMjIgMTc6MTA6MDArMDA6MDAiLCAiRW5kX1RpbWUiOiAiMjAyNS0wMy0yMiAxMjoxMTowMCswMDowMCIsICJEaXNjcmlwdGlvbiI6ICJhc2RmYXNkIn0=')

print("Decoded:", decoded_data)
