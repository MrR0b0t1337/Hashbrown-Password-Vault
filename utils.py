import math
import re

def calculate_entropy(password: str) -> float:
    if not password:
        return 0.0
    
    pool = 0
    if re.search(r'[a-z]', password):
        pool+= 26
    if re.search(r'[A-Z]', password):
        pool+= 26
    if re.search(r'[0-9]', password):
        pool += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool += 32
    
    if pool == 0:
        return 0.0
    
    return len(password) * math.log2(pool)


def get_strength_label(entropy: float) -> tuple[str, str]:
    if entropy < 40:
        return ("Weak", "#FF4444")
    elif entropy < 60:
        return ("Fair", "#FF8800")
    elif entropy < 80:
        return ("Strong", "#FFEA00")
    else:
        return ("Very Strong", "#04FF00")
    

def validate_password(password: str) -> list[str]:
    errors = []

    if len(password) < 12:
        errors.append("Password must contain at least 12 characters")
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter")
    if not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter")
    if not re.search(r'[0-9]', password):
        errors.append("Password must contain at least one number")
    if not re.search(r'[^a-zA-Z0-9]', password):
        errors.append("Password must contain at least one special character")

    return errors