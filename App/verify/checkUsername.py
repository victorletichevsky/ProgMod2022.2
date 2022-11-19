import re

__all__ = ["checkUsername", "removeCaret"]

def checkUsername(regex, username):
  
  extremes = minMax(regex)
  if extremes != -1: #se extremes = -1, n houve definicao de tamanho
    minlen = extremes[0]
    maxlen = extremes[1]
    # username digitado é menor que o tamanho mínimo
    if len(username) < minlen:
      return -1
    # username digitado é maior que o tamanho máximo
    if len(username) > maxlen:
      return -2

  #se identificarmos que um caractere expressamente definido como ilegal
  #na verdade foi utilizado no username, retornamos -3
  if findIllegalCharacter(regex, username) != None:
    return -3
  
  padrao = re.search(regex, username)
  # username digitado não atende aos requisitos da expressão regular, de modo mais generalizado
  if not padrao:
    return -4
  # username válido
  return 1

  
# Pipeline de verificacao de caracteres proibidos
def removeCaret(regex): #o caret ('^') eh o caracter que representa a negacao
  if "^" in regex:
    return regex.replace("^","")

def getAllRestrictions(regex):
  ###recebe a regex do usuario e encontra "subregexes" que se adequem ao modelo de restricao
  restriction = "\[\^.*?\]"
  restrictionRegex = re.compile(restriction, re.DOTALL)
  allRestrictions = re.findall(restrictionRegex, regex)
  if allRestrictions != None:
    return allRestrictions
  else:
    return []

def findIllegalCharacter(regex, username):
  restrictions = getAllRestrictions(regex)
  illegality = ""
  #antirestrictions sao as regexes de restricoes, mas sem o caret
  #ou seja, se houve algum desrespeito a restricao, a antirestriction encontra
  #justamente o que desrespeitou a restricao
  for pattern in restrictions:
    illegality = re.search(removeCaret(pattern), username)
    if illegality != None:
      return illegality
  return None

  
# Pipeline de verificacao do tamanho do username
def getLength(tamanhos):
  tamanhos = tamanhos.strip("{")
  tamanhos = tamanhos.strip("}")
  tamanhos = tamanhos.split(",")
  # transforma cada elemento da array de string em inteiro
  tamanhos = [int(numeric_string) for numeric_string in tamanhos]
  return tamanhos


def getCharLimitCases(username):
  charLimit = re.compile("[{][1-9][0-9]*,[1-9][0-9]*[}]")
  charCases = re.findall(charLimit, username)
  return charCases


def getExtremes(tamanhos):
  tamanhosOrdenado = sorted(tamanhos, key=lambda tamanho: tamanho[1])
  return tamanhosOrdenado[-1]

def minMax(regex):
  regexTamanhos = getCharLimitCases(regex)
  if len(regexTamanhos) != 0:
    tamanhos = [getLength(regexTamanho) for regexTamanho in regexTamanhos]
    return getExtremes(tamanhos)
  else:
    return -1

