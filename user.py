class User:
    num_users = 0
    
    def __init__(self, name = None, lastaname = None, rol= "user" , password = None, ci = None):
        self._name = name
        self._lastname = lastaname
        self._rol = rol
        self._password = password
        self._ci = ci

        User.num_users += 1
        
    def __str__(self):
        return  "Name: {}\nlastname: {}\nrol: {}\nPassword: {}\nci: {}".format(self._name, self._lastname, self._rol, self._password, self._ci)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        return self._name
    
    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, lastname):
        return self._lastname
    
    @property
    def rol(self):
        return self._rol
    
    @rol.setter
    def rol(self, rol):
        return self._rol

    @property
    def ci(self):
        return self._ci
    
    @ci.setter
    def ci(self, ci):
        return self._ci

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        return self._password
    

if __name__ == "__main__":
    user1 = User(name='lian', lastaname='tudela', rol='admin', password="leandropicachu34", ci="9904322")
    print(user1)
    print(user1.password)