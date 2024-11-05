import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned dataset
data = pd.read_csv(r'car_cleaned_data.csv')

# Set up the page title
st.title("🚘 Car Classifieds Dashboard: Explore Trends & Insights 📈")

st.write("This dashboard provides an overview of car categories, engine types, price distribution, and other important features to aid in data-driven analysis of car listings.")

# Sidebar filters
st.sidebar.header("Filter Options")
make_filter = st.sidebar.multiselect("Select Car Make:", options=data['Make'].unique())
fuel_filter = st.sidebar.multiselect("Select Fuel Type:", options=data['Fuel'].unique())
transmission_filter = st.sidebar.multiselect("Select Transmission Type:", options=data['Transmission'].str.title().unique())

# Apply filters
filtered_data = data.copy()
if make_filter:
    filtered_data = filtered_data[filtered_data['Make'].isin(make_filter)]
if fuel_filter:
    filtered_data = filtered_data[filtered_data['Fuel'].isin(fuel_filter)]
if transmission_filter:
    filtered_data = filtered_data[filtered_data['Transmission'].isin(transmission_filter)]

# Show the filtered data (limit to 10 rows)
st.subheader("Filtered Data (Showing first 10 rows)")
st.write(filtered_data.head(10))

# Show the visualize data
st.subheader("Visualize Data")

# Visualization 1: Distribution of Car Categories
category_counts = filtered_data['Category'].value_counts()
fig1 = px.bar(
    x=category_counts.index,
    y=category_counts.values,
    #orientation='h',
    color=category_counts.index,
    labels={'x': 'Car Category', 'y': 'Number of Cars'},
    title='Viz 1: Distribution of Car Categories'
)
fig1.update_layout(xaxis=dict(tickangle=45))
st.plotly_chart(fig1)
st.write("**Comment**: The bar chart displays the number of cars available by category, highlighting which types of vehicles are most commonly listed.")

# Visualization 2: Distribution of Engine Types
engine_type_counts = filtered_data['Engine Type'].value_counts()
fig2 = px.bar(
    x=engine_type_counts.index,
    y=engine_type_counts.values,
    color=engine_type_counts.index,
    labels={'x': 'Engine Type', 'y': 'Number of Cars'},
    title='Viz 2: Distribution of Engine Types'
)
fig2.update_layout(xaxis=dict(tickangle=45))
st.plotly_chart(fig2)
st.write("**Comment**: This bar chart shows the distribution of different engine types in the dataset, indicating the most common engine types among the car listings.")

# Visualization 3: Price Distribution by Engine Type
fig3 = px.box(
    filtered_data,
    x='Engine Type',
    y='Price Gross',
    color='Engine Type',
    labels={'Price Gross': 'Price (Gross)', 'Engine Type': 'Engine Type'},
    title='Viz 3: Price Distribution by Engine Type'
)
fig3.update_layout(xaxis=dict(tickangle=45))
fig3.update_yaxes(range=[0, 120000]) # Set y-axis range from 0 to 120k
st.plotly_chart(fig3)
st.write("**Comment**: This box plot illustrates the distribution of car prices by engine type, providing insights into how price varies among different engine types and identifying outliers.")

# Visualization 4: Trends in Fuel Types
fuel_counts = filtered_data['Fuel'].value_counts().sort_values(ascending=True)
fig4 = px.bar(
    y=fuel_counts.index,
    x=fuel_counts.values,
    color=fuel_counts.index,
    labels={'y': 'Fuel Type', 'x': 'Number of Cars'},
    title='Viz 4: Distribution of Fuel Types'
)
fig4.update_layout(xaxis=dict(tickangle=45))
st.plotly_chart(fig4)
st.write("**Comment**: This horizental bar chart shows the distribution of cars by fuel type, indicating trends in fuel preferences among the listings.")

# Visualization 5: Relationship Between Engine Power and Price
fig5 = px.scatter(
    filtered_data,
    x='Power',
    y='Price Gross',
    color='Category',
    labels={'Power': 'Engine Power (HP)', 'Price Gross': 'Price (Gross)', 'Category': 'Car Category'},
    title='Viz 5: Relationship between Engine Power and Price',
    opacity=0.6
)
fig5.update_yaxes(range=[0, 120000]) # Set y-axis range from 0 to 120k
st.plotly_chart(fig5)
st.write("**Comment**: This scatter plot visualizes the relationship between engine power and price, suggesting that higher power typically correlates with higher prices for cars.")

# Visualization 6: Distribution of Mileage vs. Price by Fuel Type
fig6 = px.scatter(
    filtered_data,
    x='Mileage',
    y='Price Gross',
    color='Fuel',
    labels={'Mileage': 'Mileage (in km)', 'Price Gross': 'Price (Gross)', 'Fuel': 'Fuel Type'},
    title='Viz 6: Distribution of Mileage vs. Price by Fuel Type',
    opacity=0.6
)
fig6.update_xaxes(range=[0, 500000]) # Set y-axis range from 0 to 500k
fig6.update_yaxes(range=[0, 120000]) # Set y-axis range from 0 to 120k
st.plotly_chart(fig6)
st.write("**Comment**: This scatter plot depicts the distribution of mileage against price, colored by fuel type. It highlights how mileage affects price across different fuel types.")
