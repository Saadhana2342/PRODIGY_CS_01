

def encrypt(text,shift):
    alphabet_lower='abcdefghijklmnopqrstuvwxyz'
    alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_text=''
    for char in text:
        if char in alphabet_lower:
            new_index=(alphabet_lower.index(char)+shift)%26
            encrypted_text+=alphabet_lower[new_index]
        elif char in alphabet_upper:
            new_index=(alphabet_upper.index(char)+shift)%26
            encrypted_text+=alphabet_upper[new_index]
        else:
            encrypted_text+=char
    return encrypted_text
def decrypt(text,shift):
    alphabet_lower='abcdefghijklmnopqrstuvwxyz'
    alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_text=''
    for char in text:
        if char in alphabet_lower:
            new_index=(alphabet_lower.index(char)-shift)%26
            decrypted_text+=alphabet_lower[new_index]
        elif char in alphabet_upper:
            new_index=(alphabet_upper.index(char)-shift)%26
            decrypted_text+=alphabet_upper[new_index]
        else:
            decrypted_text+=char
    return decrypted_text

def main():
    op = input("Enter your choice: \n 1.Encryption  \n 2.Decryption \n")
    text = input("Enter the text: ")
    shift = int(input("Enter the number of shifts: "))
    if op == '1':
        result = encrypt(text, shift)
        print("Encrypted text: ",result)
    elif op == '2':
        result = decrypt(text, shift)
        print("Decrypted text: ",result)
    else:
        print("Invalid choice.")
 
if __name__ == "__main__":
    main()


            