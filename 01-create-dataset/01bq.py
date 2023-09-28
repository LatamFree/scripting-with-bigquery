from google.cloud import bigquery

bq = bigquery.Client(project='ado-boolean')

dataset_id = 'scripting_druminot'

dataset = bq.dataset(dataset_id)
dataset.location = 'southamerica-west-1'

bq.create_dataset(dataset, exists_ok=True)