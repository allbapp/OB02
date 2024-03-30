class User():
    def __init__(self, id, name, access):
        self.id = id
        self.name = name
        self.__private_access = access  #приватный атрибут



    def get_private(self):
        return self.__private_access

    def set_private(self, value):
        self.__private_access = value



class Admin(User):
    def __init__(self, id, name, access, admin):
        super().__init__(id, name, access)
        self.__private_admin = admin #приватный атрибут

        def get_private(self):
            return self.__private_admin

        def set_private(self, value):
            self.__private_admin = value

    def add_user(self):
        print(f"Add user: {self.name}")

    def remove_user(self):
        print(f"Remove user: {self.name}")

    def test_private(self):
        self.__private_add_user()

    def test_private(self):
        self.__private_remove_user()



user1 = User(1, "John", "user")
user2 = User(2, "Jane", "user")
user3 = Admin(3, "Bob", "user", "admin")
user4 = User(4, "Kate", "user")
user5 = Admin(5, "Alex", "user", "admin")



user3.add_user()
user5.remove_user()
user5.add_user()

print(user1.get_private())
print(user2.get_private())
print(user3.get_private())
print(user4.get_private())
print(user5.get_private())


