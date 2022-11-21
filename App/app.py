from service import getMessages, createMessage
from verify import checkInput, checkUsername
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

app.secret_key = b'\x11k\xe6M$\xb3\xe3\x0f}P\xc2('

temas_habilitados = ("todos", "Trabalho", "Meta", "Familia", "Faculdade")

@app.route("/", methods=['GET'])
def home():
	"""
	Show messages based on the filter chosen by the user. If this filter doesn't exist, it shows all messages.
	"""
	tema = request.args.get("tema")
	if tema in temas_habilitados:
		# se um tema correto foi passado, o usaremos para filtrar
		dados = getMessages(tema)
	else:
		# se nÃ£o houver um tema como parametro, baixamos todos
		dados = getMessages()
	return render_template('index.html', msgs = dados)


@app.route('/filtro', methods=['POST'])
def filter():
	"""
	Uses the filter chosen by the user to redirect him to the page of this filter.
	"""
	if request.method == 'POST':
		tema = request.form.get("tema")
		return redirect(f"/?tema={tema}")


@app.route('/msg', methods=["POST"])
def upload():
	"""
	Verify if message, user and theme are valids. If they are, store them on Firebase.
	"""
	if request.method == 'POST':
		tema = request.form.get("tema")
		msg = request.form.get("msg")
		user = request.form.get("user")
		userNameStatus = checkUsername("[^!@\|]{5,20}", user)
		print(f"{user}: {userNameStatus}")
		condition = checkInput(user) and checkInput(msg) and userNameStatus == 1
		if (condition): # verificando comandos SQL
			createMessage(user, msg, tema)
		elif userNameStatus == -1:
			flash(f"O nome de usuário deve ter de 5 e 20 caracteres. {user} é pequeno demais")
		elif userNameStatus == -2:
			flash(f"O nome de usuáriodeve ter de 5 e 20 caracteres. {user} é grande demais")
		elif userNameStatus == -3:
			flash(f"O nome de usuário não deve conter '!', '|' ou '@'. {user} possui algum desses caracteres.")
		elif userNameStatus == -4:
			flash(f"O nome de usuário {user} é inválido por um motivo desconhecido.")
	return redirect("/")

if __name__ == '__main__':
	app.debug = True
	app.run()
