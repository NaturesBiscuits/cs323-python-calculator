letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(key : int, message : str):
    encryptedText = ""
    for m in message:
        if letters.count(m) < 1:
            encryptedText += m
            continue
        index = letters.index(m)
        print(index)
        encryptedText += letters[(index ** key) % 26]
    
    return encryptedText

def decrypt(key : int, message : str):
    decryptedText = ""
    for m in message:
        if letters.count(m) < 1:
            decryptedText += m
            continue
        index = letters.index(m)
        decryptedText += letters[(index ** key) % 26]
    
    return decryptedText

if __name__ == "__main__":
    while(True):
        print("(1) Encrypt\n(2) Decrypt\n(0) Quit")
        selection = int(input("> "))
        match selection:
            case 1:
                inputText = input("Enter Unencrypted Text: ")
                inputKey = int(input("Enter Key: "))
                print(encrypt(inputKey, inputText))
            case 2:
                inputText = input("Enter Encrypted Text: ")
                inputKey = int(input("Enter Key: "))
                print(decrypt(inputKey, inputText))
            case 0:
                print("Goodbye!")
                break
