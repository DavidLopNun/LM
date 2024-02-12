import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Alumnos":{
        "alumno":{
            "nombre":{
                "type":"string",
                "minLength": 1
            }, "apellido":{
                "type":"string",
                "minLength": 1
            }
            }, "required":["nombre", "apellido"]
    }
}

# Archivo JSON a validar
archivo_json = '''
{
    "Alumnos": {
      "alumno": [
        {
          "nombre": "Juan",
          "apellido": "Pérez"
        },
        {
          "nombre": "María",
          "apellido": "Gómez"
        },
        {
          "nombre": "Pedro",
          "apellido": "López"
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