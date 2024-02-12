import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Modulos":{
        "modulo":{
            "nombre":{
                "type":"string",
                "minLength": 1
            }, "contenidos":{
                "unDidactica":{
                "asignatura":{
                    "type":"string",
                    "minLength": 1
                }, "tipo":{
                    "type":"string",
                    "minLength": 1
                }, "descripcion":{
                    "type":"string",
                    "minLength": 1
                }
    }, "required":["asignatura", "tipo", "descripcion"]
}
}, "required":["nombre"]
}
}

# Archivo JSON a validar
archivo_json = '''
{
  "Modulos": {
    "modulo": [
      {
        "nombre": [
          "DAW"
        ],
        "contenidos": [
          {
            "unDidactica": [
              {
                "asignatura": [
                  "Lenguaje de Marcas"
                ],
                "tipo": [
                  "Informatica"
                ],
                "descripcion": [
                  "Profesor/a: Ana"
                ]
              },
              {
                "asignatura": [
                  "Entornos de Desarrollo"
                ],
                "tipo": [
                  "Informatica"
                ],
                "descripcion": [
                  "Profesor/a: Ana"
                ]
              },
              {
                "asignatura": [
                  "Base de Datos"
                ],
                "tipo": [
                  "Informatica"
                ],
                "descripcion": [
                  "Profesor/a: Juan Carlos"
                ]
              },
              {
                "asignatura": [
                  "Sistemas informáticos"
                ],
                "tipo": [
                  "Informatica"
                ],
                "descripcion": [
                  "Profesor/a: Juan Carlos"
                ]
              },
              {
                "asignatura": [
                  "Programacion"
                ],
                "tipo": [
                  "Informatica"
                ],
                "descripcion": [
                  "Profesor/a: Diego"
                ]
              },
              {
                "asignatura": [
                  "FOL"
                ],
                "tipo": [
                  "Informatica"
                ],
                "descripcion": [
                  "Profesor/a: Jorge"
                ]
              }
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