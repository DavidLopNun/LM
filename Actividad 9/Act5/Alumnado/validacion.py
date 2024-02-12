import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Alumnado":{
        "Alumno":{
            "NIF":{
                "type":"string",
                "minLength": 1
            }, "resultado":{
                "type":"string",
                "minLength": 1
            }, "observaciones":{
                "type":"string",
                "minLength": 1
            }, "IP_MAC":{
                "type":"string",
                "minLength": 1
            }
            }, "required":["NIF", "resultado", "observaciones", "IP_MAC"]
    }
}

# Archivo JSON a validar
archivo_json = '''
{
  "Alumnado": {
    "Alumno": [
      {
        "NIF": [
          "77496750k"
        ],
        "resultado": [
          "Apto"
        ],
        "observaciones": [
          "Realiza buen proyecto"
        ],
        "IP_Mac": [
          "IP"
        ]
      },
      {
        "NIF": [
          "77496777k"
        ],
        "resultado": [
          "Apto"
        ],
        "observaciones": [
          ""
        ],
        "IP_Mac": [
          "MAC"
        ]
      },
      {
        "NIF": [
          "77496666k"
        ],
        "resultado": [
          "No apto"
        ],
        "observaciones": [
          "No realiza proyecto"
        ],
        "IP_Mac": [
          "IP"
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