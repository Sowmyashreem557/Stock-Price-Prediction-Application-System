import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt

scaler = StandardScaler()

def run_model(model, stock_data, num_days, st, symbol):
    df = stock_data[['Close']].copy()
    df['Predicted_Close'] = df['Close'].shift(-num_days)

    X = scaler.fit_transform(df[['Close']].values)
    X_forecast = X[-num_days:]
    X = X[:-num_days]
    y = df['Predicted_Close'].dropna().values

    if len(y) < num_days:
        st.error(f"Not enough data. Try fewer days.")
        return

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    st.write(f"**R² Score:** {r2_score(y_test, preds):.4f}")
    st.write(f"**MAE:** {mean_absolute_error(y_test, preds):.4f}")

    forecast = model.predict(X_forecast)
    forecast_dates = pd.date_range(df.index[-1] + pd.Timedelta(days=1),
                                   periods=num_days, freq='B')

    forecast_df = pd.DataFrame({
        'Predicted Close': forecast
    }, index=forecast_dates)

    return forecast_df
