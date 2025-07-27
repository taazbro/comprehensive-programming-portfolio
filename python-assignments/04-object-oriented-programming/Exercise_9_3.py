class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

eric = User('Tanjim', 'Ahmed', 'Ahmed1_t', 'ahmed_t@gmail.com', 'Ypsilanti')
eric.describe_user()
eric.greet_user()

willie = User('Fahad', 'Akond', 'Makon', 'makon@gmail.com', 'Ann Arbor')
willie.describe_user()
willie.greet_user()