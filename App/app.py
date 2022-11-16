from service import getMessages, createMessage
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


temas_habilitados = ("todos", "Trabalho", "Meta", "Familia", "Faculdade")

@app.route("/", methods=['GET'])
def home():
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
	if request.method == 'POST':
		tema = request.form.get("tema")
		return redirect(f"/?tema={tema}")


@app.route('/msg', methods=["POST"])
def upload():
	if request.method == 'POST':
		tema = request.form.get("tema")
		msg = request.form.get("msg")
		user = "teste"
		createMessage(user, msg, tema)
	return redirect("/")

if __name__ == '__main__':
	app.debug = True
	#app.run()
