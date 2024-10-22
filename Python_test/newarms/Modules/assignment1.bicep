@description('This defines the name of a Storage Account')
@minLength(3)
@maxLength(24)
param storageAccountName string='jitin'

@description('This is an array of locations for Storage Account')
param storageLocation array = [
  'eastus'
  'westus3'
  'uaenorth'
  'swedencentral'
]

@description('All the available SKUs for the Storage account')
param storageAccountSku array =[
   'Standard_LRS'
   'Premium_ZRS'
]

@description('List of all the available environments')
param environment array = [
  'prod'
  'test'
]
@description('Current Time Stam in MMddyyyy format')
param currentDate string = utcNow('MMddyyyy') 

@description('Kind of a storage account')
param storageKind string='StorageV2'

resource storageAccountUSA 'Microsoft.Storage/storageAccounts@2023-01-01'= [for i in range(0,length(storageLocation)): if(contains(storageLocation[i],'us')) {
  name:'${environment[0]}${i}${storageAccountName}${currentDate}'  
  location:storageLocation[i]
  sku:{
    name:storageAccountSku[1]
  }
  kind:storageKind
} ]


resource storageAccountNotUSA 'Microsoft.Storage/storageAccounts@2023-01-01'= [for i in range(0,length(storageLocation)): if(!contains(storageLocation[i],'us')){
  name:'${environment[1]}${i}${storageAccountName}${currentDate}'  
  location:storageLocation[i]
  sku:{
    name:storageAccountSku[0]
  }
  kind:storageKind
} ]


