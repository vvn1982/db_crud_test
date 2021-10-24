# program.py
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
import sqlalchemy.ext.declarative
from utils.load_data import load_dataset, save_df_to_db

__engine = None
__factory = None


def setup_db():
    # engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/db_crud_test")
    global __engine, __factory
    __engine = create_engine("sqlite:///data/db_crud_test")
    __factory = sessionmaker(bind=__engine)
    session: Session = __factory()
    session.expire_on_commit = False

    # Base = sqlalchemy.ext.declarative.declarative_base()
    # Base.metadata.create_all(__engine)


def main():
    global __engine
    setup_db()
    # load dataset
    path_to_dataset = Path(r'D:\projects\db_crud_test\data\test_data.xlsx')
    df = load_dataset(path_to_dataset)
    if df:
        names = df['names']
        properties = df['properties']
    save_df_to_db(names, "names", engine=__engine)
    save_df_to_db(properties, "properties", __engine)
    save_df_to_db(properties, "properties", __engine)


if __name__ == '__main__':
    main()