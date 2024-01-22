# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os
import requests
import traceback



base_path = tmp_global_obj["basepath"] #type: ignore
cur_path = base_path + 'modules' + os.sep + 'GoSocket' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)


class GoSocket_auth:

    def __init__(self, url, user, password):
        self.user = user
        self.password = password
        self.goSocket_url = url
        self.getToken()

    def getToken(self):
        try:    
            session = requests.Session()
            session.auth = (self.user, self.password)

            r = session.post(self.goSocket_url)
            r.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"Error de autenticación: {e}")
            return None
    
    def getReceivedDocuments(self, take_, order=False, conToken=None):

        try:
            session = requests.Session()
            session.auth = (self.user, self.password)

            getReceiveds = f'api/Mobile/GetReceivedDocuments?take={take_}&orderByEmisionDate={order}'
            if conToken:
                getReceiveds += f"&continuationToken={conToken}"

            r = session.get(self.goSocket_url + getReceiveds)

            return r.json()
           
        except Exception as e:
             PrintException()
             raise e
    
    def getSentDocuments(self, take_, order=False, conToken=None):

        try:
            session = requests.Session()
            session.auth = (self.user, self.password)

            getSents = f'api/Mobile/GetSentDocuments?take={take_}&orderByEmisionDate={order}'
            if conToken:
                getSents += f"&continuationToken={conToken}"

            r = session.get(self.goSocket_url + getSents)

            return r.json()
           
        except Exception as e:
             PrintException()
             raise e
        
    def downloadPdf(self, doc_id):
        try:
            session = requests.Session()
            session.auth = (self.user, self.password)
            
            get_pdf = f'api/Mobile/DownloadPdf?documentId={doc_id}'

            response = session.get(self.goSocket_url + get_pdf)

            if response.text == "null":
                raise Exception("The API return null, check the document_id or the API data")
            
            if response.status_code == 500:
                raise Exception("An error as ocurred")

            return response.content
        
        except Exception as e:
             PrintException()
             raise e
        
    def downloadXml(self, documentId):

        try:
            session = requests.Session()
            session.auth = (self.user, self.password)
            
            get_xml = f'api/Mobile/DownloadXml?documentId={documentId}'

            response = session.get(self.goSocket_url + get_xml)

            if response.text == "null":
                raise Exception("The API return null, check the document_id or the API data")
            if response.status_code == 500:
                raise Exception("An error as ocurred")

            return response.content
            

        except Exception as e:
             PrintException()
             raise e

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module") #type: ignore

global mod_gos_session
SESSION_DEFAULT = "default"

try:
    if not mod_gos_session : #type:ignore
        mod_gos_session = {SESSION_DEFAULT:{}}
except NameError:
    mod_gos_session = {SESSION_DEFAULT:{}}

session = GetParams("session") #type: ignore

if not session:
    session = ''

api_url = 'https://api.gosocket.net/'

try:
    if module == "connect":
        
        user = GetParams("user") #type: ignore
        password = GetParams("password")  #type: ignore
        result = GetParams("result") #type: ignore

        try:
            
            mod_gos_session = GoSocket_auth(api_url, user, password)
            
            if result:
                SetVar(result, True)    #type: ignore
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            mod_gos_session = None
            SetVar(result, False)   #type: ignore
            PrintException()    #type: ignore
            raise e

    if module == "getReceiveds":
        nro = GetParams("take_")
        orderby = GetParams("order")
        conToken_ = GetParams("conToken")
        result = GetParams("result")

        try:
            if not orderby:
                orderby = False

            documents = mod_gos_session.getReceivedDocuments(nro, orderby, conToken_)

            SetVar(result, documents)

        except Exception as e:
            import traceback  
            traceback.print_exc()
            SetVar(result, False)   #type: ignore
            PrintException()    #type: ignore
            raise e
        
    if module == "getSents":
        nro = GetParams("take_")
        orderby = GetParams("order")
        conToken_ = GetParams("conToken")
        result = GetParams("result")

        try:
            
            if not orderby:
                orderby = False

            documents = mod_gos_session.getSentDocuments(nro, orderby, conToken_)

            SetVar(result, documents)

        except Exception as e:
            import traceback  
            traceback.print_exc()
            SetVar(result, False)   #type: ignore
            PrintException()    #type: ignore
            raise e
        
    if module == "download":
        result = GetParams("result_var") #type: ignore
        doc = GetParams("id")    #type: ignore
        path = GetParams("path")    #type: ignore
        format = GetParams("format")

        try:
            if not doc:
                raise Exception("DocumentID no enviado")

            if not path:
                raise Exception("No se ingreso la ruta donde guardar el archivo")
             

            if format == 'PDF (.pdf)':
                pdf = mod_gos_session.downloadPdf(doc)  
                path_ = os.path.join(path, doc + '.pdf')
                
                with open(path_, 'wb') as pdf_file:
                    pdf_file.write(pdf)
           
            else:
                xml = mod_gos_session.downloadXml(doc)
                path_ = os.path.join(path, doc + '.xml')  

                with open(path_, 'wb') as xml_file:
                    xml_file.write(xml)

            SetVar(result, True)

        except Exception as e:
                import traceback
                traceback.print_exc()
                PrintException()    #type: ignore
                SetVar(result, False)   #type: ignore
                raise e

except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()    #type: ignore
            raise e