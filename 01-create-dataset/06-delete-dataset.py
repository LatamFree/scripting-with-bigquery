from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'ado-boolean.scripting_druminot'
client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)
print("Deleted dataset '{}'.".format(dataset_id))