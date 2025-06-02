def main():
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
    ]
    user_pref = input("Type 'encode' to encrypt or type 'decode' to decrypt: ").lower()
    text = input("Type the message: ").lower()
    shift = int(input("Enter the shift number: "))

    if user_pref == 'encode':
        encrypt(text, shift, alphabet)
    elif user_pref == 'decode':
        decrypt(text, shift, alphabet)


def encrypt(text, shift, alphabet):
    st = ''
    for i in text:
        if i not in alphabet:
            st += i
        else:
            index = (shift + alphabet.index(i)) % len(alphabet)
            st += alphabet[index]
    print(f"Encrypted text: {st}")


def decrypt(text, shift, alphabet):
    st = ''
    for i in text:
        if i not in alphabet:
            st += i
        else:
            index = (alphabet.index(i) - shift)
            st += alphabet[index]
    print(f"Decrypted Text: {st}")


if __name__ == "__main__":
    from banner import ban
    print(ban)
    main()
    user = input("Type 'yes' if you want to go again. Otherwise 'no': ").lower()
    if user == 'yes':
        main()
    else:
        print("Good Bye")
