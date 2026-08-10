# Diffie-Hellman Key Exchange Algorithm


p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))


mike_private = int(input("Enter Mike's private key: "))


jordan_private = int(input("Enter Jordan's private key: "))


mike_public = (g ** mike_private) % p


jordan_public = (g ** jordan_private) % p

print("\nMike's Public Key:", mike_public)
print("Jordan's Public Key:", jordan_public)


mike_secret = (jordan_public ** mike_private) % p
jordan_secret = (mike_public ** jordan_private) % p

print("\nShared Secret Key computed by Mike:", mike_secret)
print("Shared Secret Key computed by Jordan:", jordan_secret)


if mike_secret == jordan_secret:
    print("\nKey Exchange Successful!")
    print("Secure Shared Key:", mike_secret)
else:
    print("\nKey Exchange Failed!")