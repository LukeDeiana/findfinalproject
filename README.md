# F.I.N.D.
**F.I.N.D. - Financial Insight through Numerical Data** is a Python-based tool designed to extract, analyze, and visualize financial data for Tesla (TSLA) and GameStop (GME). Leveraging powerful libraries such as `yfinance`, `requests`, `BeautifulSoup`, and `plotly`, this project automates the retrieval of historical stock prices and quarterly revenue data, transforming it into interactive dashboards for actionable financial insights.

## Key Features
- **Data Extraction**:  
  - Historical stock data for Tesla and GameStop is fetched using the `yfinance` library.  
  - Quarterly revenue data is scraped from web sources using `BeautifulSoup` and processed for analysis.  

- **Data Processing**:  
  - Stock data is cleaned and structured, with the first five rows readily accessible for review.  
  - Revenue data is refined by removing currency symbols and commas, converting it to numeric format, and filtering out missing or invalid entries.  

- **Visualization**:  
  - Interactive dual-axis graphs are generated with `plotly`, showcasing stock price trends alongside revenue data up to June 2021.  
  - Visualizations are saved as HTML files for standalone viewing or can be displayed inline in Jupyter Notebook.  
