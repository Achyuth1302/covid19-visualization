import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn theme
sns.set(style="whitegrid")

def load_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df.fillna(0, inplace=True)
    return df

def plot_total_cases(df, country):
    country_df = df[df['location'] == country]
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=country_df, x='date', y='total_cases')
    plt.title(f'Total COVID-19 Cases Over Time in {country}')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_total_deaths(df, country):
    country_df = df[df['location'] == country]
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=country_df, x='date', y='total_deaths')
    plt.title(f'Total COVID-19 Deaths Over Time in {country}')
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_total_vaccinations(df, country):
    country_df = df[df['location'] == country]
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=country_df, x='date', y='total_vaccinations')
    plt.title(f'Total COVID-19 Vaccinations Over Time in {country}')
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    data_path = 'data/owid-covid-data.csv'
    country = 'India'  # You can change this to any country

    df = load_data(data_path)
    df = preprocess_data(df)

    plot_total_cases(df, country)
    plot_total_deaths(df, country)
    plot_total_vaccinations(df, country)

if __name__ == '__main__':
    main()
