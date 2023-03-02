import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/home/vinny/Code/Python/data_analysis_cert/Projects/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df.loc[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16,5))
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.plot(df, color='red')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.reset_index()
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['years'] = df_bar['date'].dt.year
    df_bar['months'] = df_bar['date'].dt.month
    months_named = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
                    6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
                    11: 'November', 12: 'December'}
    order = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['months'] = pd.Categorical(df_bar['months'].map(months_named), categories=order, ordered=True)
    df_bar = df_bar.groupby(['years', 'months'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(10,6))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box = df_box.rename(columns={'value': 'Page Views', 'year': 'Year', 'month': 'Month'})
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['Month'] = pd.Categorical(df_box['Month'], categories=order, ordered=True)

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(data=df_box, x='Year', y='Page Views', ax=axs[0])
    sns.boxplot(data=df_box, x='Month', y='Page Views', ax=axs[1])


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
