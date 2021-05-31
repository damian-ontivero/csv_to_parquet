import pandas

if __name__ == '__main__':
    csv_path = 'file.csv'
    parquet_name = 'file.parquet'

    file = pandas.read_csv(csv_path)
    file.to_parquet(parquet_name)