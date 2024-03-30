
class Admin(User):
    def __init__(self, id, name, access, admin):
        super().__init__(id, name, access)
        self.admin = admin

    def add_user(self):
        print(f"Add user: {self.name}")

    def remove_user(self):
        print(f"Remove user: {self.name}")


user1 = User(1, "John", "user")
user2 = User(2, "Jane", "user")
print(user1._User__private_access)