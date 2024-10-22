param location string

param myName object = {
  name:'Standard_LRS'
  tier:'Standard'
}

@secure()
param sqlServerAdminLogin string

@secure()
param sqlServerAdminPassword string

param isEnabled bool

param sqlDbSku object={
  name: 'Standard'
  tier: 'Standard'
}

@allowed([
  'Dev'
  'Prod'
])
param environmentName string = 'Dev'
param auditStorageAccountSKU string ='Standard_LRS'

var sqlServerName = 'jitinserver24012024'
var sqlDbName = 'jitinDB'

var auditingEnabled ='Prod'
var sa_name ='jitinsa01242024'




resource sqlServer 'Microsoft.Sql/servers@2023-05-01-preview' ={
  name:sqlServerName
  location:location
  properties:{
    administratorLogin:sqlServerAdminLogin
    administratorLoginPassword:sqlServerAdminPassword
  }
}

resource sqlDb 'Microsoft.Sql/servers/databases@2023-05-01-preview'={
  parent: sqlServer
  name: sqlDbName
  location:location
  sku:sqlDbSku

}

resource auditStorgeAccount 'Microsoft.Storage/storageAccounts@2023-01-01'= if(auditingEnabled =='Dev'){
  name:'jitin01202024'
  location:'eastus'
  sku:myName
  kind:'StorageV2'
}



