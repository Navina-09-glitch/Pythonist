from LoginException import LoginUserError, LoginPasswordError
def welcome(uname):
    print("Hi {}, Good Morning-Good Rememberence about username and pwd".format(uname))
def validation(uname,pwd):
    usernames=["python","java","c"]
    passwords=["rossum","james","ritchie"]
    if uname not in usernames:
        raise LoginUserError
    else:
        if pwd not in passwords:
            raise LoginPasswordError
        else:
            welcome(uname)