import requests
import time
import sqlite3
from datetime import datetime

#clase desde la cual se haran consultas a la api desde donde se traeran la vulnerabilidades
class Cliente:
    """cliente desde donde salen las peticiones a la api"""
    def __init__(self,url="https://services.nvd.nist.gov/rest/json/cves/2.0/"):
        """constructor del cliente api"""
        self.con=sqlite3.connect("../db.sqlite3")
        self.cursor=cur = self.con.cursor()
        self.base = url

    def convertirFecha(self, fecha):
        """funcion para dar formato a una fecha"""
        fecha=datetime.strptime(fecha,"%Y-%m-%dT%H:%M:%S.%f")

        return fecha

    def guardarRegistro(self,id,severidad,publicado,editado,descripcion,estado):
        """funcion para guardar una vulnerabilidad en la base de datos"""
        consulta ='INSERT INTO api_cve  VALUES ("{}",{},"{}","{}","{}","{}","{}")'.format(id,False,self.convertirFecha(publicado),self.convertirFecha(editado),descripcion,severidad,estado)
        #print(consulta)
        self.cursor.execute(consulta)









    #funcion para llenar la tabla de cve desde cero
    #se haran multiples consultas a la api para traer
    def llenarTabla(self):
        """Funcion para llenar la tabla de vulnerabilidades"""

        incremento=2000
        total= requests.get(self.base+"?resultsPerPage={}&startIndex={}".format(1,1)).json()["totalResults"]
        indice=len(self.cursor.execute('SELECT * FROM api_cve ').fetchall())

        contador=0
        while(indice<total):
            url=self.base+"?resultsPerPage={}&startIndex={}".format(incremento,indice)
            #print(url)
            datos = requests.get(url)
            print(len(self.cursor.execute("SELECT * FROM api_cve").fetchall()))
            if datos.status_code!=200:
                time.sleep(30)
                continue
            else:
                for i in datos.json()['vulnerabilities']:
                    dato=i["cve"]
                    if "cvssMetricV2" in dato["metrics"]:
                        severidad=dato["metrics"]["cvssMetricV2"][0]["baseSeverity"]
                    else:
                        severidad=str(None)

                    self.guardarRegistro(dato["id"],severidad,dato["published"],dato["lastModified"],str(dato["descriptions"][0]["value"]).replace('"',"'"),dato["vulnStatus"])

                self.con.commit()

            #total = int(datos["totalResults"])


            indice +=incremento
            print(str(indice)+"/"+str(total))


if __name__ == "__main__":

    c= Cliente( )
    c.llenarTabla()