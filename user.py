class User:
    num_users = 0
    
    def __init__(self, name = None, lastaname = None, rol= "user" , password = None):
        self._name = name
        self._lastname = lastaname
        self._rol = rol
        self._password = password

        User.num_users += 1
        
    def __str__(self):
        return  "Name: {}\nlastname: {}\nrol: {}\nPassword: {}".format(self._name, self._lastname, self._rol, self._password)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        return self.name
    
    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, lastname):
        return self.lastname
    
    @property
    def rol(self):
        return self._rol
    
    @rol.setter
    def rol(self, rol):
        return self.rol
    

if __name__ == "__main__":
    user1 = User(name='lian', lastaname='tudela', rol='admin', password="leandropicachu34")
    print(user1)