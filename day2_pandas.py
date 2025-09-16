import pandas as pd
import matplotlib.pyplot as plt
#print ("Pandas Version: ",pd.__version__)

#sales_file = pd.read_csv('sales.csv')
super_store_file = pd.read_csv('super-store-sales.csv')

#print("Sales File: \n",sales_file.head())
#print("Super Store File: \n",super_store_file.head())


#print("Shape of Sales File: \n", sales_file.shape)
#print("Shape of Super Store File: \n", super_store_file.shape)

#print("Columns of Sales File: \n", sales_file.columns.to_list())
#print("Columns of Super Store File: \n", super_store_file.columns.to_list())

#print("Summary of Sales File: \n", sales_file.describe())
#print("Summary of Super Store File: \n", super_store_file.describe())

#print("Info of Sales File: \n", sales_file.info())
#print("Info of Super Store File: \n", super_store_file.info())

#above_sales = super_store_file[super_store_file['Sales'] > 100]
#print("Sale of Super Store Above 100: \n", above_sales)
#print("Count of Super Store Above 100: \n", len(above_sales))

sales_by_product = super_store_file.groupby('Product Name')['Sales'].sum()
#print("Sum of Group by Product: \n", sales_by_product)

sales_by_product.plot(kind='bar', title='Total Sales by Product')

plt.xlabel('Product')
plt.ylabel('Total-Sales')
plt.show()


