# Objective-Key-Results (OKRs) registration project
---
This is a Django project for creating OKRs.


---


## Testing the endpoints:
  
Listing all OKRS: 
```console
curl --location --request GET 'http://127.0.0.1:8000/register/okr-list/'
```
  
Listing all Integrantes:
```console
curl --location --request GET 'http://127.0.0.1:8000/register/okr-integrantes/'
```
  
GET a single OKR:
```console
curl --location --request GET 'http://127.0.0.1:8000/register/okr-list/1'
```
  
POST a new OKR:
```console
curl --location --request POST 'http://127.0.0.1:8000/register/okr-list/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "integrante": 1,
    "objetivo": "Aprender Django-Rest-Framework",
    "resultado_1": "Conhecer o framework",
    "resultado_2": "Praticar REST",
    "resultado_3": "Testar funcionalidades novas",
    "resultado_4": "Entender o principio Request-Response",
    "resultado_5": "Entender APIs RESTFUL"
}'
```
  