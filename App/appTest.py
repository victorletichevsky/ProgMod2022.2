from app import app
import unittest
import json

class FlaskTest(unittest.TestCase):

    # check response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_theme_todos(self):
        tester = app.test_client(self)
        response = tester.get('/?tema=Todos')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    def test_theme_trabalho(self):
        tester = app.test_client(self)
        response = tester.get('/?tema=Trabalho')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_theme_faculdade(self):
        tester = app.test_client(self)
        response = tester.get('/?tema=Faculdade')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_theme_meta(self):
        tester = app.test_client(self)
        response = tester.get('/?tema=Meta')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_theme_familia(self):
        tester = app.test_client(self)
        response = tester.get('/?tema=Familia')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_theme_not_specified(self):
        tester = app.test_client(self)
        response = tester.get('/?tema=other')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_post_ok(self):
        tester = app.test_client(self)
        response = tester.post('/msg', data={"tema": "Trabalho", "msg": "Amo meu trabalho!", "user": "test_user"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)
    
    def test_post_empty(self):
        tester = app.test_client(self)
        response = tester.post('/msg', data={})
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

    def test_post_incomplete(self):
        tester = app.test_client(self)
        response = tester.post('/msg', data={"tema": "Trabalho", "msg": "Amo meu trabalho!"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)
    
    def test_filter_ok(self):
        tester = app.test_client(self)
        response = tester.post('/filtro', data={"tema": "Trabalho"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

    def test_filter_not_ok(self):
        tester = app.test_client(self)
        response = tester.post('/filtro', data={"tema": "other"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

    def test_filter_empty(self):
        tester = app.test_client(self)
        response = tester.post('/filtro', data={})
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

if __name__ == "__main__":
    unittest.main()

