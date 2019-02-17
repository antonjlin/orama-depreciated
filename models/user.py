from passlib.hash import pbkdf2_sha256



class User:
    def __init__(self,email,password,faceHash):
        self.email = email
        self.password = password
        self.faceHash = faceHash




        