



# GoSocket
  
This module allows you to connect to your GoSocket account. You will be able to obtain the documents received and sent; and download them in PDF or XML format.  

![banner](imgs/ModuloGoSocket.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Set up credentials
  
Configure credentials to connect to the GoSocket API
|Parameters|Description|example|
| --- | --- | --- |
|Usuario|GoSocket Registered Email|user|
|Clave|GoSocket Password|password|
|Variable|Variable where the result will be saved|res|
|Session|Session ID (Optional)|session|

### Get Received Documents
  
List the documents that are in the received folder
|Parameters|Description|example|
| --- | --- | --- |
|Number of documents to obtain|Number of documents received that will be obtained|10|
|Order by emision date|The documents obtained will be ordered by issue date. By default it is False|False|
|Paging Token|Pagination token that the command brings within 'm_Item1' the first time it is used, when it is necessary to paginate to obtain the other documents|session|
|Variable|Variable where the result will be saved|res|
|Session|Session ID (Optional)|session|

### Get Sent Documents
  
List the documents that are in the sent folder
|Parameters|Description|example|
| --- | --- | --- |
|Number of documents to obtain|Number of documents sent that will be obtained|10|
|Order by emision date|The documents obtained will be ordered by issue date. By default it is False|False|
|Paging Token|Pagination token that the command brings within 'm_Item1' the first time it is used, when it is necessary to paginate to obtain the other documents|session|
|Variable|Variable where the result will be saved|res|
|Session|Session ID (Optional)|session|

### Download Document
  
Download a document received from GoSocket in PDF or XML format
|Parameters|Description|example|
| --- | --- | --- |
|Document ID|You can get with the command Get Received Documents by clearing the variable as follows {docs}['m_Item2'][0]['DocumentId']|1M1YsqIRAaQnjWcSYjinLiaChD_0sE|
|Document format|Choose between PDF or XML|---- Select format ----|
|Path|Path where to save file|C:\users\usuario\Downloads|
|Variable|Variable where the result will be saved|Variable|
|Session||session|
