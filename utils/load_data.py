import numpy as np, pandas as pd


def load_dataset(filepath: str):
    try:
        dfs = pd.read_excel(filepath,
                            engine='openpyxl',
                            sheet_name=None
                            )
    except FileNotFoundError as e:
        print(e)
        dfs = None

    return dfs


def save_df_to_db(df: pd.DataFrame,  table_name: str, engine):
    df.to_sql(table_name, engine)

