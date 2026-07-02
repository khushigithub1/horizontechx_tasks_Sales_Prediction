import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots
import joblib
import os

# ==========================================================
# LOAD MODEL
# ==========================================================

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "random_forest_sales.pkl"
)

model = joblib.load(MODEL_PATH)

FEATURES = ["TV", "Radio", "Newspaper"]

feature_importance = model.feature_importances_

# ==========================================================
# COMMON LAYOUT
# ==========================================================

def update_theme(fig):

    fig.update_layout(

        autosize=True,

        height=400,

        paper_bgcolor="#161b22",

        plot_bgcolor="#161b22",

        font=dict(
            color="white",
            family="Segoe UI"
        ),

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        title_x=0.5,

        hovermode="closest"

    )

    fig.update_xaxes(

        showgrid=True,

        gridcolor="#30363d",

        zeroline=False

    )

    fig.update_yaxes(

        showgrid=True,

        gridcolor="#30363d",

        zeroline=False

    )

    return fig


# ==========================================================
# TV VS SALES
# ==========================================================

def tv_sales_chart(df):

    fig = px.scatter(

        df,

        x="TV",

        y="Sales",

        color="Sales",

        color_continuous_scale="Blues",

        size="Sales",

        template="plotly_dark"

    )

    fig.update_traces(marker=dict(line=dict(width=1,color="white")))

    return update_theme(fig)


# ==========================================================
# RADIO VS SALES
# ==========================================================

def radio_sales_chart(df):

    fig = px.scatter(

        df,

        x="Radio",

        y="Sales",

        color="Sales",

        size="Sales",

        color_continuous_scale="Greens",

        template="plotly_dark"

    )

    fig.update_traces(marker=dict(line=dict(width=1,color="white")))

    return update_theme(fig)


# ==========================================================
# NEWSPAPER VS SALES
# ==========================================================

def newspaper_sales_chart(df):

    fig = px.scatter(

        df,

        x="Newspaper",

        y="Sales",

        color="Sales",

        size="Sales",

        color_continuous_scale="Oranges",

        template="plotly_dark"

    )

    fig.update_traces(marker=dict(line=dict(width=1,color="white")))

    return update_theme(fig)


# ==========================================================
# SALES DISTRIBUTION
# ==========================================================

def sales_distribution_chart(df):

    fig = px.histogram(

        df,

        x="Sales",

        nbins=20,

        color_discrete_sequence=["#58a6ff"],

        template="plotly_dark"

    )

    return update_theme(fig)


# ==========================================================
# CORRELATION HEATMAP
# ==========================================================

def correlation_heatmap(df):

    corr = df.corr(numeric_only=True)

    fig = px.imshow(

        corr,

        text_auto=True,

        color_continuous_scale="RdBu",

        aspect="auto"

    )

    return update_theme(fig)


# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

def feature_importance_chart():

    fig = px.bar(

        x=feature_importance,

        y=FEATURES,

        orientation="h",

        color=feature_importance,

        color_continuous_scale="Viridis",

        template="plotly_dark"

    )

    fig.update_layout(

        coloraxis_showscale=False

    )

    return update_theme(fig)


# ==========================================================
# GAUGE CHART
# ==========================================================

def gauge_chart(prediction):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=prediction,

            number={

                "suffix":" M",

                "font":{"size":40}

            },

            title={

                "text":"Predicted Sales"

            },

            gauge={

                "axis":{"range":[0,30]},

                "bar":{"color":"#58a6ff"},

                "steps":[

                    {"range":[0,10],"color":"#f85149"},

                    {"range":[10,20],"color":"#ffa657"},

                    {"range":[20,30],"color":"#3fb950"}

                ]

            }

        )

    )

    fig.update_layout(

        paper_bgcolor="#161b22",

        font=dict(color="white")

    )

    return fig