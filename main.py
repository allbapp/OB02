class User():
    def __init__(self, id, name, access):
        self.id = id
        self._name = name
        self._access = access  #приватный атрибут



    def get_access(self):
        return self._access
    def get_name(self):
        return self._name


    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, id, name, access, admin):
        super().__init__(id, name, access)
        self._admin = admin #приватный атрибут

    def add_user(self, user_list, name):
        user_list.append(name)
        print(f"Add user:")
        print(user_list)

    def remove_user(self, user_list, name):
        user_list.remove(name)
        print(f"Remove user: ")



users = []
admin = Admin(1, "John", "user", "admin")
user1 = User(2, "Jane", "user")
user2 = User(3, "Jack", "user")
user3 = User(4, "Jill", "user")

print(user1.get_name())
admin.add_user(users, "John")
admin.add_user(users, "Kate")