resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01'= {
name:'jitinstorage22012024'
kind:'StorageV2'
sku:{
  name:'Premium_LRS'
}
location:'westus3'
}
