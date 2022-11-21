from service import getMessages, createMessage, messageFilter, db

from firebase_admin import firestore

messageTestRef = db.collection('messagesTest')

def delete_collection(coll_ref, batch_size: int):
    '''
    Delete a specific number of items in a database.
    
    Parameters
    ----------
        messageTestRef : list
            Is the list of dictonarys with DB data
        batch_size : int
            Is the quantity of elements you want to exclude
    '''
    docs = coll_ref.list_documents(page_size = batch_size)
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.get().to_dict()}')
        doc.delete()
        deleted = deleted + 1

    if (deleted >= batch_size):
        return delete_collection(coll_ref, batch_size)
    
def test_createMessageTest():
    '''
    In this test we want to test the creation of elements in the data base.
    '''
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
    '''
    In this test we want to test the lenghth of all messages in the DB.
    '''
    allmessagesTest = getMessages(docRef = messageTestRef)
    assert len(allmessagesTest) == 4

def test_getMessagesWithFilter():
    '''
    In this test we want to test the Filter tho topics of DB, we expect return 1 every time since we only put 4 elements in it.
    '''
    trabalho = messageFilter(filter = "Trabalho", docRef = messageTestRef)
    assert len(trabalho) == 1
    faculdade = messageFilter(filter = "Faculdade", docRef = messageTestRef)
    assert len(faculdade) == 1
    meta = messageFilter(filter = "Meta", docRef = messageTestRef)
    assert len(meta) == 1
    familia = messageFilter(filter = "Familia", docRef = messageTestRef)
    assert len(familia) == 1 

