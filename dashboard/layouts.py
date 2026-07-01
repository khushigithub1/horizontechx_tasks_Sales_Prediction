from dash import html, dcc
from dash import dash_table

from charts import (
    tv_sales_chart,
    radio_sales_chart,
    newspaper_sales_chart,
    sales_distribution_chart,
    correlation_heatmap,
    feature_importance_chart,
    gauge_chart
)


def create_layout(df):

    return html.Div(

        className="main-container",

        children=[

            # ---------------- Sidebar ----------------

            create_sidebar(),

            # ---------------- Main Content ----------------

            html.Div(

                className="content",
                    children=[

                        create_header(),

                        create_kpi_cards(df),

                        html.Br(),

                        create_analytics(df),

                        html.Br(),

                        create_prediction_panel(),

                        html.Br(),

                        create_business_insights(),

                        html.Br(),

                        create_reports()

                    ]

            )

        ]

    )

def create_sidebar():

    return html.Div(

        className="sidebar",

        children=[

            html.Div(

                className="logo",

                children=[

                    html.H2("📊"),

                    html.H3("Sales AI")

                ]

            ),

            html.Hr(),

            html.Div(

                className="menu",

                children=[

                    html.A("🏠 Dashboard", href="#"),

                    html.A("📈 Analytics", href="#analytics"),

                    html.A("🤖 Prediction", href="#prediction"),

                    html.A("💡 Insights", href="#insights"),

                    html.A("📥 Reports", href="#reports"),

                    html.A("⚙ Settings", href="#")

                ]

            )

        ]

    )

def create_header():

    return html.Div(

        className="header",

        children=[

            html.Div(

                children=[

                    html.H1("📊 Sales Intelligence Dashboard"),

                    html.P(

                        "Advertising Sales Prediction using Machine Learning"

                    )

                ]

            ),

            html.Div(

                children=[

                    html.Div(

                        id="live-clock",

                        className="clock"

                    ),

                    html.Br(),

                    html.Div(
                        [
                            html.H4("👩‍💻 Data Science Dashboard"),
                            html.P("Random Forest | Plotly Dash")
                        ]
                    )
                ]

            )

        ]

    )

def create_kpi_cards(df):

    return html.Div(

        className="kpi-grid",

        children=[

            html.Div(

                className="kpi-card",

                children=[

                    html.Div("📁", className="kpi-icon"),

                    html.P("Total Records",

                           className="kpi-title"),

                    html.H2(

                        len(df),

                        className="kpi-value"

                    )

                ]

            ),

            html.Div(

                className="kpi-card",

                children=[

                    html.Div("📺", className="kpi-icon"),

                    html.P("Average TV Budget"),

                    html.H2(

                        f"{df.TV.mean():.1f}K"

                    )

                ]

            ),

            html.Div(

                className="kpi-card",

                children=[

                    html.Div("📈", className="kpi-icon"),

                    html.P("Average Sales"),

                    html.H2(

                        f"{df.Sales.mean():.2f}"

                    )

                ]

            ),

            html.Div(

                className="kpi-card",

                children=[

                    html.Div("🎯", className="kpi-icon"),

                    html.P("Model Accuracy"),

                    html.H2("98.13%")

                ]

            )

        ]

    )

def create_analytics(df):

    return html.Div(

        id="analytics",

        className="analytics-section",

        children=[

            html.H2(
                "📈 Advertising Analytics",
                className="section-title"
            ),

            html.Div(

                className="chart-grid",

                children=[

                    chart_card(
                        "📺 TV Advertisement vs Sales",
                        tv_sales_chart(df)
                    ),

                    chart_card(
                        "🔥 Correlation Heatmap",
                        correlation_heatmap(df)
                    ),

                    chart_card(
                        "📻 Radio Advertisement vs Sales",
                        radio_sales_chart(df)
                    ),

                    chart_card(
                        "🌳 Feature Importance",
                        feature_importance_chart()
                    ),

                    chart_card(
                        "📊 Sales Distribution",
                        sales_distribution_chart(df)
                    ),

                    chart_card(
                        "📰 Newspaper Advertisement vs Sales",
                        newspaper_sales_chart(df)
                    )

                ]

            )

        ]

    )

