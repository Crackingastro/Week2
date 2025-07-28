from google_play_scraper import Sort, reviews
import pandas as pd
import os

def fetch_reviews(app_id, app_name, max_reviews=500):
    """
    Fetch reviews from the Google Play Store for a given app.
    """
    print(f"Scraping reviews for {app_name}...")
    all_reviews = []

    while len(all_reviews) < max_reviews:
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=400,
            filter_score_with=None
        )
        all_reviews.extend(result)
        if len(result) < 400:
            break

    df = pd.DataFrame(all_reviews)
    df = df[['reviewId', 'userName', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'at']]
    df.rename(columns={
        'content': 'review',
        'score': 'rating',
        'at': 'date',
        'reviewCreatedVersion': 'app_version'
    }, inplace=True)
    return df

def save_reviews(df, bank_name):
    """
    Save reviews DataFrame to CSV in data/raw folder.
    """
    os.makedirs("data/raw", exist_ok=True)
    file_path = f"data/raw/reviews_{bank_name}.csv"
    df.to_csv(file_path, index=False)
    print(f"Saved {len(df)} reviews to {file_path}")

def scrape_and_save():
    """
    Main scraping logic for multiple banking apps.
    """
    apps = {
        "com.combanketh.mobilebanking": "CBE",
        "com.boa.boaMobileBanking": "BOA",
        "com.dashen.dashensuperapp": "Dashen"
    }

    for app_id, name in apps.items():
        df = fetch_reviews(app_id, name, max_reviews=400)
        save_reviews(df, name)

if __name__ == "__main__":
    scrape_and_save()
    print("All reviews scraped and saved.")
