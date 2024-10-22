param timestamp string = utcNow('MMddyyyyhhss')
param location string = 'westus3'

module application 'Modules/modules.bicep'={
  name: 'jitinApplication'
  params:{
    app: 'jitin${timestamp}-app'
    plan:'jitin${timestamp}-plan'
    location:location
    sku:'F1'
  }
}
module sadetail 'Modules/storage.bicep' ={
  name: 'storagedeploy'
  params:{
    saname:'jitin${timestamp}'
    sasku:'Premium_LRS'
    kind:'StorageV2'
    location:location
  }
}
 
