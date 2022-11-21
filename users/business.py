

password = 'Ab@123456'
count = 0
for p in password:
    if (p.islower()): 
        count+=1
        print(f' {p}, letra minuscula {count}')
    if (p.isupper()): 
        count+=1
        print(f' {p}, letra maiuscula {count}')
    if(p=='@'or p=='$' or p=='_'): 
        count+=1
        print(f' {p}, simbolo {count}')
if count >= 3: 
    print("Valid Password") 
else: 
    print("Invalid Password") 

