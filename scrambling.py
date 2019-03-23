import random,string
def scramble():
    name=input("enter filename:")
    f=open(name,"r")
    e=f.read()
    print(e)
    l=(".",",","?")
    wordlist=e.split(" ")
    
    final=" "
    for i in range(len(wordlist)):
       
        s=wordlist[i]
        if len(s)>4 and s.endswith(l):
            n=len(s)
            s1=s[-1]
            s4=s[-2]
            s2=s[0]
            s3=list(s[1:n-2])
            random.shuffle(s3)
            y="".join(s3)
           
            si=s2+y+s4+s1+" "
            wordlist[i]=si
            
            final+=si
        elif len(s)>3 and not s.endswith(l):
            
            n=len(s)
            s1=s[-1]
            s2=s[0]
            s3=list(s[1:n-1])
            random.shuffle(s3)
            y="".join(s3)
           
            si=s2+y+s1+" "
            wordlist[i]=si
            
            final+=si
        else :
           
            wordlist[i]+=" "
            final+=wordlist[i]
    fo=open("D:\\python\\scrambled.txt","w")
    fo.write(final)
    fo.close()
    f.close()

    
scramble()    
        
