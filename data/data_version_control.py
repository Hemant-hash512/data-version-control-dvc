from google.cloud import bigquery_storage
from google.cloud.bigquery_storage import types
import pandas

bqstorageclient = bigquery_storage.BigQueryReadClient()

project_id = "root-micron-336614"
dataset_id = "Dataset_1"
table_id = "Table_1"
table = f"projects/{project_id}/datasets/{dataset_id}/tables/{table_id}"

# Select columns to read with read options. If no read options are
# specified, the whole table is read.
read_options = types.ReadSession.TableReadOptions(
    selected_fields=["species_common_name", "fall_color"]
)

parent = "projects/{}".format(project_id)

requested_session = types.ReadSession(
    table=table,
    # Avro is also supported, but the Arrow data format is optimized to
    # work well with column-oriented data structures such as pandas
    # DataFrames.
    data_format=types.DataFormat.ARROW,
    read_options=read_options,
)
read_session = bqstorageclient.create_read_session(
    parent=parent, read_session=requested_session, max_stream_count=1,
)

# This example reads from only a single stream. Read from multiple streams
# to fetch data faster. Note that the session may not contain any streams
# if there are no rows to read.
stream = read_session.streams[0]
reader = bqstorageclient.read_rows(stream.name)

# Parse all Arrow blocks and create a dataframe.
frames = []
for message in reader.rows().pages:
    frames.append(message.to_dataframe())
dataframe = pandas.concat(frames)
print(dataframe.head())