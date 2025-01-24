from werkzeug.security import check_password_hash

def check_password(password, password_hash):
    # Check if the provided password matches the hashed password
    return check_password_hash(password_hash, password)
