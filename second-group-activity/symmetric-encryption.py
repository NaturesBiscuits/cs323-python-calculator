#SIMPLE CAESAR CIPHER
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(key : int, message : str):
    encryptedText = ""
    for m in message:
        if letters.count(m) < 1:
            encryptedText += m
            continue
        index = letters.index(m)
        encryptedText += letters[(index + key) % 26]
    
    return encryptedText

def decrypt(key : int, message : str):
    decryptedText = ""
    for m in message:
        if letters.count(m) < 1:
            decryptedText += m
            continue
        index = letters.index(m)
        decryptedText += letters[(index - key) % 26]
    
    return decryptedText

if __name__ == "__main__":
    test = "All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.".lower()
    key = 5

    encryptedText = encrypt(key, test)
    decryptedText = decrypt(key, encryptedText)

    print(f"Key: {key}\nInitial Text: {test}\nEncrypted Text: {encryptedText}\nDecrypted Text: {decryptedText}")
