import hmac
import hashlib

# Shared secret key
secret_key = b"mysecretkey"

# Message
message = b"Hello, Secure World!"

# Generate MAC
mac = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
print("Generated MAC:", mac)

# Verify MAC
received_message = b"Hello, Secure World!"
received_mac = mac

calculated_mac = hmac.new(
    secret_key,
    received_message,
    hashlib.sha256
).hexdigest()

if hmac.compare_digest(received_mac, calculated_mac):
    print("MAC Verification Successful")
    print("Message is Authentic and Untampered")
else:
    print("MAC Verification Failed")
    print("Message Integrity Compromised")