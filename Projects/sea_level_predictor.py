import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(14,8))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_error =linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    regression_line = slope * df['Year'] + intercept
    x_extrapolate = range(1880, 2051, 1)
    extrapolated_line = [slope * xi + intercept for xi in x_extrapolate]
    plt.plot(x_extrapolate, extrapolated_line, color='blue')

    # Create second line of best fit
    mask = df['Year'] > 1999
    df_2k = df[mask]
    slope, intercept, r_value, p_value, std_error =linregress(x=df_2k['Year'], y=df_2k['CSIRO Adjusted Sea Level'])
    regression_line = slope * df_2k['Year'] + intercept
    x_extrapolate = range(2000, 2051, 1)
    extrapolated_line = [slope * xi + intercept for xi in x_extrapolate]
    plt.plot(x_extrapolate, extrapolated_line, color='red')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()