import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Productos":{
        "producto":{
            "nombre":{
                "type":"string"
            },"precio":{
                "type":"number"
            }, "disponible":{
                "type":"boolean"
            }, "detalles":{
                  "color":{
                    "type":"string"
                }, "talla":{
                    "type":"string"
                }
    }, "required":["color", "talla"]
}, "required":["nombre", "precio", "disponible"]
}
}

# Archivo JSON a validar
archivo_json = '''
{
  "Productos": {
    "producto": [
      {
        "nombre": [
          "Camiseta"
        ],
        "precio": [
          "19.99"
        ],
        "disponible": [
          "true"
        ],
        "detalles": [
          {
            "color": [
              "Rojo"
            ],
            "talla": [
              "M"
            ]
          }
        ]
      },
      {
        "nombre": [
          "Pantalón"
        ],
        "precio": [
          "29.99"
        ],
        "disponible": [
          "false"
        ],
        "detalles": [
          {
            "color": [
              "Azul"
            ],
            "talla": [
              "L"
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