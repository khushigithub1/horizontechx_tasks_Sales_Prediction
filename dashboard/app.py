"""
=========================================================
Sales Intelligence Platform
Author : Akanksha Srivastava
Project : Sales Prediction using Machine Learning
Framework : Dash + Plotly
=========================================================
"""

import os
import joblib
import pandas as pd
from dash import Dash

# -------------------------------
# Import Project Files
# -------------------------------

from layouts import create_layout
from callbacks import register_callbacks

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = os.path.dirname(__file__)

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "Advertising.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "random_forest_sales.pkl"
)

# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_csv(DATA_PATH)

if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)

# ==========================================================
# LOAD MODEL
# ==========================================================

model = joblib.load(MODEL_PATH)

# ==========================================================
# CREATE DASH APP
# ==========================================================

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    title="Sales Intelligence Platform"
)

server = app.server

# ==========================================================
# APP LAYOUT
# ==========================================================

app.layout = create_layout(df)

# ==========================================================
# REGISTER CALLBACKS
# ==========================================================

register_callbacks(app, model)

# ==========================================================
# RUN SERVER
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("🚀 Sales Intelligence Platform Started Successfully")
    print("=" * 60)
    print("Dashboard URL : http://127.0.0.1:8050")
    print("=" * 60)

    app.run(
        debug=True,
        host="127.0.0.1",
        port=8050
    )