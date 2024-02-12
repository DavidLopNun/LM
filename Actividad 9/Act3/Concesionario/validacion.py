import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Concesionario":{
        "coche":{
            "codCoche":{
                "type":"string",
                "minLength": 1
            }, "marca":{
                "type":"string",
                "minLength": 1
            }, "modelo":{
                "type":"string",
                "minLength": 1
            }, "matricula":{
                "type":"string",
                "minLength": 1
            }, "potencia":{
                "caballos":{
                    "type":"integer"
                }
            },"required":["codCoche", "marca", "modelo", "caballos"] 
            ,"plazas":{
                "type":"integer"
            }, "numPuertas":{
                "type":"integer"
            }
            }, "required":["plazas", "numPuertas"]
    }
}

# Archivo JSON a validar
archivo_json = '''
{
    "Concesionario": {
      "coche": [
        {
          "codCoche": "1",
          "marca": "mercedes",
          "modelo": "G",
          "matricula": "9421 GMT",
          "potencia": {
            "caballos": "170"
          },
          "plazas": "5",
          "numPuertas": "5"
        },
        {
          "codCoche": "2",
          "marca": "peugeot",
          "modelo": "307",
          "matricula": "9444 GLT",
          "potencia": {
            "caballos": "136"
          },
          "plazas": "5",
          "numPuertas": "5"
        },
        {
          "codCoche": "3",
          "marca": "audi",
          "modelo": "Q3",
          "matricula": "9421 FFF",
          "potencia": {
            "caballos": "150"
          },
          "plazas": "5",
          "numPuertas": "5"
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