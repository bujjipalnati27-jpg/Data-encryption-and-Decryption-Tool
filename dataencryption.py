print("===== Data Encryption and Decryption Tool =====")

text = input("Enter your message: ")
key = int(input("Enter key value: "))

# Encryption
encrypted = ""

for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        encrypted += chr((ord(char) - start + key) % 26 + start)
    else:
        encrypted += char

print("\nEncrypted Message:", encrypted)

# Decryption
decrypted = ""

for char in encrypted:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        decrypted += chr((ord(char) - start - key) % 26 + start)
    else:
        decrypted += char

print("Decrypted Message:", decrypted)
