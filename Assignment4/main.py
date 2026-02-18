from datetime import datetime
from src.user import User
from src.user_service import UserService
from src.user_util import UserUtil

user_id = UserUtil.generate_user_id()
birthday = datetime(2000, 5, 15)

user = User(user_id, "John", "Doe", birthday)
user.email = UserUtil.generate_email("John", "Doe", "gmail.com")
user.password = UserUtil.generate_password()

UserService.add_user(user)

print(user.get_details())
print("Age:", user.get_age())
print("Total Users:", UserService.get_number())
