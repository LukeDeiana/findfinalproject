import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
import plotly.io as pio
from IPython.display import display, HTML

# Imposta il renderer di default per Plotly
pio.renderers.default = "iframe"

# Ignora i warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Definizione della funzione make_graph
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        subplot_titles=("Historical Share Price", "Historical Revenue"), 
                        vertical_spacing=0.3)
    stock_data_specific = stock_data[stock_data['Date'] <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data['Date'] <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific['Date']), 
                             y=stock_data_specific['Close'].astype("float"), 
                             name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific['Date']), 
                             y=revenue_data_specific['Revenue'].astype("float"), 
                             name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible=True)
    return fig

# Question 1: Estrazione dei dati azionari di Tesla
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print("Primi cinque righe dei dati azionari di Tesla:")
print(tesla_data.head())

# Question 2: Web scraping dei dati di fatturato di Tesla
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")
tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])
for row in soup.find_all("tbody")[1].find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text.replace('$', '').replace(',', '')
    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({'Date': [date], 'Revenue': [revenue]})], ignore_index=True)
tesla_revenue['Revenue'] = pd.to_numeric(tesla_revenue['Revenue'], errors='coerce')
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print("Ultime cinque righe dei dati di fatturato di Tesla:")
print(tesla_revenue.tail())

# Question 3: Estrazione dei dati azionari di GameStop
gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="max")
gme_data.reset_index(inplace=True)
print("Primi cinque righe dei dati azionari di GameStop:")
print(gme_data.head())

# Question 4: Web scraping dei dati di fatturato di GameStop
url_gme = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_gme = requests.get(url_gme).text
soup_gme = BeautifulSoup(html_data_gme, "html.parser")
gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])
for row in soup_gme.find_all("tbody")[1].find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text.replace('$', '').replace(',', '')
    gme_revenue = pd.concat([gme_revenue, pd.DataFrame({'Date': [date], 'Revenue': [revenue]})], ignore_index=True)
gme_revenue['Revenue'] = pd.to_numeric(gme_revenue['Revenue'], errors='coerce')
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
print("Ultime cinque righe dei dati di fatturato di GameStop:")
print(gme_revenue.tail())

# Question 5: Grafico dei dati di Tesla
make_graph(tesla_data, tesla_revenue, "Tesla")

# Question 6: Grafico dei dati di GameStop
make_graph(gme_data, gme_revenue, "GameStop")

# Crea e salva il grafico di Tesla
fig_tesla = make_graph(tesla_data, tesla_revenue, "Tesla")
fig_tesla.write_html("grafico_tesla.html")

# Crea e salva il grafico di GameStop
fig_gamestop = make_graph(gme_data, gme_revenue, "GameStop")
fig_gamestop.write_html("grafico_gamestop.html")

