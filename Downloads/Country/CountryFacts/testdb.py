import sqlalchemy as db
import pandas as pd

def print_database_data():
    engine = db.create_engine('sqlite:///seocountryinfo.db')

    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM country_info ORDER BY rowid DESC LIMIT 10;")).fetchall()

        if query_result:
            df = pd.DataFrame(query_result)
            print(df.to_string(index=False))  # Print the DataFrame without the index
        else:
            print("No data found in the database.")

