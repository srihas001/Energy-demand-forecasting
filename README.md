# ⚡ Energy Demand Forecasting

A comprehensive machine learning project for forecasting energy demand using multiple advanced modeling techniques. This repository contains both a Streamlit web application and Jupyter notebook analysis for energy consumption prediction.

## 🎯 Project Overview

This project focuses on forecasting energy demand using historical hourly energy consumption data from PJM Interconnection (PJME). The system implements two distinct modeling approaches:

- **SARIMAX Model**: Statistical time series forecasting using Seasonal AutoRegressive Integrated Moving Average with eXogenous factors
- **XGBoost Model**: Machine learning approach using gradient boosting with engineered temporal features

## 🚀 Features

### Web Application (`app.py`)
- **Interactive Streamlit Interface**: User-friendly web application for energy demand forecasting
- **File Upload**: Support for CSV data uploads
- **Model Selection**: Choose between SARIMAX and XGBoost models
- **Real-time Forecasting**: Generate 30-step ahead predictions
- **Performance Metrics**: Display MAE, MAPE, and RMSE for model evaluation
- **Visualization**: Interactive charts showing forecasted energy demand

### Analysis Notebook (`Energy demand analysis.ipynb`)
- **Comprehensive Data Analysis**: Exploratory data analysis of energy consumption patterns
- **Feature Engineering**: Temporal feature extraction (hour, day, month, year, etc.)
- **Model Training**: Complete pipeline for both SARIMAX and XGBoost models
- **Performance Evaluation**: Detailed model comparison and metrics
- **Visualization**: Multiple plots for data understanding and model performance

## 📊 Dataset

The project uses the **PJME_hourly.csv** dataset containing:
- **Datetime**: Hourly timestamps from 2002-2018
- **PJME_MW**: Energy demand in Megawatts (MW)
- **Format**: Time series data with hourly granularity

## 🛠️ Technical Stack

### Core Dependencies
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning utilities and metrics

### Machine Learning Models
- **XGBoost**: Gradient boosting framework for regression
- **Statsmodels**: Statistical modeling (SARIMAX implementation)

### Data Processing
- **Datetime handling**: Advanced time series operations
- **Feature engineering**: Temporal feature extraction
- **Data visualization**: Matplotlib and Seaborn for plotting

## 📁 Project Structure

```
Energy-demand-forecasting/
├── app.py                          # Streamlit web application
├── Energy demand analysis.ipynb    # Jupyter notebook analysis
├── PJME_hourly.csv                # Energy consumption dataset
├── requirements.txt                # Python dependencies
├── sarima_model.pkl               # Trained SARIMAX model
├── xgboost_model.pkl              # Trained XGBoost model
└── README.md                      # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Energy-demand-forecasting
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

### Using the Web App

1. **Upload Data**: Use the file uploader to upload your energy demand CSV file
2. **Select Model**: Choose between SARIMAX or XGBoost
3. **View Results**: See the forecasted energy demand and performance metrics
4. **Analyze Performance**: Review MAE, MAPE, and RMSE scores

## 📈 Model Performance

### SARIMAX Model
- **MAE**: ~6,763 MW
- **MAPE**: ~23.39%
- **RMSE**: ~7,562 MW
- **Best for**: Long-term trends and seasonal patterns

### XGBoost Model
- **Features**: Hour, day of week, quarter, month, year, day of year
- **Best for**: Complex non-linear relationships and feature interactions

## 🔬 Methodology

### SARIMAX Implementation
- **Order**: (1,1,1) - ARIMA parameters
- **Seasonal Order**: (1,1,1,7) - Weekly seasonality
- **Training**: 2002-2017 data (5,694 days)
- **Testing**: 2017-2018 data (365 days)

### XGBoost Implementation
- **Feature Engineering**: Temporal features from datetime index
- **Cross-validation**: K-fold validation for robust model selection
- **Hyperparameter Tuning**: Optimized for energy demand prediction

## 📊 Data Visualization

The analysis includes comprehensive visualizations:
- **Time Series Plots**: Energy consumption over time
- **Hourly Patterns**: Box plots showing demand distribution by hour
- **Weekly Patterns**: Energy usage patterns across days
- **Model Performance**: Training vs. testing predictions with confidence intervals

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass before submitting



## 🙏 Acknowledgments

- **PJM Interconnection** for providing the energy consumption dataset
- **Open Source Community** for the excellent libraries and frameworks used
- **Contributors** who have helped improve this project

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the documentation in the Jupyter notebook
- Review the Streamlit app for usage examples

## 🔮 Future Enhancements

- [ ] Real-time data streaming capabilities
- [ ] Additional ML models (LSTM, Prophet, etc.)
- [ ] Automated hyperparameter tuning
- [ ] Model deployment to cloud platforms
- [ ] API endpoints for programmatic access
- [ ] Enhanced visualization dashboard
- [ ] Multi-region energy demand forecasting

---


