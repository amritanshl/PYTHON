param locations array=[
  'eastus'
  'westus3'
  'centralindia'
  'japaneast'
]

resource sa 'Microsoft.Storage/storageAccounts@2023-01-01'= [for i in range(0,length(locations)) :{
  name: '${locations[i]}deepak012420'
  sku:{
    name:'Standard_GRS'
  }
  location:locations[i]
  kind:'StorageV2'
}

]

