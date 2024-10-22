using './multiple.bicep'


@allowed([
  'CentralIndia'
  'WestIndia'
  'SouthIndia'
  
])
param location = '{location}'
param sa_name = '{sa_name}'

