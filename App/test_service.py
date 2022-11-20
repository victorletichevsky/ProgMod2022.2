from service import getMessages, createMessage, messageFilter, db

from firebase_admin import firestore

messageTestRef = db.collection('messagesTest')

def delete_collection(coll_ref, batch_size):
    docs = coll_ref.list_documents(page_size=batch_size)
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.get().to_dict()}')
        doc.delete()
        deleted = deleted + 1

    if (deleted >= batch_size):
        return delete_collection(coll_ref, batch_size)
    
def test_createMessageTest():
    delete_collection(messageTestRef, 4)
    testTrabalho = createMessage("teste", "messagem de teste Trabalho", "Trabalho", messageTestRef)
    assert testTrabalho == 1
    testFamilia = createMessage("teste", "messagem de teste Familia", "Familia", messageTestRef)
    assert testFamilia == 1
    testMeta = createMessage("teste", "messagem de teste Meta", "Meta", messageTestRef)
    assert testMeta == 1
    testFaculdade = createMessage("teste", "messagem de teste Faculdade", "Faculdade", messageTestRef)
    assert testFaculdade == 1
    
    

def test_getMessagesTest():
    allmessagesTest = getMessages(docRef = messageTestRef)
    assert len(allmessagesTest) == 4

def test_getMessagesWithFilter():
    trabalho = messageFilter(filter = "Trabalho", docRef = messageTestRef)
    assert len(trabalho) == 1
    faculdade = messageFilter(filter = "Faculdade", docRef = messageTestRef)
    assert len(faculdade) == 1
    meta = messageFilter(filter = "Meta", docRef = messageTestRef)
    assert len(meta) == 1
    familia = messageFilter(filter = "Familia", docRef = messageTestRef)
    assert len(familia) == 1 

