import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("progmodgrupo4-29067-firebase-adminsdk-3yozx-954637da7d.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def adicionaItem(user, message, theme):
    try:
        messagesRef.add({
            "user": user,
            "message": message,
            "theme": theme
        })
        return
    except:
        print("Erro criando mensagem")
        return 

def baixaItem(filter = "todos"):
	messageList = list()
	try:
		allMessages = messagesRef.get()
		if (filter == "todos"):
			for currentMessage in allMessages:
				messageList.append(currentMessage.to_dict())
			return messageList
		else:
			messageList = get_tema(filter)
			return messageList
	except:
		print("Erro ao baixar itens")
		return

def get_tema(filter):
    filteredMessageList = list()
    try:
        messages = messagesRef.get()
        for currentMessage in messages:
            if (currentMessage.get("theme") == filter):
                filteredMessageList.append(currentMessage.to_dict())
        return filteredMessageList
    except:
        print("Error filtrando mensagens")
        return 

messagesRef = db.collection('messages')
# filter = "Trabalho"
#filtraMensagem = print(get_tema("Trabalho"))
# teste = adicionaItem("Paulo", "teste meta", "Meta")