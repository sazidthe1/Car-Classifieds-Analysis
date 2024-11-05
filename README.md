# 🚘 Car Classifieds Dashboard: Explore Trends & Insights 📈

<p align="center">
  <a href="License">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="Python">
    <img src="https://img.shields.io/badge/Python-3.12%2B-blue.svg"></a>
  <a href="Status">
    <img src="https://img.shields.io/badge/Status-Completed-brightgreen.svg"></a>
</p>

This project showcases a comprehensive web-based dashboard using Streamlit and Plotly, which visualizes key trends in a car classifieds dataset. The dashboard provides insights into price distribution, car categories, engine types, and other important features to aid in data-driven analysis of car listings.

## App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://car-classifieds-dashboard.streamlit.app)

## Project Overview

The `car_cleaned_data.csv` file contains information on car listings with the following features:
- `Source Id`, `Title`, `Make`, `Model`, `Category`, `Engine Type`, `Power`, `Capacity`, `Transmission`, `Fuel`, `Construction Year`, `Mileage`, and `Price Gross`

## Features

- **Interactive Filters**: Users can filter car listings based on make, fuel type, and transmission, allowing a customized dataset view.
- **Visualizations**:
  - **Distribution of Car Categories**: A bar chart illustrating the number of cars for each category.
  - **Distribution of Engine Types**: A bar chart depicting the number of cars for each engine type.
  - **Price Distribution by Engine Type**: A box plot showing how prices vary across different engine types.
  - **Distribution of Fuel Types**: A horizontal bar plot highlighting the distribution of cars based on fuel type.
  - **Relationship Between Engine Power and Price**: A scatter plot revealing how car power influences price.
  - **Distribution of Mileage vs. Price by Fuel Type**: A scatter plot to examine how mileage and price are distributed for various fuel types.

## Visualizations

1. **Distribution of Car Categories**  
   This visualization highlights the number of cars in each category, such as Saloon, Estate Car, and Limousine. It provides a clear understanding of the prevalent types of cars listed.

   ![Viz 1](https://github.com/sazidthe1/Car-Classifieds-Analysis/raw/main/viz%201.png)

3. **Distribution of Engine Types**  
   This chart shows the count of car listings for each engine type. It helps identify which engine types are more common, indicating potential buyer preferences or market availability.

   ![Viz 2](https://github.com/sazidthe1/Car-Classifieds-Analysis/raw/main/viz%202.png)

5. **Price Distribution by Engine Type**  
   The box plot reveals how car prices are distributed across different engine types, helping identify the variations in pricing and potential outliers.

   ![Viz 3](https://github.com/sazidthe1/Car-Classifieds-Analysis/raw/main/viz%203.png)

7. **Distribution of Fuel Types**  
   This count plot shows the frequency of different fuel types in the listings. It helps assess which fuel types dominate the market and may influence pricing or demand.

   ![Viz 4](https://github.com/sazidthe1/Car-Classifieds-Analysis/raw/main/viz%204.png)

9. **Relationship Between Engine Power and Price**  
   A scatter plot demonstrating the correlation between engine power and car price. This plot can indicate whether higher-powered cars generally have higher price points.

   ![Viz 5](https://github.com/sazidthe1/Car-Classifieds-Analysis/raw/main/viz%205.png)

11. **Distribution of Mileage vs. Price by Fuel Type**  
   This scatter plot explores the distribution of mileage and price, segmented by fuel type. It provides insights into how fuel efficiency (mileage) and pricing interact across different fuel categories.

![Viz 6](https://github.com/sazidthe1/Car-Classifieds-Analysis/raw/main/viz%206.png)

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sazidthe1/Car-Classifieds-Analysis
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run car_classifieds_dashboard.py
   ```

5. **Open the app**: The app will open in your browser at `http://localhost:8501`.

## Project Structure

- `car_classifieds_dashboard.py`: The main script for the Streamlit app.
- `car_cleaned_data.csv`: The cleaned dataset used for visualizations.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python packages required to run the app.

## Prerequisite Libraries

All Python libraries used in the creation of this dashboard app can be found in the file `requirements.txt`.

## Future Improvements

- Adding more interactive charts and filters.
- Integrating advanced analytics like predictive pricing models.
- Enhancing the UI for better user experience.

## License

This project is licensed under the MIT License.
