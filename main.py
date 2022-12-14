class Encryptor:
    def __init__(self, Index, AllSymbols):
        self.Index = int(Index)
        self.AllowedSymbols = AllSymbols

    def EncryptWithCaesarCipher(self, message):
        resultString = ""
        allowedSymbolsLength = len(self.AllowedSymbols)

        for char in message:
            # Index of current char in allowed symbols
            indexOfCurrentChar = self.AllowedSymbols.index(char)

            # Checks if current char index is not out of bounds of allowed symbols list
            if (indexOfCurrentChar + self.Index) >= allowedSymbolsLength:
                rest = (indexOfCurrentChar + self.Index) - allowedSymbolsLength
                resultString += self.AllowedSymbols[rest]
            elif indexOfCurrentChar + self.Index < 0:
                rest = allowedSymbolsLength + (indexOfCurrentChar + self.Index)
                resultString += self.AllowedSymbols[rest]
            else:
                resultString += self.AllowedSymbols[indexOfCurrentChar + self.Index]
        return  resultString

    def DecryptWithCaesarCipher(self, message):
        resultString = ""
        allowedSymbolsLength = len(self.AllowedSymbols)
        for char in message:
            indexOfCurrentChar = self.AllowedSymbols.index(char)

            # Checks if current char index is not out of bounds of allowed symbols list
            if (indexOfCurrentChar - self.Index) < 0:
                rest = allowedSymbolsLength + (indexOfCurrentChar - self.Index)
                resultString += self.AllowedSymbols[rest]
            elif (indexOfCurrentChar - self.Index) >= allowedSymbolsLength:
                rest = (indexOfCurrentChar - self.Index) - allowedSymbolsLength
                resultString += self.AllowedSymbols[rest]
            else:
                resultString = resultString + self.AllowedSymbols[indexOfCurrentChar - self.Index]
        return resultString


index = 2

caesarEncryptor = Encryptor(index, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ123456789!&?_\/';@$%^~,.{}[]` ")
message = input("Write your message: ")

encryptedMessage = caesarEncryptor.EncryptWithCaesarCipher(message)
decryptedMessage = caesarEncryptor.DecryptWithCaesarCipher(encryptedMessage)

print(f"Your encrypyed message: {encryptedMessage}")
print(f"Your decrypted message: {decryptedMessage}")
