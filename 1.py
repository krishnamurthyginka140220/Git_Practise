
import pandas as pd

# Load data from a CSV file
df = pd.read_csv('data.csv')

# Display the first few rows of the dataframe
print("Original Data:")
print(df.head())

# Example transformation 1: Filtering rows
# Filter data to include only rows where a certain column's value meets a condition
filtered_df = df[df['column_name'] > 10]  # Replace 'column_name' and condition as needed
print("\nFiltered Data:")
print(filtered_df.head())

# Example transformation 2: Adding a new column
# Add a new column that is a transformation of existing columns
df['new_column'] = df['column_name'] * 2  # Replace 'column_name' and transformation as needed
print("\nData with New Column:")
print(df.head())

# Example transformation 3: Aggregation
# Group data by a column and aggregate another column
aggregated_df = df.groupby('group_column')['aggregate_column'].sum()  # Replace as needed
print("\nAggregated Data:")
print(aggregated_df.head())

# Save the transformed dataframe to a new CSV file
df.to_csv('transformed_data.csv', index=False)
