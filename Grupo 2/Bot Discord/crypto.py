from asyncio.windows_events import NULL
from cryptography.fernet import Fernet

def encrypt(TextInput, key = NULL):
	if key == NULL:
		key = Fernet.generate_key()
	f = Fernet(key)
	token = f.encrypt(bytes(TextInput, encoding='utf8'))
	
	a = [token.decode('utf-8'), key.decode('utf-8')]

	return a


def decrypt(Token, key):
	f = Fernet(key)
	return (f.decrypt(Token).decode('utf-8'))
