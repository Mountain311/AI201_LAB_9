def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(message):

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol

        print('Hacking key #%s: %s' % (key, translated))


text = input("Enter Text to Encrypt:")
s = int(input("Enter Shift Key:"))

print()

print ("Cipher: " + encrypt(text,s))

print('\n\n')

detext = input("Enter Text to Decrypt")

decrypt(detext)
