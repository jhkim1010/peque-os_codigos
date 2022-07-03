import requests

# get pedido (venta online)
payload = {'name': 'marcos_kim', 'job': 'director UBF BsAs'}
# r = requests.get("http://ecommerce.coolsistema.com/api/erp/order", params = payload)
# r = requests.get("http://ecommerce.coolsistema.com/api/erp/product/krencia/80530726")
r = requests.post("http://reqres.in/api/user", json = payload)
print(r.text)