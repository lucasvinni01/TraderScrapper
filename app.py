import streamlit as st
from functions.plot_ts import plot

st.title('Histórico de cotações')
st.write('Acompanhe o histórico de cotações')

ticker = st.sidebar.text_input('Escolha seu ticker:', value= 'AAPL')

figure = plot(ticker)
st.plotly_chart(figure)