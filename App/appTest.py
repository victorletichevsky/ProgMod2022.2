from app import app

def test_home_page():
    
    try:
        response = app.test_client().get("/")
        assert response.status_code == 200
        print('ROTA INICIAL PASSOU NO TESTE!')
    except:
        print('ROTA INICIAL FALHOU NO TESTE!')


test_home_page()