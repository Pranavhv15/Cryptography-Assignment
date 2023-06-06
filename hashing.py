import random
def hashing(message):
    random.seed(message) 
    hashingValue = random.randint(0, 3**10-1)
    return hashingValue

message=input("Enter the Message to be sent:")
hashedValue=hashing(message)

print("Sent Message:", message) 
print("Hash value:", hashedValue)

receivedMessage=input("Enter the Received message: ")
receivedHashValue=hashing(receivedMessage) 

print("Received Message:", receivedMessage)
print("Received Hash value:", receivedHashValue)

if receivedHashValue == hashedValue: 
    print("Ensured Integrity: The message has not been modified.")
else:
    print("Ensured Integrity: The message has been modified.")