def chart_card(title, figure):

    return html.Div(

        className="chart-card",

        children=[

            html.H4(title),

            dcc.Graph(

                figure=figure,

                config={"displayModeBar": False}

            )

        ]

    )

def create_prediction_panel():

    return html.Div(

        id="prediction",

        className="prediction-section",

        children=[

            html.H2(
                "🤖 Live Sales Prediction",
                className="section-title"
            ),

            html.Div(

                className="prediction-grid",

                children=[

                    # LEFT PANEL
                    html.Div(

                        className="prediction-left",

                        children=[

                            html.Label("📺 TV Advertisement Budget"),

                            dcc.Slider(
                                id="tv-slider",
                                min=0,
                                max=300,
                                step=1,
                                value=150,
                                tooltip={"placement": "bottom"}
                            ),

                            html.Br(),

                            html.Label("📻 Radio Advertisement Budget"),

                            dcc.Slider(
                                id="radio-slider",
                                min=0,
                                max=50,
                                step=1,
                                value=25,
                                tooltip={"placement": "bottom"}
                            ),

                            html.Br(),

                            html.Label("📰 Newspaper Advertisement Budget"),

                            dcc.Slider(
                                id="news-slider",
                                min=0,
                                max=120,
                                step=1,
                                value=40,
                                tooltip={"placement": "bottom"}
                            ),

                            html.Br(),

                            html.Button(

                                "🚀 Predict Sales",

                                id="predict-button",

                                className="predict-btn"

                            )

                        ]

                    ),

                    # RIGHT PANEL
                    html.Div(

                        className="prediction-right",

                        children=[

                            html.H3("Predicted Sales"),

                            html.H1(

                                "0.00 Million",

                                id="prediction-value",

                                className="prediction-value"

                            ),

                            dcc.Graph(

                                id="prediction-gauge",

                                figure=gauge_chart(0),

                                config={"displayModeBar": False}

                            )

                        ]

                    )

                ]

            )

        ]

    )

def create_business_insights():

    return html.Div(

        id="insights",

        className="insight-section",

        children=[

            html.H2("💡 AI Business Insights"),

            html.Div(

                id="business-insights",

                className="insight-box",

                children=[

                    html.Div("🤖 AI Analysis", className="insight-title"),

                    html.P(
                        "Click the 'Predict Sales' button to generate business recommendations."
                    )

                ]

            )

        ]

    )


from dash import html, dcc

def create_reports():

    return html.Div(

        id="reports",

        className="report-section",

        children=[

            html.H2(
                "📥 Reports & Export Center",
                className="section-title"
            ),

            html.Div(

                className="report-card",

                children=[

                    html.Div(

                        className="report-header",

                        children=[

                            html.H3("📄 Sales Prediction Report"),

                            html.P(
                                "Export the latest machine learning prediction and advertising budget details."
                            )

                        ]

                    ),

                    html.Hr(),

                    html.Div(

                        className="report-info",

                        children=[

                            html.Div(

                                className="info-box",

                                children=[

                                    html.H4("📊 Report Type"),

                                    html.P("CSV Export")

                                ]

                            ),

                            html.Div(

                                className="info-box",

                                children=[

                                    html.H4("🤖 Model"),

                                    html.P("Random Forest")

                                ]

                            ),

                            html.Div(

                                className="info-box",

                                children=[

                                    html.H4("⚡ Status"),

                                    html.P("Ready")

                                ]

                            )

                        ]

                    ),

                    html.Br(),

                    html.Button(

                        "⬇ Download Prediction Report",

                        id="download-btn",

                        className="download-btn"

                    ),

                    dcc.Download(
                        id="download-prediction"
                    )

                ]

            )

        ]

    )