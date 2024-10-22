@description('Environment Name')
@allowed([
  'dev'
  'test'
  'prod'
])
@secure()
param environmentName string ='dev'
@description('Unique name of our solution')
@minLength(5)
@maxLength(30)
param solutionName string = 'jitin3838383'
@minValue(1)
@maxValue(10)
param appserviceplaninstancecount int = 1
param appServicePlanSKU object ={
  name: 'F1'
  tier: 'Free'

}
@secure()
param location string = 'eastus'

@secure()
@description('Admin username for sql server')
param sqlServerAdministratorLogin string

@secure()
@description('admin password for sql server')
param sqlServerAdministratorPassword string

@description('The name and tier of sql')
param sqlDbSKU object ={
  name :'Standard'
  tier : 'Standard'
}



@description('Unique name for app serivice plan')
var appservicePlanName = '${environmentName}-${solutionName}-plan'
@description('Unique name for our web app')
var appServiceAppName = '${environmentName}-${solutionName}-site'
@description('Unique name for sql')
var sqlServerName = '${environmentName}-${solutionName}-sql'
var sqlDatabaseName = 'Employees'


resource sqlServer 'Microsoft.Sql/servers@2023-05-01-preview'={
  name: sqlServerName
  location:location
  properties:{
    administratorLogin:sqlServerAdministratorLogin
    administratorLoginPassword:sqlServerAdministratorPassword
  }
}

resource sqlDatabase 'Microsoft.Sql/servers/databases@2023-05-01-preview'={
  parent:sqlServer
  name:sqlDatabaseName
  location:location
  sku:{
    name:sqlDbSKU.name
    tier: sqlDbSKU.tier
  }
}


resource appServicePlan 'Microsoft.Web/serverfarms@2023-01-01'={
  name:appservicePlanName
  location:location
  sku:{
    name:appServicePlanSKU.name
    tier:appServicePlanSKU.tier
    capacity : appserviceplaninstancecount
  }

}
resource appServiceApp 'Microsoft.Web/sites@2023-01-01'={
  name: appServiceAppName
  location:location
  properties:{
    serverFarmId:appServicePlan.id
    httpsOnly:true
  }
}

