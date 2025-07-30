import secrets

def generate_jwt_secret_key():
    return secrets.token_hex(32)

if __name__ == '__main__':
    jwt_secret_key = generate_jwt_secret_key()
    print("Generated JWT Secret Key:", jwt_secret_key)
