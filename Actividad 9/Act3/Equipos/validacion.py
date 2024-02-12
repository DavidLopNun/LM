import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Equipos":{
        "equipo":{
            "colorEquipacion":{
                "type":"string",
                "minLength": 1
            }, "marcaEquipacion":{
                "type":"string",
                "minLength": 1
            }, "posicion":{
                "type":"integer"
            }, "entrenador":{
                "type":"string",
                "minLength": 1
            }, "presidente":{
                "type":"string",
                "minLength": 1
            }, "required":["colorEquipacion", "marcaEquipacion", "posicion", "entrenador", "presidente"]
    }
}
}

# Archivo JSON a validar
archivo_json = '''
{
    "Equipos": {
      "equipo": [
        {
          "colorEquipacion": "Blanca ",
          "marcaEquipacion": "Adidas",
          "posicion": "2",
          "entrenador": "Ancelotti",
          "presidente": "Florentino"
        },
        {
          "colorEquipacion": "Blaugrana ",
          "marcaEquipacion": "Nike",
          "posicion": "4",
          "entrenador": "Xavi",
          "presidente": "Laporta"
        },
        {
          "colorEquipacion": "Verde y blanca ",
          "marcaEquipacion": "Hummel",
          "posicion": "7",
          "entrenador": "Pellegrini",
          "presidente": "Haro"
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