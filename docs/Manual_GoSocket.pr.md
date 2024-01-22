



# GoSocket
  
Este módulo permite que você se conecte à sua conta GoSocket. Você poderá obter os documentos recebidos e enviados; e baixe-os em formato PDF ou XML.  

![banner](imgs/ModuloGoSocket.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Configurar credenciais
  
Configure credenciais para conectar-se à API GoSocket
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Usuario|E-mail registrado GoSocket|user|
|Dica|Senha GoSocket|password|
|Variável|Variável onde o resultado será salvo|res|
|Session|ID da sessão (Opcional)|session|

### Obtenha documentos recebidos
  
Liste os documentos que estão na pasta recebida
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Número de documentos a obter|Número de documentos recebidos que serão obtidos|10|
|Classificar por data de emissão|Os documentos obtidos serão ordenados por data de emissão. Por padrão é falso|False|
|Token de paginação|Token de paginação que o comando traz dentro de 'm_Item1' na primeira vez que é utilizado, quando é necessário paginar para obter os demais documentos|session|
|Variável|Variável onde o resultado será salvo|res|
|Session|ID da sessão (Opcional)|session|

### Obter documentos enviados
  
Liste os documentos que estão na pasta enviada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Número de documentos a obter|Número de documentos enviados que serão obtidos|10|
|Classificar por data de emissão|Os documentos obtidos serão ordenados por data de emissão. Por padrão é falso|False|
|Token de paginação|Token de paginação que o comando traz dentro de 'm_Item1' na primeira vez que é utilizado, quando é necessário paginar para obter os demais documentos|session|
|Variável|Variável onde o resultado será salvo|res|
|Session|ID da sessão (Opcional)|session|

### Baixar documento
  
Baixe um documento recebido do GoSocket em formato PDF ou XML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do documento|Você pode obter com o comando Obter documentos recebidos limpando a variável da seguinte maneira {docs}['m_Item2'][0]['DocumentId']|1M1YsqIRAaQnjWcSYjinLiaChD_0sE|
|Formato do documento|Escolha entre PDF ou XML|---- Select format ----|
|Caminho|Caminho onde salvar o arquivo|C:\users\usuario\Downloads|
|Variável|Variável onde o resultado será salvo|Variável|
|Session||session|
