import pandas_datareader.wb as wb
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time

def create_g7_gdp_chart():
    """
    Fetches both Real GDP per Capita and Total Real GDP for G7 countries.
    Generates a figure with two subplots:
    1. GDP per Capita normalized to 2010=100.
    2. Total Real GDP in Trillions of US$.
    """
    # 1. Configuration
    g7_countries = ['CA', 'FR', 'DE', 'IT', 'JP', 'GB', 'US']
    
    # Define indicators:
    # NY.GDP.PCAP.KD = GDP per capita (constant 2015 US$)
    # NY.GDP.MKTP.KD = GDP (constant 2015 US$)
    indicators = {
        'NY.GDP.PCAP.KD': 'GDP_Per_Capita',
        'NY.GDP.MKTP.KD': 'GDP_Total'
    }
    
    start_year = 2010
    end_year = datetime.now().year
    
    print("Fetching data from World Bank API...")
    
    df = None
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            # 2. Fetch Data
            # We can fetch multiple indicators at once.
            df = wb.download(
                indicator=list(indicators.keys()),
                country=g7_countries,
                start=start_year,
                end=end_year
            )
            # Rename columns to friendly names
            df = df.rename(columns=indicators)
            break # Success, exit loop
            
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Error fetching data after multiple attempts.")
                print("Please check your internet connection or try again later.")
                return

    # 3. Data Processing
    # Reset index to make 'year' a column
    df = df.reset_index()
    df['year'] = df['year'].astype(int)
    
    # Pivot for GDP Per Capita
    df_pcap = df.pivot(index='year', columns='country', values='GDP_Per_Capita')
    df_pcap = df_pcap.sort_index()
    
    # Pivot for Total GDP
    df_total = df.pivot(index='year', columns='country', values='GDP_Total')
    df_total = df_total.sort_index()

    # --- Processing Plot 1: Normalization (2010 = 100) ---
    if 2010 not in df_pcap.index:
        print("Error: 2010 data is missing from the retrieved dataset.")
        return

    baseline = df_pcap.loc[2010]
    df_pcap_norm = df_pcap.div(baseline).mul(100)
    df_pcap_norm = df_pcap_norm.dropna(how='all')

    # --- Processing Plot 2: Normalization (2010 = 100) ---
    # Formula: (Year_Value / 2010_Value) * 100
    
    if 2010 not in df_total.index:
        print("Error: 2010 data is missing from the retrieved dataset.")
        return

    baseline_total = df_total.loc[2010]
    df_total_norm = df_total.div(baseline_total).mul(100)
    df_total_norm = df_total_norm.dropna(how='all')

    # 4. Visualization
    # Create 2 subplots arranged vertically
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 14))
    
    colors = {
        'United States': '#1f77b4',
        'Canada': '#d62728',     # Red
        'United Kingdom': '#9467bd',
        'Germany': '#ff7f0e',
        'France': '#2ca02c',
        'Italy': '#8c564b',
        'Japan': '#e377c2'
    }

    # --- Plot 1: GDP Per Capita (Normalized) ---
    for country in df_pcap_norm.columns:
        c = colors.get(country, None)
        ax1.plot(df_pcap_norm.index, df_pcap_norm[country], 
                 marker='o', markersize=4, linewidth=2, label=country, color=c)

    ax1.axhline(y=100, color='black', linestyle='--', alpha=0.5, linewidth=1, label='Base Year (2010=100)')
    ax1.set_title('Real GDP per Capita Growth (2010=100)', fontsize=14, pad=10)
    ax1.set_ylabel('Index (2010 = 100)', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)
    # Legend for the first plot
    ax1.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
    ax1.set_xticks(df_pcap_norm.index)

    # --- Plot 2: Total Real GDP (Normalized) ---
    for country in df_total_norm.columns:
        c = colors.get(country, None)
        ax2.plot(df_total_norm.index, df_total_norm[country], 
                 marker='s', markersize=4, linewidth=2, label=country, color=c)

    ax2.set_title('Annual Real GDP Growth (2010=100)', fontsize=14, pad=10)
    ax2.set_ylabel('Index (2010 = 100)', fontsize=12)
    ax2.set_xlabel('Year', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    # Legend for the second plot (optional, but good if axes are far apart)
    ax2.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
    ax2.set_xticks(df_total_norm.index)

    plt.tight_layout()
    
    print("Displaying charts...")
    plt.show()

if __name__ == "__main__":
    create_g7_gdp_chart()