"""
Project: Sales Data Analysis (Week 3)
Description: Loads sales dataset, cleans data, computes key business metrics,
             and generates formatted terminal outputs and summary statistics.
"""

import pandas as pd

def load_and_clean_data(file_path):
    """Loads CSV dataset and performs basic data cleaning checks."""
    print("[-] Loading dataset...")
    df = pd.read_csv(file_path)
    
    # Display dataset dimensions
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Check for missing values
    missing_values = df.isnull().sum().sum()
    print(f"Missing Values Found: {missing_values}")
    
    # Check for duplicate rows
    duplicates = df.duplicated().sum()
    print(f"Duplicate Rows Found: {duplicates}")
    
    if duplicates > 0:
        df = df.drop_duplicates()
        print("Duplicates removed successfully.")
        
    return df

def analyze_sales(df):
    """Calculates core business metrics and regional breakdowns."""
    print("\n" + "="*40)
    print("--- SALES PERFORMANCE REPORT ---")
    print("="*40)
    
    # 1. Total Revenue
    total_revenue = df['Total_Sales'].sum()
    print(f"Total Revenue: ₹{total_revenue:,.2f}")
    
    # 2. Total Quantity Sold
    total_units = df['Quantity'].sum()
    print(f"Total Units Sold: {total_units:,}")
    
    # 3. Best-Selling Product by Revenue
    product_performance = df.groupby('Product').agg({
        'Total_Sales': 'sum',
        'Quantity': 'sum'
    }).reset_index().sort_values(by='Total_Sales', ascending=False)
    
    best_product = product_performance.iloc[0]
    print(f"\nBest-Selling Product (by Revenue): {best_product['Product']} (₹{best_product['Total_Sales']:,.2f})")
    
    print("\n--- Product Performance Breakdown ---")
    print(product_performance.to_string(index=False))
    
    # 4. Regional Sales Breakdown
    regional_performance = df.groupby('Region').agg({
        'Total_Sales': 'sum',
        'Quantity': 'sum'
    }).reset_index().sort_values(by='Total_Sales', ascending=False)
    
    print("\n--- Regional Sales Breakdown ---")
    print(regional_performance.to_string(index=False))
    
    return product_performance, regional_performance

if __name__ == "__main__":
    # File path for dataset
    file_name = 'sales_data (1).csv'
    
    # Run pipeline
    dataframe = load_and_clean_data(file_name)
    analyze_sales(dataframe)