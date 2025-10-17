from sqlalchemy import create_engine
from config.database import get_db_connection
import pandas as pd

def load_to_database(df, table_name='reports'):
    """Load processed data to PostgreSQL database"""
    engine = create_engine(get_db_connection())
    
    # Create table if not exists (with proper schema)
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"Loaded {len(df)} records to {table_name} table")
