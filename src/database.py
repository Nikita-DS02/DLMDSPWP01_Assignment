import pandas as pd
from sqlalchemy import create_engine, text

class DatabaseManager:
    def __init__(self, db_name="project_data.db"):
        self.engine = create_engine(f"sqlite:///{db_name}")
        print(f"Connected to SQLite DB: {db_name}")

    def load_csv_to_db(self, csv_path, table_name):
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, self.engine, if_exists="replace", index=False)
        print(f"Loaded '{csv_path}' into table '{table_name}'")

    def preview_table(self, table_name, rows=5):
        with self.engine.connect() as conn:
            result = conn.execute(text(f"SELECT * FROM {table_name} LIMIT {rows}"))  # <-- fixed line
            for row in result:
                print(row)

