import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Database connection
def get_connection():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

def create_tables():
    """Create simple tables"""
    commands = [
        """
        CREATE TABLE IF NOT EXISTS banks (
            bank_id SERIAL PRIMARY KEY,
            bank_name VARCHAR(255) NOT NULL UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            bank_name VARCHAR(255) NOT NULL,
            review_text TEXT,
            rating INTEGER,
            review_date DATE,
            sentiment_score FLOAT,
            sentiment_label VARCHAR(50)
        )
        """
    ]
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            for cmd in commands:
                cur.execute(cmd)
        conn.commit()
    print("Tables created successfully")

def import_csv_to_db():
    """Import data from CSV files directly"""
    csv_files = {
        'BOA': '../data/raw/reviews_BOA.csv',
        'CBE': '../data/raw/reviews_CBE.csv',
        'Dashen': '../data/raw/reviews_Dashen.csv'
    }
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Insert banks
            for bank in csv_files.keys():
                cur.execute(
                    "INSERT INTO banks (bank_name) VALUES (%s) ON CONFLICT (bank_name) DO NOTHING",
                    (bank,)
                )
            conn.commit()
            
            # Insert reviews
            for bank_name, filename in csv_files.items():
                try:
                    df = pd.read_csv(filename)
                    print(f"Importing {len(df)} reviews from {filename}")
                    
                    for _, row in df.iterrows():
                        cur.execute(
                            """
                            INSERT INTO reviews 
                            (bank_name, review_text, rating, review_date, sentiment_score, sentiment_label)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """,
                            (
                                bank_name,
                                str(row.get('review_text', '')),
                                int(row.get('rating', 0)),
                                pd.to_datetime(row.get('review_date', 'today')).date(),
                                float(row.get('sentiment_score', 0)),
                                str(row.get('sentiment_label', 'neutral'))
                            )
                        )
                    conn.commit()
                    print(f"Successfully imported {len(df)} reviews for {bank_name}")
                    
                except FileNotFoundError:
                    print(f"File not found: {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
                    conn.rollback()

if __name__ == '__main__':
    print("Starting data import...")
    create_tables()
    import_csv_to_db()
    print("Data import completed!")