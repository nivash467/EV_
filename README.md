# ⚡ Electric Vehicle Adoption Tracker

An interactive Streamlit dashboard for analyzing Electric Vehicle (EV) adoption trends, charging infrastructure growth, and regional EV sales patterns using powerful data visualizations.

## 📌 Project Overview

The Electric Vehicle Adoption Tracker provides insights into EV adoption through interactive charts and dashboards. Users can explore EV registration growth, charging station distribution, and regional sales trends to better understand the expansion of electric mobility.

## 🚀 Features

### 📈 EV Registration Growth Trend
- Interactive line chart using Plotly.
- Visualizes EV sales growth over time.
- Compare adoption trends across different cities.

### 🏙️ Charging Stations by City
- Bar chart showing charging infrastructure availability.
- Helps identify cities with stronger EV support systems.

### 🔥 Regional EV Sales Heatmap
- Heatmap visualization using Seaborn.
- Displays EV registration intensity across regions and dates.
- Highlights high-adoption regions.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly Express
- Matplotlib
- Seaborn

## 📂 Project Structure

Electric-Vehicle-Adoption-Tracker/
│
├── app.py
├── ev_data.csv
├── requirements.txt
└── README.md

## 📊 Dataset Requirements

The dataset (`ev_data.csv`) should contain the following columns:

| Column | Description |
|---------|-------------|
| date | Date of EV registration |
| city | City name |
| region | Region name |
| ev_sales | Number of EV registrations/sales |
| charging_stations | Number of charging stations |

Example:

date,city,region,ev_sales,charging_stations
2024-01-01,Chennai,South,1200,50
2024-01-01,Bangalore,South,1500,65
2024-01-01,Mumbai,West,1800,70

## ⚙️ Installation

1. Clone the repository

git clone https://github.com/yourusername/electric-vehicle-adoption-tracker.git

cd electric-vehicle-adoption-tracker

2. Install dependencies

pip install -r requirements.txt

3. Run the Streamlit application

streamlit run app.py

## 📦 Required Libraries

streamlit
pandas
plotly
matplotlib
seaborn

## 🎯 Learning Outcomes

- Build interactive dashboards using Streamlit.
- Perform data analysis with Pandas.
- Create visualizations using Plotly and Seaborn.
- Analyze EV adoption and infrastructure trends.
- Understand dashboard development workflows.

## 🔮 Future Enhancements

- State-wise EV adoption comparison.
- Predictive analytics using Machine Learning.
- Real-time EV registration data integration.
- Advanced filtering and search options.
- Geographic map-based visualizations.

## 👨‍💻 Author

**Nivash M**

BE Computer Science and Engineering (AI & ML)

Interested in Artificial Intelligence, Data Science, Machine Learning, and Data Visualization.

⭐ If you found this project useful, consider starring the repository.
