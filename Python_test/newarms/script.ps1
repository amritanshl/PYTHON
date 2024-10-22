$csvData = Import-CSV -Path "D:\Data\Desktop\ARM\newarm\input.csv"
$csvData
$getparameterdata = Get-Content -Path ''
foreach($row in $csvData){
    Get-date 
     $sa_name = $row.fname + $row.lname + $row.empid
     $sa_name 
     
}

