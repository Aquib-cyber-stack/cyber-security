from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()


message = input("Enter the message to sign: ").encode()


signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nDigital Signature Generated Successfully!")
print("Signature (hex):", signature.hex())


verify_message = input("\nEnter the message to verify: ").encode()

try:
    public_key.verify(
        signature,
        verify_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("\n✓ Signature Verified Successfully!")
    print("Integrity: Maintained")
    print("Authenticity: Verified")

except Exception:
    print("\n✗ Signature Verification Failed!")
    print("The message has been modified or is not authentic.")