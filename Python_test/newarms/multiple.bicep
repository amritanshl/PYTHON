param location string 
param sa_name string 

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01'= {
name:sa_name
kind:'StorageV2'
sku:{
  name:'Premium_LRS'
  }
location:location
}


resource webAppPlan 'Microsoft.Web/serverfarms@2023-01-01' ={
  name:concat(sa_name,'plan')
  location:location
  sku:{
    name:'F1'
  }
}


resource webApp 'Microsoft.Web/sites@2023-01-01'={
  name:concat(sa_name,'site')
  location:location
  properties:{
    serverFarmId:webAppPlan.id
    httpsOnly:true
  }
}
