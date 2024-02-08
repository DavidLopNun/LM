import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "BDsms":{
        "sms":{
            "telefono":{
                "type":"string"
            }, "fecha":{
                "type":"string", "format":"date"
            }, "hora":{
                "type":"string"
            }, "mensaje":{
                "type":"string"
            }
            }, "required":["telefono", "fecha", "hora", "mensaje"]
    }
}

# Archivo JSON a validar
archivo_json = '''
{
    "BDsms": {
      "sms": [
        {
          "telefono": "955556555",
          "fecha": "1/7/2011",
          "hora": "23:55",
          "mensaje": "Juego 1: Tetris"
        },
        {
          "telefono": "745155611",
          "fecha": "22/9/2011",
          "hora": "15:05",
          "mensaje": "Juego 2: Arkanoid"
        },
        {
          "telefono": "842352200",
          "fecha": "10/11/2011",
          "hora": "09:22",
          "mensaje": "Juego 3: Comecocos"
        }
      ]
    }
  }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.