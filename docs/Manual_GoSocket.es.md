



# GoSocket
  
Este módulo le permite conectarse a su cuenta de GoSocket. Podrá obtener los documentos recibidos y enviados; y descargarlos en formato PDF o XML.  

  
![banner](imgs/ModuloGoSocket.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Configurar credenciales
  
Configura las credenciales para conectar con la api de GoSocket
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|User|Mail registrado de GoSocket|user|
|Clue|Contraseña de GoSocket|password|
|Variable|Variable donde se guardará el resultado|res|
|Session|Identificador de sesión (Opcional)|session|

### Obtener Documentos Recibidos
  
Lista los documentos que estén en la carpeta de recibidos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Cantidad de documentos a obtener|Cantidad de documentos recibidos que serán obtenidos|10|
|Ordenar por fecha de emisión|Los documentos obtenidos se ordenarán por fecha de emisión. Por default es Falso|False|
|Token de paginación|Token de paginación que trae el comando dentro de 'm_Item1' la primera vez que es utilizado, cuando es necesario paginar para obtener los demás documentos|session|
|Variable|Variable donde se guardará el resultado|res|
|Session|Identificador de sesión (Opcional)|session|

### Obtener Documentos Enviados
  
Lista los documentos que estén en la carpeta de enviados
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Cantidad de documentos a obtener|Cantidad de documentos enviados que serán obtenidos|10|
|Ordenar por fecha de emisión|Los documentos obtenidos se ordenarán por fecha de emisión. Por default es Falso|False|
|Token de paginación|Token de paginación que trae el comando dentro de 'm_Item1' la primera vez que es utilizado, cuando es necesario paginar para obtener los demás documentos|session|
|Variable|Variable donde se guardará el resultado|res|
|Session|Identificador de sesión (Opcional)|session|

### Descargar Documento
  
Decarga un documento recibido de GoSocket en formato PDF o XML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del Documento|Se puede conseguir con el comando Obtener Documentos Recibidos al limpiar la variable de la siguiente manera {docs}['m_Item2'][0]['DocumentId']|1M1YsqIRAaQnjWcSYjinLiaChD_0sE|
|Formato del documento|Elige entre PDF o XML|---- Select format ----|
|Ruta|Ruta donde guardar archivo|C:\users\usuario\Downloads|
|Variable|Variable donde se guardará el resultado|Variable|
|Session||session|
