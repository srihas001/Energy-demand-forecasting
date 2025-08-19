import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
models = {
    "SARIMAX": pickle.load(open("sarima_model.pkl", "rb")),
    "XGBoost": pickle.load(open("xgboost_model.pkl", "rb"))
}

st.title("⚡ Energy Demand Forecasting App")
uploaded_file = st.file_uploader("📂 Upload your energy demand CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['Datetime'], index_col='Datetime')
    st.write("📊 Data Preview:", df.head())
    model_choice = st.selectbox("🔎 Choose a Model", list(models.keys()))
    model = models[model_choice]
    train = df.iloc[:-30]
    test = df.iloc[-30:]
    if model_choice == "SARIMAX":
        pred = model.get_forecast(steps=30).predicted_mean
    else:  # XGBoost
    
        df = df.copy()
        df.index = pd.to_datetime(df.index)
        df_features = pd.DataFrame({
                                'hour': df.index.hour,
                                'day_of_week': df.index.dayofweek,
                                'quarter': df.index.quarter,
                                'month': df.index.month,
                                'year': df.index.year,
                                'dayofyear': df.index.dayofyear
                              })
        pred = model.predict(df_features.iloc[-30:])
 
    st.subheader("📈 Forecasted Energy Demand (Next 30 Steps)")
    st.line_chart(pred)
    mae = mean_absolute_error(test["PJME_MW"], pred)
    mape = mean_absolute_percentage_error(test["PJME_MW"], pred) * 100
    rmse = np.sqrt(mean_squared_error(test["PJME_MW"], pred))

    st.subheader("📊 Model Performance Metrics")
    st.write(f"**MAE  :** {mae:.2f}")
    st.write(f"**MAPE :** {mape:.2f}%")
    st.write(f"**RMSE :** {rmse:.2f}")
