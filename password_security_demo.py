import math
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def calculate_entropy(password: str) -> float:
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(not c.isalnum() for c in password): pool += 32
    return round(len(password) * math.log2(pool), 2) if pool else 0.0

if __name__ == "__main__":
    print("Entropy 123456:", calculate_entropy("123456"))
    print("Entropy k9#mP$2vL!9xQ@zW:", calculate_entropy("k9#mP$2vL!9xQ@zW"))