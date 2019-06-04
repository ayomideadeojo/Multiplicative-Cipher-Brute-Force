KEY = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(n, ciphertext):
    result = ''
    
    for x in ciphertext:
        index = KEY.index(x)
        i = (index * n) % 26
        result = i
    return result
    
for n in range(0,26):
    dec1 = decrypt(n,'c')
    dec2 = decrypt(n,'k')
    dec3 = decrypt(n,'q')
    dec4 = decrypt(n,'b')
    dec5 = decrypt(n,'q')
    dec6 = decrypt(n,'y')
    print ("%d . %s%s%s%s%s%s" % (n,chr(dec1 + 97),chr(dec2 + 97),chr(dec3 + 97),
    chr(dec4 + 97),chr(dec5 + 97),chr(dec6 + 97)))
