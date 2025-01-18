import base64
with open('api.py','r') as file:
    text = file.read()

# Encode the string to bytes, then encode to Base64
encoded_bytes = base64.b64encode(text.encode('utf-8'))
encoded_str = encoded_bytes.decode('utf-8')
with open('api_encode.py','w') as filee:
    filee.write(encoded_str)