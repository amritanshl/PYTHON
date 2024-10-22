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
@description('Unique name for app serivice plan')
var appservicePlanName = '${environmentName}-${solutionName}-plan'
@description('Unique name for our web app')
var appServiceAppName = '${environmentName}-${solutionName}-site'

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

