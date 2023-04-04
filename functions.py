# Extract "/qr" from the user's message and return the url to create QR Code
def extract_string(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]
    return string
