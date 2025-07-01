import daft
import pandas as pd
# import deltalake
# from deltalake.schema import _convert_pa_schema_to_delta


def read_data():
    """
    Import data and check datafrmae which are not materialized
    1. Import data using pandas
    2. Import data using daft
    3. Keep columns needed
    """
    df = pd.read_csv(r"C:\Users\HP\Desktop\TryDuckDB_Lambda\data.csv")
    print(df)

    df_daft = daft.read_csv(r"C:\Users\HP\Desktop\TryDuckDB_Lambda\data.csv",allow_variable_columns=True)
    print(df_daft)

    columns_to_keep = ['date','serial_number','model','capacity_bytes','failure','datacenter','cluster_id','vault_id','pod_id','pod_slot_num']

    df_cleaned = df_daft.select(*columns_to_keep)
    print(df_cleaned)
    df_cleaned.write_deltalake('s3://confessions-of-a-data-guy/ducklamb')
    df_date = daft.from_pydict({"date": ['2024-12-30'], 'model': ['ST4000DM000'], 'failure_rate': [0]})
    print(df_date)
    df_cleaned.write_deltalake('s3://confessions-of-a-data-guy/ducklambcummulative', partition_cols=['date'])
read_data()





