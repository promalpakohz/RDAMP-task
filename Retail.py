import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Ace Superstore Retail Dataset.csv')
print(df.head(10))
print(df['Customer ID'])
df.drop('Customer ID', axis=1, inplace=True)
print(df.columns)
print(df.Country.unique())
print(df.Region.unique())
print(df['Country'].value_counts())
print(df['Region'].value_counts())
#checking for missing values
print(df.isna().sum())
#dropping missing values
df.dropna(inplace=True)
#checking for duplicates
print(df.duplicated().sum())
print(df.shape)
print(df.describe())
print(df.Sales.sum())
print(df['Cost Price'].sum())
print(df.groupby('Region')['Sales'].sum().plot(kind='bar', title='Sales by Region'))
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()
print(df.groupby('Region')['Discount'].sum().plot(kind='bar', title='Discount by Region'))
plt.xlabel('Region')
plt.ylabel('Total Discounts')
plt.show()
Revenue= df['Sales'] - df['Cost Price']
print(Revenue)
df['Revenue']=Revenue
print(df.groupby('Region')['Revenue'].sum().plot(kind='bar', title='Revenue by Region'))
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.show()
print(df.columns)
# Top 5 products by sales
print(df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5))
# Bottom 5 products by sales 
print(df.groupby('Product Name')['Sales'].sum().sort_values(ascending=True).head(5))
#Product with highest margins
print(df.groupby('Product Name')['Revenue'].sum().sort_values(ascending=False).head(5))
#Online vs Offline Sales
print(df.groupby('Order Mode')['Sales'].sum().plot(kind='bar', title='Sales by Channel'))
plt.xlabel('Order Mode')
plt.ylabel('Total Sales')
plt.show()


