def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - offset + shift) % 26 + offset)
            elif mode == 'decrypt':
                result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))
mode = input("Choose 'encrypt' or 'decrypt': ").strip().lower()

# Result
output = caesar_cipher(message, shift, mode)
print(f"\nResult ({mode}ed message): {output}")