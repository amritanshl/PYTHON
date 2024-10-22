param saname string
param location string
param sasku string
param kind string

resource saaccout 'Microsoft.Storage/storageAccounts@2023-01-01'={
  name:saname
  location:location
  kind:kind
  sku:{
    name:sasku
  }
}
