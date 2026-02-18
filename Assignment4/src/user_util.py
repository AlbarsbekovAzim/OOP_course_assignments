from datetime import datetime
import random
import string
import re


class UserUtil:

    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.now().year)[-2:]
        random_digits = ''.join(random.choices(string.digits, k=7))
        return int(year_prefix + random_digits)

    @staticmethod
    def generate_password():
        while True:
            password = ''.join(random.choices(
                string.ascii_letters + string.digits + "!@#$%^&*()",
                k=10
            ))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*()]", password):
            return False
        return True

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$"
        return re.match(pattern, email) is not None
