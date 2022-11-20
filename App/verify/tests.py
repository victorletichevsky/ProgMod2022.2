import unittest
from checkUsername import *
from checkInput import *

def test_input_ilegal_caractere(self):
  resultado_esperado = checkInput("""
Today i am going to hack this website
update Customers set ContactName='Juan';
""")
  self.assertEquals(resultado_esperado, False)

def test_input_ilegal_command_drop_table(self):
  resultado_esperado = checkInput("""
vou escrever um pouquinho de texto aqui sendo que ninguem
vai achar nada demais quando na verdade drop table criminosos
""")
  self.assertEquals(resultado_esperado, False)

def test_input_caractere_ilegal_double_dash(self):
  resultado_esperado = checkInput("""
vou comentar todo o sql que vem depois disso! --
""")
  self.assertEquals(resultado_esperado, False)

def test_input_ilegal_1_equal_1(self):
  resultado_esperado = checkInput("""
vou hackear 1=1 vcs hein
""")
  self.assertEquals(resultado_esperado, False)

def test_input_start_quote(self):
  resultado_esperado = checkInput("""'boa tarde. estou cobrando R$2000 para libertar vosso site""")
  self.assertEquals(resultado_esperado, False)

def test_input_ilegal_comand_select_from(self):
  resultado_esperado = checkInput("""
watch me as i inject some SQL
select * from customers_creditcards
""")
  self.assertEquals(resultado_esperado, False)

def test_input_caractere_invalido(self):
  resultado_esperado = checkInput("""
Today i am going to hack this website
update Customers set ContactName='Juan';
""")
  self.assertEquals(resultado_esperado, False)

def test_input_update_sozinho(self):
  resultado_esperado = checkInput("""
Every day of my life is trying to update my antivirus software
""")
  self.assertEquals(resultado_esperado, True)

def test_input_ilegal_comand_delete_from(self):
  resultado_esperado = checkInput("""
I was walking through a lonely road
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste'
""")
  self.assertEquals(resultado_esperado, False)
  
def test_input_delete_sozinha(self):
  resultado_esperado = checkInput("""
I was walking through a lonely road
and decided to every DELETE some bank apps
""")
  self.assertEquals(resultado_esperado, True)

def test_sucesso_com_restricao(self):
  resultado_esperado = checkUsername("[^!\|@]{1,10}", "eduardo29")
  self.assertEquals(resultado_esperado, 1)

def test_username_nao_atende_requisitos(self):
  resultado_esperado = checkUsername("pabllo@[^gh]mail.com", "vittin")
  self.assertEquals(resultado_esperado, -4)

def test_caracteres_ilegais_na_regex_e_tam_menor(self):
  resultado_esperado = checkUsername("[^@;!]{10,20}", "oMatador!")
  self.assertEquals(resultado_esperado, -1)

def test_caractere_ilegal(self):
  resultado_esperado = checkUsername("[^_-]{10,20}", "carlos-pilotto-94")
  self.assertEquals(resultado_esperado, -3)

def test_tam_maior_que_max(self):
  resultado_esperado = checkUsername(".{10,20}", "o_cabeca_de_motor_1922")
  self.assertEquals(resultado_esperado, -2)

def test_sem_restricao(self):
  resultado_esperado = checkUsername(".*", "Paulinho\t\nXDXD")
  self.assertEquals(resultado_esperado, 1)

def test_tamanho_menor_que_min(self):
  resultado_esperado = checkUsername(".{50,100}", "maureca_77")
  self.assertEquals(resultado_esperado, -1)

