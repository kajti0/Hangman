import bcrypt


class PasswordHelper:
    def generate_hash(self, password):
        bytes_pass = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(bytes_pass, salt)

    def check_password(self, userpassword, hash_pass):
        return bcrypt.checkpw(userpassword.encode('utf-8'), hash_pass.encode('utf-8'))