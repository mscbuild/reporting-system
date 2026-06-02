## 📊 Reporting Collection & Analysis System

 
<img  width="900" height="400" alt="Analysis System" src="https://github.com/user-attachments/assets/0ee3e76e-91b0-472b-939d-d2bfc2a16b30" class="center">


**Project Overview**

This system provides an end-to-end solution for collecting, processing, storing, and visualizing reporting data. The workflow begins with data collection via Excel forms, processes the data using Python scripts, stores it in a PostgreSQL database, exports required datasets, and finally creates interactive dashboards using Power BI.

**System Architecture**

~~~bash

┌─────────────────┐    ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                  │    │                 │    │                 │
│  Excel Forms    ├───►│  Python Data    ├───►│  PostgreSQL      ├───►│  Python Export  ├───►│  Power BI       │
│  (Data Input)   │    │  Processing     │    │  Database        │    │  Scripts        │    │  Dashboards     │
│                 │    │  Scripts        │    │  (Storage)       │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └──────────────────┘    └─────────────────┘    └─────────────────┘
~~~

**Technologies Used**

- **Data Collection:** Microsoft Excel (.xlsx files)
- **Data Processing:** Python 3.8+ with pandas, openpyxl, SQLAlchemy
- **Database:** PostgreSQL 12+
- **Data Export:** Python scripts with pandas
- **Visualization:** Microsoft Power BI Desktop
- **Version Control:** Git/GitHub

**Installation & Setup**

**Prerequisites**
- Python 3.8 or higher
- PostgreSQL 12 or higher
- Microsoft Excel (for form creation)
- Power BI Desktop
- Git

  # Environment Setup

**1.Clone the repository:**

~~~bash
git clone https://github.com/mscbuild/reporting-system.git
cd reporting-collection-system
~~~

**2.Create and activate virtual environment:**

~~~bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
~~~

**3.Install Python dependencies:**

~~~bash
pip install -r requirements.txt
~~~

**4.Set up PostgreSQL database:**

~~~bash
CREATE DATABASE reporting_system;
CREATE USER reporting_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE reporting_system TO reporting_user;
~~~

**5.Configure environment variables:**

Create a `.env` file in the project root:

~~~bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=reporting_system
DB_USER=reporting_user
DB_PASSWORD=secure_password
EXCEL_INPUT_DIR=./data/input
EXPORT_OUTPUT_DIR=./data/export
~~~

## Directory Structure

~~~bash
reporting-system/
├── docs/                    # Documentation files
│   ├── architecture.md
│   └── user_guide.md
├── data/
│   ├── input/              # Excel input files
│   └── export/             # Exported CSV/Excel files for Power BI
├── src/
│   ├── config/
│   │   └── database.py     # Database configuration
│   ├── ingestion/
│   │   └── excel_processor.py  # Excel processing scripts
│   ├── storage/
│   │   └── db_loader.py    # Database loading scripts
│   ├── export/
│   │   └── data_exporter.py # Data export scripts
│   └── utils/
│       └── helpers.py      # Utility functions
├── tests/                  # Unit tests
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore
├── README.md
└── powerbi/                # Power BI files and documentation
    ├── dashboards/
    └── documentation/
~~~

## Usage Guide

**1. Data Collection (Excel Forms)**

- Use the provided Excel template `(templates/reporting_template.xlsx)` to collect data
- Save completed forms in the `data/input/` directory
- Ensure all required fields are filled according to the data dictionary

**2. Data Processing and Loading**

Run the data processing pipeline:

~~~bash
# Process Excel files and load to database
python src/ingestion/excel_processor.py
python src/storage/db_loader.py
~~~

Or run the complete pipeline:

~~~bash
python run_pipeline.py
~~~

**3. Data Export**

Export required datasets for Power BI:

~~~bash
# Export all reports
python src/export/data_exporter.py --all

# Export specific report for date range
python src/export/data_exporter.py --report monthly_summary --start-date 2025-01-01 --end-date 2025-09-30
~~~

**4. Power BI Dashboard Creation**

1.Open Power BI Desktop

2.Import exported CSV/Excel files from `data/export/`

3.Create relationships between tables as needed

4.Build visualizations and dashboards

5.Save `.pbix file` in `powerbi/dashboards/`

## Key Scripts

**Excel Processing** `(src/ingestion/excel_processor.py)`

**Database Loading** `(src/storage/db_loader.py)`

**Data Export** `(src/export/data_exporter.py)`

**Database Schema** `sgl`

## Power BI Integration

**1.Data Refresh:** Configure Power BI to automatically refresh from the export directory

**2.Parameters:** Create date parameters for dynamic period selection

**3.Measures:** Implement DAX measures for KPIs and calculations

**4.Visualizations:**

- Time series charts for trend analysis
 
- Bar charts for departmental comparisons
 
- Tables for detailed data review

## Testing

Run unit tests:

~~~bash
python -m pytest tests/
~~~

## Deployment

For production deployment:

1.Set up scheduled tasks (cron jobs or Windows Task Scheduler) to run the pipeline daily

2.Configure database backups

3.Implement error logging and monitoring

4.Set up Power BI service for cloud-based dashboard sharing

## Contributing

1.Fork the repository

2.Create a feature branch  

3.Commit your changes  

4.Push to the branch  

5.Create a Pull Request

## License

This project is licensed under the MIT License  

> [!NOTE]   
> Remember to update the `.env.example` file with your actual configuration and never commit sensitive information to version control.

<!--
keywords: n8n workflows, n8n automation, n8n examples, n8n templates, no-code automation, telegram bot workflows, openai n8n, webhook automation, best proyect, creative repo, awesome, star repo, mscbuild, YuriDev
-->
