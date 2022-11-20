from crypto import encrypt,decrypt


def test_encrypt_with_key():
	a = encrypt("aaa",'luM0UC4X6Jv4a-akn0dHwaO5uodRpUcg4-2c9TxPCXc=')
	assert decrypt(a[0],a[1]) == "aaa"

def test_encrypt_no_key():
	a = encrypt("aaa")
	assert decrypt(a[0],a[1]) == "aaa"

def test_decrypt():
	assert decrypt("gAAAAABjeTieAsFR6OmjmwlGwOXyMIGMbMWPA0CK3I9J2Skc_2GrcRx8JJGixjgmUKyu_uvdQLokPzaZdzeBAjFmb_uIW9wQuQ==","luM0UC4X6Jv4a-akn0dHwaO5uodRpUcg4-2c9TxPCXc=") == "aaa"