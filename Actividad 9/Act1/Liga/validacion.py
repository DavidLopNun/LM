import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "liga":{
        "equipo":{
                "presidente":{
                "type":"string",
                "minLength": 1
            }, "nombre":{
                "type":"string",
                "minLength": 1
            }, "FechaFundacion":{
                "type":"string", "format":"date",
               "dia":{
               "type":"integer"
            }, "mes":{
               "type":"integer"
            }, "anio":{
               "type":"integer"
            }
}, "required":["presidente", "nombre", "dia", "mes", "anio"]
            }
        }
    }

# Archivo JSON a validar
archivo_json = '''
{
    "liga": {
      "equipo": [
        {
          "presidente": "Florentino Pérez",
          "nombre": "Real Madrid",
          "FechaFundacion": {
            "dia": 6,
            "mes": "Marzo",
            "anio": 1902
          }
        },
        {
          "presidente": "Joan Laporta",
          "nombre": "F.C. Barcelona",
          "FechaFundacion": {
            "dia": 29,
            "mes": "Noviembre",
            "anio": 1899
          }
        },
        {
          "presidente": "Enrique Cerezo",
          "nombre": "Atlético de Madrid",
          "FechaFundacion": {
            "dia": 26,
            "mes": "Abril",
            "anio": 1903
          }
        },
        {
          "presidente": "Ángel Haro",
          "nombre": "Real Betis",
          "FechaFundacion": {
            "dia": 12,
            "mes": "Septiembre",
            "anio": 1907
          }
        },
        {
          "presidente": "Jose Castro",
          "nombre": "Sevilla F.C.",
          "FechaFundacion": {
            "dia": 25,
            "mes": "Enero",
            "anio": 1890
          }
        },
        {
          "presidente": "Manuel Vizcaíno.",
          "nombre": "Cádiz C.F.",
          "FechaFundacion": {
            "dia": 3,
            "mes": "Junio",
            "anio": 1911
          }
        },
        {
          "presidente": "Jokin Aperribay",
          "nombre": "Real Sociedad",
          "FechaFundacion": {
            "dia": 7,
            "mes": "Septiembre",
            "anio": 1909
          }
        },
        {
          "presidente": "Carlos Mouriño",
          "nombre": "Celta de Vigo",
          "FechaFundacion": {
            "dia": 23,
            "mes": "Agosto",
            "anio": 1923
          }
        },
        {
          "presidente": "Aitor Elizegi",
          "nombre": "Athletic Club de Bilbao",
          "FechaFundacion": {
            "dia": "Desconocido",
            "mes": "Desconocido",
            "anio": 1898
          }
        },
        {
          "presidente": "Turki Al-Sheik",
          "nombre": "Unión Deportiva Álmería",
          "FechaFundacion": {
            "dia": 26,
            "mes": "Julio",
            "anio": 1989
          }
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