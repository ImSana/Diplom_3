from faker import Faker


class CreateUser:
    @staticmethod
    def creat_user():
        fake = Faker()
        user = {"email": fake.email(),
                   "password": fake.password(),
                   "name": fake.user_name()}
        return user
