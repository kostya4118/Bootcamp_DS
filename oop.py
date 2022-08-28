class User:
    count = 0
    __login = 'login'
    __password = 'password'

    def __init__(self, name, login, password):
        self.name = name
        self.__login = login
        self.__password = password
        User.count += 1

    def my_name(self):
        print(self.name)

    def change_name(self, new_name):
        self.name = new_name
        print('Имя изменено на ' + self.name)

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return f'Пароль посмотреть нельззя!'
    @password.setter
    def password(self, new_pass):
        self.__password = new_pass

    def show_info(self):
        print(f'Name & login: {self.name}, {self.login}')


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role='moderator'):
        super().__init__(name, login, password)
        self.role = role
        SuperUser.count += 1

    def my_role(self):
        print(self.role)

    def change_role(self, new_role):
        self.role = new_role
        print('Роль изменена на ' + self.role)

    def show_info(self):
        print(f'Name & login & role: {self.name}, {self.login}, {self.role}')


user = User('paul_ggg', 'paul', '1234')
user2 = SuperUser('paul_iyheg', 'paulus', '1234')
user3 = SuperUser('paul_iyheg', 'paulus', '1234')

user.my_name()
user.change_name('Victor')
user.my_name()
print(user.password)

user2.password = 'ggggggggg'
user3.show_info()
user3.change_role('admin')
user3.my_role()

print(User.count, SuperUser.count)