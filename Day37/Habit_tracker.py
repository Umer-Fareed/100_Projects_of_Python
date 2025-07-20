import  requests

USER_NAME= "umer-fareed"
TOKEN= "asdfrq5jn234n234112"
pixela_endpoint= "https://pixe.la/v1/users"

user_params= {
    "token": TOKEN,
    "username": USER_NAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response= requests.post(url=pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config= {
    "id": "graph786",
    "name" : "Study Graph",
    "unit" : "minute",
    "type" : "int",
    "color" : "ajisai"
}

headers= {
    "X-USER-TOKEN": TOKEN
}
# response= requests.post(url=graph_endpoint,json=graph_config, headers= headers)
# print(response.text)


