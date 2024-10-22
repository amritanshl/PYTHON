using './webappday2.bicep'

param environmentName = 'dev'
param solutionName = 'jitin3838383'
param appserviceplaninstancecount = 1
param appServicePlanSKU = {
  name: 'F1'
  tier: 'Free'
}
param location = 'eastus'

