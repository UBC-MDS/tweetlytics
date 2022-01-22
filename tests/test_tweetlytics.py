# Authors: Mahsa Sarafrazi, Mahmood Rahman, Shiva Shankar Jena, Amir Shojakhani
# Jan 2022

# imports
from tweetlytics.tweetlytics import get_store
import pandas as pd
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()  # load .env files in the project folder


def test_get_store():
    """
    Test various features of the get_store() function.
    - Check if .json file is created
    - Check if .csv file is created
    - Check if the result is a pandas dataframe
    - Check the column names of the returned dataframe
    - Check the number of returned rows in the dataframe

    5 tests will run
    """
    bearer_token = os.getenv("BEARER_TOKEN")
    today_str = datetime.now().strftime("%Y-%m-%d")
    start_str = (datetime.now() - timedelta(days=6)).strftime("%Y-%m-%d")
    tweets_results_df = get_store(
        bearer_token,
        keyword="vancouver",
        start_date=start_str,
        end_date=today_str,
        store_path="tests/output/",
        max_results=100,
        store_csv=True,
    )

    # Check if .json file is created
    assert os.path.exists("tests/output/tweets_response.json")

    # Check if .csv file is created
    assert os.path.exists("tests/output/tweets_response.csv")

    # Check if the result is a pandas dataframe
    assert type(tweets_results_df) == pd.core.frame.DataFrame

    # Check the column names of the returned dataframe
    assert set(tweets_results_df.columns) == set(
        [
            "public_metrics",
            "source",
            "author_id",
            "created_at",
            "conversation_id",
            "lang",
            "reply_settings",
            "referenced_tweets",
            "id",
            "text",
            "in_reply_to_user_id",
            "retweetcount",
            "reply_count",
            "like_count",
            "quote_count",
        ]
    )

    # Check the number of returned rows in the dataframe
    assert len(tweets_results_df) == 100
