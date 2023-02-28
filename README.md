# Project: Reto python crm
    

Api rest desarollada en django framework, utilisando una base de datos sqlite 3, se desarollo con la finalidad de llevar un control de las vulnerabilidades obtenidas en la api(https://services.nvd.nist.gov/rest/json/cves/2.0) con el fin de saber cuales vulnerabilidades han sido corregidas en nuestro sistema y caules no.


## REQUISITOS


1.   docker 
2.   Docker compose

## INSTALACIÓN 
En la carpeta raiz del projecto(Reto-python-CRM) ejecutar por terminal el siguiente comando


```
Docker compose up -d --build
```


## End-point: obtener vulnerabilidades
Endpoint GET que devuelve el listado total de las vulnerabilidades.  
Dado que no es posible traer las mas de 200mil vulneravilidades de una sola peticion, se tendran que hacer varias peticiones ajustando parametros opcionales en la ruta.

Parametros:

- cve_por_pagina :
    

recibe un numero entero, que coresponde al numero de vulnerabilidades por peticion, este parametro es opcional y tiene como valor por defecto 10000.

- indice_inicial
    

recibe un numero entero, que coresponde al indice desde cual se enviaran la cantidad de vunerabilidades de acuerdo a la peticion, este parametro es opcional y tiene como valor por defecto 0.

- todas:
    

recibe el valor 1 para devolver todas las vulnerabilidades ignorando los parametros cve_por_pagina y indice_inicial, en caso de cualquier otro valor esta parametro se ignorara.

- solucionadas:
    

en caso de recibir el vvalor de 1 devuelve unicamente aquellas vulnerabilidades que han sido solicionadas en el sistema, en caso de recibir 0, devolvera solo las que no han sido solucio en el sistema, y en caso de cualquier otro valor devolvera indiscriminadamente las vulnerabilidades.

en cao de no encontar ninguna vulnerabilidad que se adecue a los parametros devolvera no found
### End-point: obtener vulnerabilidades ejemplo 1
### Method: GET
>```
>http://127.0.0.1:8000/api?cve_por_pagina=10
>```
### Query Params

|Param|value|
|---|---|
|cve_por_pagina|10|
|||
### Response: 200

```json
{
    "msg": "sucess",
    "CVEs": [
        {
            "id": "CVE-1999-0095",
            "solucionado": true,
            "publicado": "1988-10-01T04:00:00Z",
            "ultimaModificacion": "2019-06-11T20:29:00.263Z",
            "descripcion": "The debug command in Sendmail is enabled, allowing attackers to execute commands as root.",
            "severidad": "HIGH",
            "estado": "Modified"
        },
        {
            "id": "CVE-1999-0082",
            "solucionado": true,
            "publicado": "1988-11-11T05:00:00Z",
            "ultimaModificacion": "2008-09-09T12:33:40.853Z",
            "descripcion": "CWD ~root command in ftpd allows root access.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1471",
            "solucionado": true,
            "publicado": "1989-01-01T05:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:36.257Z",
            "descripcion": "Buffer overflow in passwd in BSD based operating systems 4.3 and earlier allows local users to gain root privileges by specifying a long shell or GECOS field.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1122",
            "solucionado": false,
            "publicado": "1989-07-26T04:00:00Z",
            "ultimaModificacion": "2018-05-03T01:29:04.817Z",
            "descripcion": "Vulnerability in restore in SunOS 4.0.3 and earlier allows local users to gain privileges.",
            "severidad": "MEDIUM",
            "estado": "Modified"
        },
        {
            "id": "CVE-1999-1467",
            "solucionado": false,
            "publicado": "1989-10-26T04:00:00Z",
            "ultimaModificacion": "2017-12-19T02:29:08.393Z",
            "descripcion": "Vulnerability in rcp on SunOS 4.0.x allows remote attackers from trusted hosts to execute arbitrary commands as root, possibly related to the configuration of the nobody user.",
            "severidad": "HIGH",
            "estado": "Modified"
        },
        {
            "id": "CVE-1999-1506",
            "solucionado": false,
            "publicado": "1990-01-29T05:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:41.257Z",
            "descripcion": "Vulnerability in SMI Sendmail 4.0 and earlier, on SunOS up to 4.0.3, allows remote attackers to access user bin.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-0084",
            "solucionado": false,
            "publicado": "1990-05-01T04:00:00Z",
            "ultimaModificacion": "2017-10-10T01:29:00.387Z",
            "descripcion": "Certain NFS servers allow users to use mknod to gain privileges by creating a writable kmem device and setting the UID to 0.",
            "severidad": "HIGH",
            "estado": "Modified"
        },
        {
            "id": "CVE-2000-0388",
            "solucionado": false,
            "publicado": "1990-05-09T04:00:00Z",
            "ultimaModificacion": "2008-09-10T19:04:33.930Z",
            "descripcion": "Buffer overflow in FreeBSD libmytinfo library allows local users to execute commands via a long TERMCAP environmental variable.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-0209",
            "solucionado": false,
            "publicado": "1990-08-14T04:00:00Z",
            "ultimaModificacion": "2008-09-09T12:34:01.117Z",
            "descripcion": "The SunView (SunTools) selection_svc facility allows remote users to read files.",
            "severidad": "MEDIUM",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1198",
            "solucionado": false,
            "publicado": "1990-10-03T04:00:00Z",
            "ultimaModificacion": "2008-09-05T20:18:57.260Z",
            "descripcion": "BuildDisk program on NeXT systems before 2.0 does not prompt users for the root password, which allows local users to gain root privileges.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        }
    ]
}
```




### End-point: obtener vulnerabilidades ejemplo 2
### Method: GET
>```
>http://127.0.0.1:8000/api?cve_por_pagina=10&indice_inicial=10
>```
### Query Params

|Param|value|
|---|---|
|cve_por_pagina|10|
|indice_inicial|10|
|||


### Response: 200
```json
{
    "msg": "sucess",
    "CVEs": [
        {
            "id": "CVE-1999-1391",
            "solucionado": true,
            "publicado": "1990-10-03T04:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:24.600Z",
            "descripcion": "Vulnerability in NeXT 1.0a and 1.0 with publicly accessible printers allows local users to gain privileges via a combination of the npd program and weak directory permissions.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1392",
            "solucionado": true,
            "publicado": "1990-10-03T04:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:24.740Z",
            "descripcion": "Vulnerability in restore0.9 installation script in NeXT 1.0a and 1.0 allows local users to gain root privileges.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1057",
            "solucionado": false,
            "publicado": "1990-10-25T04:00:00Z",
            "ultimaModificacion": "2008-09-05T20:18:37.230Z",
            "descripcion": "VMS 4.0 through 5.3 allows local users to gain privileges via the ANALYZE/PROCESS_DUMP dcl command.",
            "severidad": "MEDIUM",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1554",
            "solucionado": false,
            "publicado": "1990-10-31T05:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:48.163Z",
            "descripcion": "/usr/sbin/Mail on SGI IRIX 3.3 and 3.3.1 does not properly set the group ID to the group ID of the user who started Mail, which allows local users to read the mail of other users.",
            "severidad": "LOW",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1197",
            "solucionado": false,
            "publicado": "1990-12-20T05:00:00Z",
            "ultimaModificacion": "2008-09-05T20:18:57.117Z",
            "descripcion": "TIOCCONS in SunOS 4.1.1 does not properly check the permissions of a user who tries to redirect console output and input, which could allow a local user to gain privileges.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1115",
            "solucionado": false,
            "publicado": "1990-12-31T05:00:00Z",
            "ultimaModificacion": "2008-09-05T20:18:45.430Z",
            "descripcion": "Vulnerability in the /etc/suid_exec program in HP Apollo Domain/OS sr10.2 and sr10.3 beta, related to the Korn Shell (ksh).",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1258",
            "solucionado": false,
            "publicado": "1991-01-15T05:00:00Z",
            "ultimaModificacion": "2017-10-10T01:29:04.857Z",
            "descripcion": "rpc.pwdauthd in SunOS 4.1.1 and earlier does not properly prevent remote access to the daemon, which allows remote attackers to obtain sensitive system information.",
            "severidad": "MEDIUM",
            "estado": "Modified"
        },
        {
            "id": "CVE-1999-1438",
            "solucionado": false,
            "publicado": "1991-02-22T05:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:31.490Z",
            "descripcion": "Vulnerability in /bin/mail in SunOS 4.1.1 and earlier allows local users to gain root privileges via certain command line arguments.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1211",
            "solucionado": false,
            "publicado": "1991-03-27T05:00:00Z",
            "ultimaModificacion": "2017-12-19T02:29:03.553Z",
            "descripcion": "Vulnerability in in.telnetd in SunOS 4.1.1 and earlier allows local users to gain root privileges.",
            "severidad": "HIGH",
            "estado": "Modified"
        },
        {
            "id": "CVE-1999-1212",
            "solucionado": false,
            "publicado": "1991-03-27T05:00:00Z",
            "ultimaModificacion": "2017-12-19T02:29:03.613Z",
            "descripcion": "Vulnerability in in.rlogind in SunOS 4.0.3 and 4.0.3c allows local users to gain root privileges.",
            "severidad": "HIGH",
            "estado": "Modified"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

### End-point: obtener vulnerabilidades ejemplo 3
### Method: GET
>```
>http://127.0.0.1:8000/api?cve_por_pagina=10&solucionadas=1
>```
### Query Params

|Param|value|
|---|---|
|cve_por_pagina|10|
|solucionadas|1|


### Response: 200
```json
{
    "msg": "sucess",
    "CVEs": [
        {
            "id": "CVE-1999-0095",
            "solucionado": true,
            "publicado": "1988-10-01T04:00:00Z",
            "ultimaModificacion": "2019-06-11T20:29:00.263Z",
            "descripcion": "The debug command in Sendmail is enabled, allowing attackers to execute commands as root.",
            "severidad": "HIGH",
            "estado": "Modified"
        },
        {
            "id": "CVE-1999-0082",
            "solucionado": true,
            "publicado": "1988-11-11T05:00:00Z",
            "ultimaModificacion": "2008-09-09T12:33:40.853Z",
            "descripcion": "CWD ~root command in ftpd allows root access.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1471",
            "solucionado": true,
            "publicado": "1989-01-01T05:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:36.257Z",
            "descripcion": "Buffer overflow in passwd in BSD based operating systems 4.3 and earlier allows local users to gain root privileges by specifying a long shell or GECOS field.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1391",
            "solucionado": true,
            "publicado": "1990-10-03T04:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:24.600Z",
            "descripcion": "Vulnerability in NeXT 1.0a and 1.0 with publicly accessible printers allows local users to gain privileges via a combination of the npd program and weak directory permissions.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        },
        {
            "id": "CVE-1999-1392",
            "solucionado": true,
            "publicado": "1990-10-03T04:00:00Z",
            "ultimaModificacion": "2008-09-05T20:19:24.740Z",
            "descripcion": "Vulnerability in restore0.9 installation script in NeXT 1.0a and 1.0 allows local users to gain root privileges.",
            "severidad": "HIGH",
            "estado": "Analyzed"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: establecer vulnerabilidades solucionadas
Solicittud tipo POST, utilizada para indicar que determinadas vulnerabilidades ya fueron solucionadas en nuestro sistema.

recibe en el body un objeto tipo json, con la clave ids y como valor la lista de las id de las vulnerabilidades solucionadas.
### Method: POST
>```
>http://127.0.0.1:8000/api
>```
### Response: 200
```json
{
    "datos": {
        "CVE-1999-0095": "sucess",
        "CVE-1999-1392": "sucess",
        "CVE-1999-1391": "sucess"
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
