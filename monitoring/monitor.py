# monitoring/monitor.py

import pandas as pd
import sqlalchemy
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.metrics import RegressionQualityMetric  # ✅ New import
import os
from dotenv import load_dotenv
load_dotenv()

# Environment configs
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("POSTGRES_HOST", "monitoring-postgres") 
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "faang_monitoring")

DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=disable"

engine = sqlalchemy.create_engine(DATABASE_URI)

def load_data():
    ref = pd.read_csv("data/reference.csv")
    curr = pd.read_csv("data/current.csv")
    return ref, curr


def run_report():
    ref, curr = load_data()

    report = Report(metrics=[
        DataDriftPreset(),
        RegressionQualityMetric()  
    ])

    report.run(reference_data=ref, current_data=curr)
    
    os.makedirs("monitoring/reports", exist_ok=True)
    report.save_html("monitoring/reports/monitoring_report.html")
    report.save("monitoring/reports/monitoring_report.json")

    # Optional: store metrics in PostgreSQL
    report_data = report.as_dict()
    df_metrics = pd.json_normalize(report_data)
    df_metrics.to_sql("monitoring_metrics", engine, if_exists="append", index=False)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "run":
            run_report()
        elif sys.argv[1] == "init-db":
            from models import Base
            Base.metadata.create_all(engine)
    else:
        run_report()

    

   

