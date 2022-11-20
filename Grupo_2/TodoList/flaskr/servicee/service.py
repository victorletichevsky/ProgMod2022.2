import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("flaskr/servicee/progmodgrupo4-29067-firebase-adminsdk-3yozx-954637da7d.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
messageRef = db.collection('afazeres')

def createMessage(user, message, theme):
    try:
        messageRef.add({
            "user": user,
            "message": message,
            "theme": theme
        })
        return
    except:
        print("Erro criando item")
        return 

def getMessages(filter = "Todos"):
	messageList = list()
	try:
		allMessages = messageRef.get()
		if (filter == "Todos"):
			for currentMessage in allMessages:
				messageList.append(currentMessage.to_dict())
			return messageList
		else:
			messageList = messageFilter(filter)
			return messageList
	except:
		print("Erro ao baixar itens")
		return

def messageFilter(filter):
    filteredMessageList = list()
    try:
        allMessages = messageRef.get()
        for currentMessage in allMessages:
            if (currentMessage.get("theme") == filter):
                filteredMessageList.append(currentMessage.to_dict())
        return filteredMessageList
    except:
        print("Error filtrando itens")
        return 
        
def helloworld():
    return 'hello world'
