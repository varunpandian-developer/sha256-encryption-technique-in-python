#import the hashlib library
import hashlib
def encrypt(hash):
    variabletoencrypt = hashlib.sha256(hash.encode()).hexdigest()
    return variabletoencrypt

hash= 'varunpandian developer'
variabletoencrypt = encrypt(hash)
print(variabletoencrypt)