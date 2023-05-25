class register:
    def __init__(self, user, password):
        self.user = user
        self.password = password

def reg():
    user = register(input("What's your name: "), 123)
    return(user.user())

reg()

