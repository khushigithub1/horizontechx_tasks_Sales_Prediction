"""
==========================================================
Sales Prediction Dashboard
Utility Functions
Author : Akanksha Srivastava
==========================================================
"""

from pathlib import Path
import pandas as pd
import numpy as np
import joblib

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

DATA_PATH = PROJECT_DIR / "data" / "Advertising.csv"
MODEL_PATH = PROJECT_DIR / "models" / "random_forest_sales.pkl"

# ==========================================================
# LOAD DATASET
# ==========================================================

def load_dataset():

    df = pd.read_csv(DATA_PATH)

    # Remove unwanted index column
    if "Unnamed: 0" in df.columns:
        df.drop("Unnamed: 0", axis=1, inplace=True)

    return df


# ==========================================================
# LOAD MODEL
# ==========================================================

def load_model():

    model = joblib.load(MODEL_PATH)

    return model


# ==========================================================
# KPI CALCULATIONS
# ==========================================================

def get_kpis(df):

    kpis = {

        "records": len(df),

        "avg_sales": round(df["Sales"].mean(),2),

        "max_sales": round(df["Sales"].max(),2),

        "min_sales": round(df["Sales"].min(),2),

        "avg_tv": round(df["TV"].mean(),2),

        "avg_radio": round(df["Radio"].mean(),2),

        "avg_newspaper": round(df["Newspaper"].mean(),2),

        "total_tv": round(df["TV"].sum(),2),

        "total_radio": round(df["Radio"].sum(),2),

        "total_newspaper": round(df["Newspaper"].sum(),2)

    }

    return kpis


# ==========================================================
# PREDICTION FUNCTION
# ==========================================================

def predict_sales(model, tv, radio, newspaper):

    sample = pd.DataFrame({

        "TV":[tv],

        "Radio":[radio],

        "Newspaper":[newspaper]

    })

    prediction = model.predict(sample)[0]

    return round(float(prediction),2)


# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

def feature_importance(model):

    try:

        importance = pd.DataFrame({

            "Feature":[
                "TV",
                "Radio",
                "Newspaper"
            ],

            "Importance":model.feature_importances_

        })

        importance.sort_values(

            by="Importance",

            ascending=False,

            inplace=True

        )

        return importance

    except:

        return pd.DataFrame()


# ==========================================================
# DATA SUMMARY
# ==========================================================

def dataset_summary(df):

    summary = {

        "Rows": df.shape[0],

        "Columns": df.shape[1],

        "Missing Values": int(df.isnull().sum().sum()),

        "Duplicate Rows": int(df.duplicated().sum())

    }

    return summary


# ==========================================================
# CORRELATION
# ==========================================================

def correlation_matrix(df):

    return df.corr(numeric_only=True)


# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

def business_insights(df):

    corr = df.corr(numeric_only=True)["Sales"].sort_values(ascending=False)

    tv = corr["TV"]

    radio = corr["Radio"]

    newspaper = corr["Newspaper"]

    insights = [

        f"TV Advertising Correlation : {tv:.2f}",

        f"Radio Advertising Correlation : {radio:.2f}",

        f"Newspaper Advertising Correlation : {newspaper:.2f}",

        "TV Advertising has the strongest impact on sales.",

        "Radio advertising positively supports TV campaigns.",

        "Newspaper advertising contributes the least.",

        "Increasing TV budget is likely to improve sales.",

        "Random Forest is selected as the final predictive model."

    ]

    return insights


# ==========================================================
# WHAT-IF SIMULATION
# ==========================================================

def what_if_analysis(model):

    scenarios = pd.DataFrame({

        "Scenario":[

            "Low Budget",

            "Medium Budget",

            "High Budget"

        ],

        "TV":[

            80,

            180,

            280

        ],

        "Radio":[

            15,

            30,

            45

        ],

        "Newspaper":[

            10,

            25,

            40

        ]

    })

    scenarios["Predicted Sales"] = model.predict(

        scenarios[["TV","Radio","Newspaper"]]

    )

    return scenarios


# ==========================================================
# EXPORT PREDICTION
# ==========================================================

def export_prediction(tv, radio, newspaper, prediction):

    result = pd.DataFrame({

        "TV":[tv],

        "Radio":[radio],

        "Newspaper":[newspaper],

        "Predicted Sales":[prediction]

    })

    return result