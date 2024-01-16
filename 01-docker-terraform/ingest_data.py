#!/usr/bin/env python
# coding: utf-8

import os
import argparse

import pandas as pd 
from sqlalchemy import create_engine
from time import time

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name='output.parquet'
    csv_name='output.csv'

    os.system(f"wget {url} -O {parquet_name}")


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    df_parq = pd.read_parquet(parquet_name)
    df_parq.to_csv(csv_name, index=None)

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)


    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')


    while True:
        t_start = time()
        
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end = time()

        print('inserted another chunk..., took %.3f seconds' %(t_end - t_start))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to pgres')

    parser.add_argument('--user', help='pgres username')
    parser.add_argument('--password', help='pgres user password')
    parser.add_argument('--host', help='pgres host')
    parser.add_argument('--port', help='pgres port')
    parser.add_argument('--db', help='pgres db name')
    parser.add_argument('--table_name', help='name of table where results are written to')
    parser.add_argument('--url', help='url of csv file')


    args = parser.parse_args()

    main(args)

