from cryptography.fernet import Fernet

def encrypt(TextInput, key = None):
	if key == None:
		key = Fernet.generate_key()
	f = Fernet(key)
	token = f.encrypt(bytes(TextInput, encoding='utf8'))
	
	a = [token.decode('utf-8'), key.decode('utf-8')]

	return a


def decrypt(Token, key):
	f = Fernet(key)
	return (f.decrypt(Token).decode('utf-8'))
