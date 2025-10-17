import pandas as pd
from sqlalchemy import create_engine
from config.database import get_db_connection
import argparse
import os
from datetime import datetime

def export_monthly_summary(start_date, end_date, output_dir):
    """Export monthly summary report"""
    engine = create_engine(get_db_connection())
    
    query = f"""
    SELECT 
        DATE_TRUNC('month', report_date) as month,
        department,
        SUM(metric_value) as total_value,
        COUNT(*) as record_count
    FROM reports 
    WHERE report_date BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY DATE_TRUNC('month', report_date), department
    ORDER BY month, department
    """
    
    df = pd.read_sql(query, engine)
    filename = f"monthly_summary_{start_date}_to_{end_date}.csv"
    filepath = os.path.join(output_dir, filename)
    df.to_csv(filepath, index=False)
    print(f"Exported to {filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', required=True, help='Report type to export')
    parser.add_argument('--start-date', required=True, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', required=True, help='End date (YYYY-MM-DD)')
    parser.add_argument('--output-dir', default='./data/export', help='Output directory')
    
    args = parser.parse_args()
    export_monthly_summary(args.start_date, args.end_date, args.output_dir)
