def decoder(enc):
    a=len(enc)
    i=0
    result=""
    while i<a:
        result+=str((int(enc[i])-3)%10)
        i+=1
    return result