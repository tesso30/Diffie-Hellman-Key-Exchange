# Diffie-Hellman Key Exchange Simulation in Python

# Function to compute power mod p (modular exponentiation)
def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        exp = exp >> 1  # exp = exp // 2
        base = (base * base) % mod
    return result

# Public parameters agreed by Alice and Bob
p = 23  # A prime number
g = 5   # A generator (primitive root modulo p)

# Alice chooses a private key a, and computes A = g^a mod p
a = 6  # Alice’s private key
A = power_mod(g, a, p)

# Bob chooses a private key b, and computes B = g^b mod p
b = 15  # Bob’s private key
B = power_mod(g, b, p)

# Exchange of public keys A and B happens between Alice and Bob

# Alice computes the shared secret S1 = B^a mod p
S1 = power_mod(B, a, p)

# Bob computes the shared secret S2 = A^b mod p
S2 = power_mod(A, b, p)

# Both S1 and S2 should be the same shared secret
print(f"Shared Secret Calculated by Alice: {S1}")
print(f"Shared Secret Calculated by Bob: {S2}")

if S1 == S2:
    print("Shared secret established successfully!")
else:
    print("Error: Shared secrets do not match!")
