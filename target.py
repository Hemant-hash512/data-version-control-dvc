from google.cloud import bigquery
import pandas as pd
client = bigquery.Client()
PROJECT_ID = 'root-micron-336614'
client.create_dataset("dataset_new")
client.create_table(f"{PROJECT_ID}.dataset_new.target_table")
filename = 'data.csv'
df = pd.read_csv(filename)
df.drop('has_diabetes', inplace=True, axis=1)
df.to_csv('data1.csv')
file='data1.csv'
dataset_id = 'dataset_new'
table_id = 'target_table'
dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.autodetect = True
with open(file, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
job.result()
print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))