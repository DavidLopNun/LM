import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Plantilla":{
        "Jugador":{
            "nombre":{
                "type":"string",
                "minLength": 1
            }, "edad":{
                "type":"string",
                "minLength": 1
            }, "exEquipo":{
                "type":"string",
                "minLength": 1
            }, "required":["nombre", "edad", "exEquipo"]
    }
}
}

# Archivo JSON a validar
archivo_json = '''
{
  "Plantilla": {
    "Jugador": [
      {
        "nombre": [
          "Isco"
        ],
        "edad": [
          "31"
        ],
        "exEquipo": [
          "Sevilla"
        ]
      },
      {
        "nombre": [
          "Fekir"
        ],
        "edad": [
          "30"
        ],
        "exEquipo": [
          "O. Lyon"
        ]
      },
      {
        "nombre": [
          "Guido"
        ],
        "edad": [
          "29"
        ],
        "exEquipo": [
          "America"
        ]
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