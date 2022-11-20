from .checkUsername import *
from .checkInput import *

def test_input_ilegal_caractere():
  resultado_esperado = checkInput("""
Today i am going to hack this website
update Customers set ContactName='Juan';
""")
  assert resultado_esperado == False

def test_input_ilegal_command_drop_table():
  resultado_esperado = checkInput("""
vou escrever um pouquinho de texto aqui sendo que ninguem
vai achar nada demais quando na verdade drop table criminosos
""")
  assert resultado_esperado == False

def test_input_caractere_ilegal_double_dash():
  resultado_esperado = checkInput("""
vou comentar todo o sql que vem depois disso! --
""")
  assert resultado_esperado == False

def test_input_ilegal_1_equal_1():
  resultado_esperado = checkInput("""
vou hackear 1=1 vcs hein
""")
  assert resultado_esperado == False

def test_input_start_quote():
  resultado_esperado = checkInput("""'boa tarde. estou cobrando R$2000 para libertar vosso site""")
  assert resultado_esperado == False

def test_input_ilegal_comand_select_from():
  resultado_esperado = checkInput("""
watch me as i inject some SQL
select * from customers_creditcards
""")
  assert resultado_esperado == False

def test_input_caractere_invalido():
  resultado_esperado = checkInput("""
Today i am going to hack this website
update Customers set ContactName='Juan';
""")
  assert resultado_esperado == False

def test_input_update_sozinho():
  resultado_esperado = checkInput("""
Every day of my life is trying to update my antivirus software
""")
  assert resultado_esperado == True

def test_input_ilegal_comand_delete_from():
  resultado_esperado = checkInput("""
I was walking through a lonely road
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste'
""")
  assert resultado_esperado == False
  
def test_input_delete_sozinha():
  resultado_esperado = checkInput("""
I was walking through a lonely road
and decided to every DELETE some bank apps
""")
  assert resultado_esperado == True

def test_sucesso_com_restricao():
  resultado_esperado = checkUsername("[^!\|@]{1,10}", "eduardo29")
  assert resultado_esperado == 1

def test_username_nao_atende_requisitos():
  resultado_esperado = checkUsername("pabllo@[^gh]mail.com", "vittin")
  assert resultado_esperado == -4

def test_caracteres_ilegais_na_regex_e_tam_menor():
  resultado_esperado = checkUsername("[^@;!]{10,20}", "oMatador!")
  assert resultado_esperado == -1

def test_caractere_ilegal():
  resultado_esperado = checkUsername("[^_-]{10,20}", "carlos-pilotto-94")
  assert resultado_esperado == -3

def test_tam_maior_que_max():
  resultado_esperado = checkUsername(".{10,20}", "o_cabeca_de_motor_1922")
  assert resultado_esperado == -2

def test_sem_restricao():
  resultado_esperado = checkUsername(".*", "Paulinho\t\nXDXD")
  assert resultado_esperado == 1

def test_tamanho_menor_que_min():
  resultado_esperado = checkUsername(".{50,100}", "maureca_77")
  assert resultado_esperado == -1



