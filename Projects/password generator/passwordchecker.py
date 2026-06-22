correctpassword='admin123'
attempts=0
maxattempts=3
while attempts<maxattempts:
    entered=input("enter password")
    if entered==correctpassword:
        print('password accepted')
        break
    else:
        attempts+=1
        if attempts<maxattempts:
            print(f'sorry you got your password wrong..please try again! you have {maxattempts -attempts} attempts left')
        else:
            print('max attempts reached please contact administrator')