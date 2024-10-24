def decoder(enc):
    a=len(enc)
    i=0
    resut=""
    while i<a:
        resut+=str((int(enc[i])-3)%10)
        i+=1
    return resut