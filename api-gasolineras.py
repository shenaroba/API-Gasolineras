import requests
import json


def api_gasolineras():
    url="https://api.datos.gob.mx/v1/precio.gasolina.publico"
    response=requests.get(url)
    status_code=response.status_code
    print(status_code)
    if status_code== 200:
        content=response.content
        #print(content)
        file=open("C:/proyectos/API-Gasolineras/json1.json","wb")
        file.write(content)
        file.close()
        print("Se guardo el JSON")

        with open("C:/proyectos/API-Gasolineras/json1.json", encoding="utf8")as file:
            operacion1=json.load(file)
            operacion2=operacion1["pagination"]["page"]
            print(operacion2)
            for i in operacion1["results"]:
                dato=(i["razonsocial"])
                dato0=(i["_id"])
                dato1=(i["calle"])
                dato2=(i["regular"])
                dato3=(i["premium"])
                dato4=(i["dieasel"])

                

                Diccionario_1=[{
                    "razonsocial": dato,
                    "_id": dato0,
                    "calle": dato1,
                    "regular": dato2,
                    "premium": dato3,
                    "dieasel": dato4
                }]

                #print(Diccionario_1)
                print("_id: "+ dato0)
                print("razonsocial: "+ dato)
                print("calle: "+ dato1)
                print("regular: "+ dato2)
                print("premium: "+ dato3)
                print("dieasel: "+ dato4)


        ##Guardar diccionario json con datos trabajados en nuevo archivo, ( confirmar con danis.).
        #file=open("C:/proyectos/API-Gasolineras/Datos_Filtrados.json","wb") 
        #file.write(Diccionario_1)
        #file.close()
       # print("Se creo archivo de datos.")       

    else:
        print("No se pudo conectar a la API")

amadeo=api_gasolineras()