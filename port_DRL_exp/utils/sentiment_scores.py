import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# Load sentiment model once (e.g., FinBERT or Twitter RoBERTa)
MODEL_NAME = "ProsusAI/finbert"   # or "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def compute_sentiment_score(texts, batch_size=16):
    """
    Compute sentiment score for a list of texts.
    Returns scores between -1 (bearish) and +1 (bullish).
    """
    scores = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        tokens = tokenizer(batch, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**tokens)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        if probs.shape[1] == 3:  # negative, neutral, positive
            batch_scores = probs[:, 2] - probs[:, 0]  # positive - negative
        else:
            batch_scores = probs[:, 1]  # some models binary: prob(pos)
        scores.extend(batch_scores.cpu().numpy())
    return np.array(scores)

def add_sentiment(df, news_df, text_col="headline", date_col="date"):
    """
    Merge sentiment scores into price dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        Market data with 'date' column.
    news_df : pd.DataFrame
        News/social data with 'date' and 'headline' (or text_col).
    text_col : str
        Column in news_df containing text for sentiment.
    date_col : str
        Date column (should align with df).
    """
    news_df = news_df.copy()
    news_df["sentiment"] = compute_sentiment_score(news_df[text_col].fillna("").tolist())

    # Daily average sentiment
    daily_sentiment = news_df.groupby(date_col)["sentiment"].mean().reset_index()

    # Normalize to [0,1]
    s_min, s_max = daily_sentiment["sentiment"].min(), daily_sentiment["sentiment"].max()
    daily_sentiment["sentiment"] = (daily_sentiment["sentiment"] - s_min) / (s_max - s_min + 1e-9)

    # Merge back to price df
    df = df.merge(daily_sentiment, on="date", how="left")
    df["sentiment"] = df["sentiment"].fillna(0)  # fill missing days

    return df
