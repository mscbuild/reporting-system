import pandas as pd
import os
from config.database import get_db_connection
from utils.helpers import validate_data

def process_excel_files(input_dir):
    """Process all Excel files in the input directory"""
    processed_data = []
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.xlsx'):
            filepath = os.path.join(input_dir, filename)
            df = pd.read_excel(filepath)
            
            # Data validation and cleaning
            if validate_data(df):
                df['source_file'] = filename
                df['processed_date'] = pd.Timestamp.now()
                processed_data.append(df)
            else:
                print(f"Validation failed for {filename}")
    
    return pd.concat(processed_data, ignore_index=True) if processed_data else pd.DataFrame()
