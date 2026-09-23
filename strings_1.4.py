def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])

    return " ".join(reversed_words)

print(reverse_words("Hello World Python"))


def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + shift)
    return encrypted_text


def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        decrypted_text += chr(ord(char) - shift)
    return decrypted_text


# בדיקת הקוד
original_text = "ABC"
shift_val = 3

encrypted = caesar_encrypt(original_text, shift_val)
decrypted = caesar_decrypt(encrypted, shift_val)

print(f"Original:  {original_text}")
print(f"Encrypted: {encrypted}")  # יקבל 'DEF'
print(f"Decrypted: {decrypted}")  # יחזיר 'ABC'