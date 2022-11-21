import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("App/progmodgrupo4-29067-firebase-adminsdk-3yozx-954637da7d.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
messageRef = db.collection('messages')

def createMessage(user, message, theme, docRef = messageRef):
    '''
    Creates a new message and send it to firebase.
    
    Parameters
    ----------
        user : str
            Is the person who writes the message
        message : str
            Is the text in the message
        theme : str
            Is the topic of the message
        docRef : Any, optional
           the document reference
    '''
    try:
        docRef.add({
            "user": user,
            "message": message,
            "theme": theme
        })
        return 1
    except:
        print("Erro criando item")
        return 0

def getMessages(filter = "Todos", docRef = messageRef):
    ''' 
    Gets the messages from firebase and return a list of messages.
    
    Parameters
    ----------
    filter : str, optional
           theme of the messages (default is "Todos")
    docRef : Any, optional
           the document reference
    Returns
    -------
    list
        A list of messages
    '''
    messageList = list()
    try:
        allMessages = docRef.get()
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

def messageFilter(filter, docRef = messageRef):
    '''
    Gets the messages from firebase, filter them and return a list of filtered messages.
    
    Parameters
    ----------
    filter : str
           theme of the messages
    docRef : Any, optional
           the document reference
    Returns
    -------
    list
        A list of filtered messages
    '''
    filteredMessageList = list()
    try:
        allMessages = docRef.get()
        for currentMessage in allMessages:
            if (currentMessage.get("theme") == filter):
                filteredMessageList.append(currentMessage.to_dict())
        return filteredMessageList
    except:
        print("Error filtrando itens")
        return 

