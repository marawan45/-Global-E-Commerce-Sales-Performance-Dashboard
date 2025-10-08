# 💰 Global E-Commerce Sales Performance Dashboard

A comprehensive business intelligence dashboard built to analyze and visualize e-commerce sales performance across multiple dimensions including time, geography, product categories, and customer segments.

<img width="1334" height="714" alt="لقطة شاشة 2025-10-08 174301" src="https://github.com/user-attachments/assets/12db9ce7-3ff9-4a82-86a6-2bc3c36ddff6" />
<img width="1291" height="726" alt="لقطة شاشة 2025-10-08 174344" src="https://github.com/user-attachments/assets/4aa9676c-9c95-4208-93a3-ab37f3ba91ed" />


## 📊 Overview

This project transforms raw Superstore sales data into actionable insights through automated data cleaning, feature engineering, and interactive visualizations. The dashboard provides real-time metrics and trend analysis to support data-driven decision-making for e-commerce operations.

## ✨ Key Features

## Data Processing
- **Automated Data Cleaning Pipeline**: Handles missing values, data type conversions, and outlier detection
- **Feature Engineering**: Creates derived metrics including profit margins, shipping efficiency, and sales per unit
- **Date Intelligence**: Extracts temporal features (Year, Month) for time-series analysis
- **Robust Error Handling**: Gracefully manages data quality issues with configurable fallback strategies

## Dashboard Metrics
- **Delayed Orders Tracking**: Monitor 2K delayed shipments
- **Shipping Performance**: Average 3.96 days shipping time
- **Financial KPIs**: 
  - Total Profit: $286.40K
  - Total Sales: $2.30M
  - Profit Margin: 120.24K
- **Multi-dimensional Analysis**: Filter by Region and Category

### Visualizations
1. **Profit Trend Analysis**: Monthly profit progression with clear seasonal patterns
2. **Category Performance**: Sales and profit margin comparison across product categories
3. **Temporal Patterns**: Year/Quarter/Month/Day granularity for sales trends
4. **Customer Segmentation**: Sales distribution across Consumer, Corporate, and Home Office segments
5. **Geographic Heatmap**: City-level sales performance with global coverage

## 🛠️ Technology Stack

### Data Processing
- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

### Dashboard (Assumed)
- **Tableau/Power BI**: Interactive visualization platform
- **Microsoft Azure**: Map visualization service

## 📁 Project Structure

```
global-ecommerce-dashboard/
├── Data cleaning.py          # Main data processing script
├── Sample - Superstore.csv   # Raw data source
├── cleaned_superstore.csv    # Processed dataset
└── README.md                 # Project documentation
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/global-ecommerce-dashboard.git
cd global-ecommerce-dashboard
```

2. Place your raw data file in the designated directory:
```
C:/Users/maraw/Downloads/Global E-Commerce Sales Performance Dashboard/
```

3. Run the data cleaning script:
```bash
python "Data cleaning.py"
```

### Data Processing Pipeline

The `clean_dataframe()` function performs the following operations:

1. **Whitespace Trimming**: Removes leading/trailing spaces from text columns
2. **Date Parsing**: Converts date columns to datetime format with error handling
3. **Numeric Coercion**: Ensures numerical columns have correct data types
4. **Missing Value Imputation**:
   - Numeric columns: Mean imputation
   - Categorical columns: Mode imputation
   - ID/Name fields: 'Unknown' placeholder
5. **Feature Creation**:
   - Shipping Days
   - Profit Margin (%)
   - Discount Amount
   - Net Sales
   - Sales/Profit per Quantity

## 📈 Calculated Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| Shipping Days | Ship Date - Order Date | Logistics efficiency |
| Profit Margin (%) | (Profit / Sales) × 100 | Profitability analysis |
| Discount Amount | Sales × Discount | Promotion impact |
| Net Sales | Sales - Discount Amount | True revenue |
| Sales per Quantity | Sales / Quantity | Unit economics |
| Profit per Quantity | Profit / Quantity | Unit profitability |

## 🎯 Use Cases

- **Operations Management**: Track delayed orders and optimize shipping times
- **Financial Planning**: Monitor profit margins and identify high-performing categories
- **Marketing Strategy**: Analyze customer segments and seasonal trends
- **Geographic Expansion**: Identify high-potential markets through city-level analysis
- **Inventory Optimization**: Understand product category performance

## 📊 Dashboard Insights

### Key Findings
- **Technology** leads in sales performance
- **Consumer segment** represents 50.56% of total sales
- **December-March** shows peak profit periods with subsequent decline
- **North America** demonstrates concentrated market penetration
- Average profit margin indicates healthy business sustainability

## 🔧 Customization

### Modifying Data Cleaning Parameters

```python
# Custom date columns
cleaned = clean_dataframe(df, date_cols=['Custom Date 1', 'Custom Date 2'])

# Adjust file paths
file_path = r"your/custom/path/data.csv"
out_path = r"your/output/path/cleaned_data.csv"
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Superstore dataset for providing comprehensive e-commerce data
- Microsoft Azure for mapping capabilities
- The Python data science community

## 📧 Contact

For questions or feedback, please open an issue or contact [your.email@example.com](mailto:your.email@example.com)

---

⭐ **Star this repository if you find it helpful!**
