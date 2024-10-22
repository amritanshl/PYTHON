param location string
param app string
param plan string
param sku string


resource serverPlan 'Microsoft.Web/serverfarms@2023-01-01' ={
  name: plan
  location: location
  sku:{
    name: sku
  }
}

resource actualApp 'Microsoft.Web/sites@2023-01-01'={
  name: app
  location: location
  properties:{
    serverFarmId: serverPlan.id
    httpsOnly:true
  }
}
