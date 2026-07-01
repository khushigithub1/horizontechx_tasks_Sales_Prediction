import pandas as pd

from dash import html, Input, Output, State
from dash.exceptions import PreventUpdate

from charts import gauge_chart


# ==========================================================
# REGISTER CALLBACKS
# ==========================================================

def register_callbacks(app, model):

    # ======================================================
    # SALES PREDICTION CALLBACK
    # ======================================================

    @app.callback(
        Output("prediction-value", "children"),
        Output("prediction-gauge", "figure"),
        Output("business-insights", "children"),

        Input("predict-button", "n_clicks"),

        State("tv-slider", "value"),
        State("radio-slider", "value"),
        State("news-slider", "value"),

        prevent_initial_call=True
    )

    def predict_sales(n_clicks, tv, radio, news):

        if not n_clicks:
            raise PreventUpdate

        # -------------------------------------
        # Create Input DataFrame
        # -------------------------------------

        input_df = pd.DataFrame({
            "TV": [tv],
            "Radio": [radio],
            "Newspaper": [news]
        })

        # -------------------------------------
        # Prediction
        # -------------------------------------

        prediction = model.predict(input_df)[0]

        # -------------------------------------
        # Gauge Chart
        # -------------------------------------

        gauge = gauge_chart(prediction)

        # -------------------------------------
        # Business Insights
        # -------------------------------------

        insights = []

        # TV Analysis
        if tv >= 200:
            insights.append(
                "📺 TV advertising investment is excellent and expected to drive strong sales."
            )
        elif tv >= 120:
            insights.append(
                "📺 TV advertising budget is well balanced."
            )
        else:
            insights.append(
                "📺 Consider increasing the TV advertising budget."
            )

        # Radio Analysis
        if radio >= 30:
            insights.append(
                "📻 Radio advertising provides good customer reach."
            )
        else:
            insights.append(
                "📻 Increasing Radio advertisements may improve sales."
            )

        # Newspaper Analysis
        if news >= 40:
            insights.append(
                "📰 Newspaper spending is relatively high. Monitor ROI carefully."
            )
        else:
            insights.append(
                "📰 Newspaper budget is under control."
            )

        # Sales Prediction
        if prediction >= 20:
            insights.append(
                "🚀 Excellent expected sales performance."
            )

        elif prediction >= 15:
            insights.append(
                "📈 Good sales are expected."
            )

        else:
            insights.append(
                "⚠ Predicted sales are below average. Consider increasing advertising investment."
            )

        # Best Channel Recommendation
        insights.append(
            "💡 Recommendation: Focus primarily on TV advertising since it has the highest impact on sales."
        )

        insight_component = html.Div(

    className="insight-content",

    children=[

        html.Div(

            text,

            className="insight-item"

        )

        for text in insights

    ]

)

        return (

            f"{prediction:.2f} Million",

            gauge,

            insight_component

        )

    # ======================================================
    # DOWNLOAD PREDICTION REPORT
    # ======================================================

    @app.callback(

        Output("download-prediction", "data"),

        Input("download-btn", "n_clicks"),

        State("tv-slider", "value"),
        State("radio-slider", "value"),
        State("news-slider", "value"),

        prevent_initial_call=True

    )

    def download_prediction(n_clicks, tv, radio, news):

        if not n_clicks:
            raise PreventUpdate

        input_df = pd.DataFrame({

            "TV": [tv],
            "Radio": [radio],
            "Newspaper": [news]

        })

        prediction = model.predict(input_df)[0]

        report = pd.DataFrame({

            "TV Advertisement Budget ($1000)": [tv],

            "Radio Advertisement Budget ($1000)": [radio],

            "Newspaper Advertisement Budget ($1000)": [news],

            "Predicted Sales (Million $)": [round(prediction, 2)]

        })

        return {

            "content": report.to_csv(index=False),

            "filename": "Sales_Prediction_Report.csv"

        }