import os
import sys
import pandas as pd
from sqlalchemy import create_engine, text


DB_PATH = "./clinic_simple.db"
CSV_PATH = "./data/patients.csv"


def main():
    # Ensure the CSV exists before attempting to read it.
    if not os.path.exists(CSV_PATH):
        print(f"CSV file not found: {CSV_PATH}")
        sys.exit(1)

    # Read the CSV file.
    df = pd.read_csv(CSV_PATH, dtype=str)

    # Create the database engine.
    engine = create_engine(f"sqlite:///{DB_PATH}")

    try:
        df.to_sql("patients", con=engine, if_exists="append", index=False)
    except Exception as e:
        print("Failed to write CSV to the database:", e)
        raise

    # Verify the number of rows loaded.
    sql_count = text("SELECT COUNT(*) FROM patients")
    with engine.connect() as conn:
        result = conn.execute(sql_count)
        # Use scalar() for broader SQLAlchemy compatibility (works in 1.x and 2.x).
        total = result.scalar() or 0

    print(f"Loaded {len(df)} rows into patients. Table now has {total} rows.")


if __name__ == "__main__":
    main()
