using './conditions.bicep'

param location = ''
param sqlServerAdminLogin = ''
param sqlServerAdminPassword = ''
param isEnabled = false
param sqlDbSku = {
  name: 'Standard'
  tier: 'Standard'
}
param environmentName = 'Dev'
param auditStorageAccountSKU = 'Standard_LRS'

