

class UserProfile(object):
    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.number = None
    
    def setUserProfile(self, uname, pword, email, number):
        self.username = uname
        self.password = pword
        self.email = email
        self.number = number
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def getEmail(self):
        return self.email
    
    def getNumber(self):
        return self.number