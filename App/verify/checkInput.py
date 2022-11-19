import re

__all__ = ["checkInput"]

def checkInput(string):
  
  comandosProibidos = [
    "INSERT INTO", "CREATE DATABASE", "ALTER DATABASE",
    "CREATE TABLE", "ALTER TABLE", "DROP TABLE",
    "CREATE INDEX", "DROP INDEX", " OR "
  ]
  
  simbProibidos = [";" , "--"]

  detectSelect = re.compile("SELECT.*FROM", re.IGNORECASE)
  detectDelete = re.compile("DELETE.*FROM", re.IGNORECASE)
  detectUpdate = re.compile("UPDATE.*SET", re.IGNORECASE)

  selectMatches = re.findall(detectSelect, string)
  deleteMatches = re.findall(detectDelete, string)
  updateMatches = re.findall(detectUpdate, string)

  if (len(selectMatches) != 0 ) or (len(deleteMatches) != 0) or (len(updateMatches) != 0):
    return False
  
  for comando in comandosProibidos:
    if (comando in string) or (comando.lower() in string):
      return False

  for simbolo in simbProibidos:
    if simbolo in string:
      return False
    
  if "1=1" in string:
      return False

  if "'" in string[0]:
      return False

  return True
