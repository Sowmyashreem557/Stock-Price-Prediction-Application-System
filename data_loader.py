import yfinance as yf
import streamlit as st

@st.cache_resource
def download_data(stock_symbol, start_date, end_date):
    try:
        df = yf.download(
            stock_symbol,
            start=start_date,
            end=end_date,
            progress=False,
            auto_adjust=False
        )

        if df.empty:
            st.warning(f"No data found for {stock_symbol}.")
            return None

        st.sidebar.success(f"Data fetched for {stock_symbol}")
        return df

    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None
