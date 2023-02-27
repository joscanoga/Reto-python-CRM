from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from api.models import CVE
import json


# Create your views here.

class VistaCVE(View):
    # skip CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        #en caso de que algun parametro reciba un valor no adecuado tomara el valor por defecto

        # parametro que define el numero de CVEs enviados en la peticion por defecto tiene el valor de 10 mil
        CVEPorPagina = request.GET.get("cve_por_pagina")
        CVEPorPagina = 10000 if CVEPorPagina is None or not (CVEPorPagina.isnumeric()) else int(CVEPorPagina)


        # parametro que define el indice inicial aparttir del cual se obtentran las peticiones por defecto tiene el valor de 0
        indiceInicial = request.GET.get("indice_inicial")
        indiceInicial = 0 if indiceInicial is None or not (indiceInicial.isnumeric()) else int(indiceInicial)


        # en caso de ser 1 regresa toda la lista de CVEs, ignorando los parametros indice_inicial y cve_por_pagina,
        # poco recomendable dado que por el tamaño pueden resultar errores valor por defecto 0
        todas = request.GET.get("todas")
        todas = 0 if todas is None or todas!="1" else 1


        # en caso de ser 1 regresa toda la lista de CVEs solucionados, en caso de 0 devuelve solo los que no han sido solucionados, y en cualquier otro caso devuelve todas
        # todo esto  dentro de los limites del indice_inicial y cve_por_pagina valor por defecto 0
        solucionadas = request.GET.get("solucionadas")
        solucionadas = -1 if (solucionadas is None or not (solucionadas.isnumeric())) else int(solucionadas)

        if solucionadas==1:
            cve=list(CVE.objects.filter(solucionado=True).values())
        elif solucionadas==0:
            cve = list(CVE.objects.filter(solucionado=False).values())
        else:
            cve = list(CVE.objects.values())

        if (todas != 1):
            cve = cve[indiceInicial:indiceInicial + CVEPorPagina]

        if len(cve) > 0:
            datos = {"msg": "sucess", "CVEs": cve}
        else:
            datos = {"msg": "sucess", "CVEs": "not found"}
        return JsonResponse(datos)

    def post(self, request):
        datos = json.loads(request.body)["ids"]
        resultados = {}
        for id in datos:
            cve = list(CVE.objects.filter(id=id).values())

            if len(cve) > 0:
                cve = CVE.objects.get(id=id)
                cve.solucionado = True
                cve.save()
                resultados[id] = "sucess"
            else:
                resultados[id] = "not found"

        return JsonResponse({"datos": resultados})

class Vistasumarizada(View):

    def get(self,request):
        cve = list(CVE.objects.values())
        df=pd.DataFrame(cve)
        df.drop(['id',"descripcion"], axis=1,inplace=True)
        #df.to_json(orient = 'columns')
        severidades=df["severidad"].unique()
        datos={}
        for i in severidades:
            datos[i]=json.loads(df[df["severidad"]==i].drop(['severidad',"publicado","ultimaModificacion"], axis=1).describe().to_json(orient = 'columns'))

        #low=json.loads(df.describe().to_json(orient = 'columns'))

        return JsonResponse({"datos": datos})