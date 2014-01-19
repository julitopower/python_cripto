'''
Created on 03/10/2010

@author: veryweb
'''
from Crypto.Cipher import Blowfish
from random import randrange
import hashlib
class Security(object):

    def encrypt(self,model,password):
        print "Encript has been called"
        inputFile = file(model.getSource(),'rb')
        outputFile = file("".join([model.getDestination(),'/',self.getInputName(model.getSource()),'.enc']),'wb')
        hasher = hashlib.md5()
        hasher.update(password)
        password =hasher.digest()
        encryptedText = BFCipher(password).encrypt(inputFile.read())
        outputFile.write(encryptedText)
        outputFile.flush()
        outputFile.close()
        
    def decrypt(self,model,password):
        print "Encript has been called"
        inputFile = file(model.getSource(),'rb')
        outputFile = file("".join([model.getDestination(),'/',self.getInputName(model.getSource()),'.clean']),'wb')
        hasher = hashlib.md5()
        hasher.update(password)
        password =hasher.digest()
        encryptedText = BFCipher(password).decrypt(inputFile.read())
        outputFile.write(encryptedText)
        outputFile.flush()
        outputFile.close()
        
    def getInputName(self,input):
        if input.rfind('.') != -1:
            input = input[:input.rfind('.')]
        return input[input.rfind('/'):]
        
class BFCipher:
    def __init__(self, pword):
        self.__cipher = Blowfish.new(pword)
    def encrypt(self, file_buffer):
        ciphertext = self.__cipher.encrypt(self.__pad_file(file_buffer))
        return ciphertext
    def decrypt(self, file_buffer):
        cleartext = self.__depad_file(self.__cipher.decrypt(file_buffer))
        return cleartext
    # Blowfish cipher needs 8 byte blocks to work with
    def __pad_file(self, file_buffer):
        pad_bytes = 8 - (len(file_buffer) % 8)                                
        for i in range(pad_bytes - 1): file_buffer += chr(randrange(0, 256))
        # final padding byte; % by 8 to get the number of padding bytes
        bflag = randrange(6, 248); bflag -= bflag % 8 - pad_bytes
        file_buffer += chr(bflag)
        return file_buffer
    def __depad_file(self, file_buffer):
        pad_bytes = ord(file_buffer[-1]) % 8
        if not pad_bytes: pad_bytes = 8
        return file_buffer[:-pad_bytes]
