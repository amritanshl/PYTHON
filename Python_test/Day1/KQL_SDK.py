from azure.kusto.data import KustoClient, KustoConnectionStringBuilder, ClientRequestProperties
from datetime import timedelta
import uuid;

def main():
  cluster_uri = "https://help.kusto.windows.net"
  kcsb = KustoConnectionStringBuilder.with_interactive_login(cluster_uri)

  crp = ClientRequestProperties()

  crp.client_request_id = "QueryDemo" + str(uuid.uuid4())
  crp.set_option(crp.request_timeout_option_name, timedelta(minutes=1))
  crp.set_parameter("event_type", "Flash Flood")
  crp.set_parameter("daily_damage", str(200000000))

  with KustoClient(kcsb) as kusto_client:

    database = "Samples"
    query = "declare query_parameters(event_type:string, daily_damage:int);"\
            "StormEvents" \
            "| where EventType == event_type" \
            "| extend TotalDamages = DamageProperty + DamageCrops" \
            "| summarize DailyDamage=sum(TotalDamages) by State, bin(StartTime, 1d)" \
            "| where DailyDamage > daily_damage" \
            "| order by DailyDamage desc"

    response = kusto_client.execute_query(database, query, crp)

    state_col = 0
    start_time_col = next(col.ordinal for col in response.primary_results[0].columns if col.column_name == "StartTime")
    damage_col = 2


    print("Daily flash flood damages over 200,000,000$:")
    for row in response.primary_results[0]:
      print(row[start_time_col], "-", row[state_col], ",", row[damage_col], "$")

if __name__ == "__main__":
  main()


from azure.kusto.data import KustoClient, KustoConnectionStringBuilder

def main():
  cluster_uri = "https://jitincluster.northeurope.kusto.windows.net/"
  kcsb = KustoConnectionStringBuilder.with_interactive_login(cluster_uri)

  with KustoClient(kcsb) as kusto_client:

    database = "MyDatabase"
    query = "orderslocal"
    response = kusto_client.execute(database, query)

    print(response.primary_results[0])

if __name__ == "__main__":
  main()


from azure.kusto.data import KustoClient, KustoConnectionStringBuilder

def main():
  cluster_uri = "https://jitincluster.northeurope.kusto.windows.net/"
  kcsb = KustoConnectionStringBuilder.with_interactive_login(cluster_uri)

  with KustoClient(kcsb) as kusto_client:

    database = "MyDatabase"
    table = "MyStormEvents"

    # Create a table named MyStormEvents
    # The brackets contain a list of column Name:Type pairs that defines the table schema
    command = ".create table " + table + " " \
              "(StartTime:datetime," \
              " EndTime:datetime," \
              " State:string," \
              " DamageProperty:int," \
              " DamageCrops:int," \
              " Source:string," \
              " StormSummary:dynamic)"

    response = kusto_client.execute_mgmt(database, command)
    print_result_as_value_list(command, response)

def print_result_as_value_list(command, response):
  # create a list of columns
  cols = (col.column_name for col in response.primary_results[0].columns)

  print("\n" + "-" * 20 + "\n")
  print("Command: " + command)
  # print the values for each row
  for row in response.primary_results[0]:
    print("Result:")
    for col in cols:
      print("\t", col, "-", row[col])

if __name__ == "__main__":
  main()