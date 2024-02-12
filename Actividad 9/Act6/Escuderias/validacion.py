import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Escuderias":{
        "escuderia":{
            "nombre":{
                "type":"string",
                "minLength": 1
            }, "jefe":{
                "nombreJ":{
                    "type":"string",
                    "minLength": 1
                }, "edad":{
                    "type":"integer"
                }
    }, "required":["nombreJ", "edad"]
}, "required":["nombre"]
}
}

# Archivo JSON a validar
archivo_json = '''
{
  "Escuderias": {
    "escuderia": [
      {
        "nombreE": [
          "Ferrari"
        ],
        "jefe": [
          {
            "nombreJ": [
              "Fred Vasseur"
            ],
            "edad": [
              "54"
            ]
          }
        ]
      },
      {
        "nombreE": [
          "Red Bull"
        ],
        "jefe": [
          {
            "nombreJ": [
              "Christian Horner"
            ],
            "edad": [
              "50"
            ]
          }
        ]
      },
      {
        "nombreE": [
          "Mercedes"
        ],
        "jefe": [
          {
            "nombreJ": [
              "Toto Wolff"
            ],
            "edad": [
              "52"
            ]
          }
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