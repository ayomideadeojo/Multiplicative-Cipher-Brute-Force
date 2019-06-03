KEY = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(n, ciphertext):
    result = ''
    
    for x in ciphertext:
        try:
            index = KEY.index(x)
            i = (index * n) % 26
            result = i
        except Valueerror:
            result += i
    return result
    
for n in range(0,25):
    dec1 = decrypt(n,'d')
    dec2 = decrypt(n,'a')
    dec3 = decrypt(n,'f')
    dec4 = decrypt(n,'l')
    dec5 = decrypt(n,'a')
    dec6 = decrypt(n,'w')
    print ("%d . %s %s %s %s %s %s" % (n,dec1,dec2,dec3,dec4,dec5,dec6))
    
