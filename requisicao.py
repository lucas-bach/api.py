import requests
import json

url = "https://app.omie.com.br/api/v1/geral/clientes/"

payload = json.dumps({
  "call": "ListarClientes",
  "app_key": "4291481375181",
  "app_secret": "9262924c11b3cab9114f953cbd8e7f64",
  "param": [
    {
      "pagina": 1,
      "registros_por_pagina": 50,
      "apenas_importado_api": "N"
    }
  ]
})
headers = {
  'Content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
