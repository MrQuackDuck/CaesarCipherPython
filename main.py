class Encryptor:
    def __init__(self, Index, AllSymbols):
        self.Index = int(Index)
        self.AllSymbols = AllSymbols

    def EncryptWithCaesarCipher(self, message):
        resultString = ""
        for char in message:
            indexOfCurrentChar = self.AllSymbols.index(char)

            if (indexOfCurrentChar + self.Index) >= len(self.AllSymbols):
                rest = (indexOfCurrentChar - self.Index) - len(self.AllSymbols)
                resultString = resultString + self.AllSymbols[rest]
            else:
                resultString += self.AllSymbols[indexOfCurrentChar + self.Index]
        return  resultString
    def DecryptWithCaesarCipher(self, message):
        resultString = ""
        for char in message:
            indexOfCurrentChar = self.AllSymbols.index(char)

            if (indexOfCurrentChar - self.Index) < 0:
                rest = (indexOfCurrentChar - self.Index) - len(self.AllSymbols)
                resultString += self.AllSymbols[rest]
            else:
                resultString = resultString + self.AllSymbols[indexOfCurrentChar - self.Index]
        return resultString



caesarEncryptor = Encryptor(3, " abcdefghijklmnopqrstuvwxyzабвгґдеєжзиіїйклмнопрстуфхцчшщьюя123456789!&?_\/")
message = input("Write your message: ")

encryptedMessage = caesarEncryptor.EncryptWithCaesarCipher(message)
decryptedMessage = caesarEncryptor.DecryptWithCaesarCipher(encryptedMessage)

print(f"Your encrypyed message: {encryptedMessage}")
print(f"Your decrypted message: {decryptedMessage}")