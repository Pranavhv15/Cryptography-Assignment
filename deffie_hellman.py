def fun_dh(g, p, x, y):
    A = pow(g, x, p)
    B = pow(g, y, p)
    secretA = pow(B, x, p)
    secretB = pow(A, y, p)
    if secretA == secretB:
        return secretA
    else:
        raise Exception("Shared secrets do not match!")

g = int(input("Enter Generated Public Key g : "))
p = int(input("Enter Prime Number Public key p: "))  
x = int(input("Enter Sender Private Key x: "))   
y = int(input("Enter Reciever Private Key y: "))  

symmetricKey = fun_dh(g, p, x, y)

print("Symmetric Key:", symmetricKey)