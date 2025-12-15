# ==============================================
# Pandas CRUD Crash Course (Compiled Final Code)
# ==============================================

# --- CREATE & READ SECTION ---

import pandas as pd

# 1. Read CSV data into a DataFrame
df = pd.read_csv("telco_churn.csv")

# View the first 5 rows
print(df.head())

# View the first 10 rows
print(df.head(10))

# 2. Create a DataFrame from a dictionary
data_dict = {
    'Name': ['Nick', 'Kate', 'John', 'Sara'],
    'Age': [29, 24, 31, 27],
    'Country': ['USA', 'Canada', 'UK', 'Australia']
}

df_dict = pd.DataFrame.from_dict(data_dict)
print(df_dict.head())

# --- READ SECTION ---

# View bottom 5 rows
print(df.tail())

# View bottom 15 rows
print(df.tail(15))

# View all columns
print(df.columns)

# View data types of each column
print(df.dtypes)

# Summary statistics for numeric data
print(df.describe())

# Summary statistics for object (categorical) data
print(df.describe(include='object'))

# --- FILTERING SECTION ---

# Single column (no space in name)
print(df.columns['state'].head())

# Column name with a space
print(df['international plan'].head())

# Multiple columns
print(df[['state', 'international plan']].head())

# Unique values of specific columns
print(df['state'].unique())
print(df['churn'].unique())

# Filter rows where 'international plan' == 'No'
print(df[df['international plan'] == 'No'].head())

# Filter rows where 'international plan' == 'No' and 'churn' == True
filtered_df = df[(df['international plan'] == 'No') & (df['churn'] == True)]
print(filtered_df.head())

# --- INDEXING SECTION ---

# Integer-based indexing with iloc
print(df.iloc[14])  # 15th row

# Grab a specific column within a specific row
print(df.iloc[14, 0])   # 15th row, first column
print(df.iloc[14, -1])  # 15th row, last column

# Slice subset of rows
print(df.iloc[22:33])

# Keyword-based indexing with loc
df.set_index('state', inplace=True)
print(df.loc['OHIO'])

# --- UPDATE SECTION ---

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values, in place
df.dropna(inplace=True)
print(df.isnull().sum())

# Drop a column (example: 'area code')
df.drop('area code', axis=1, inplace=True)

# Create a new calculated column
df['new_column'] = df['total night minutes'] + df['total intl minutes']

# Update an entire column
df['new_column'] = 100
print(df['new_column'].head())

# Update a single value (first row, last column)
df.iloc[0, -1] = 10
print(df.iloc[0, -1])

# Apply conditional updates with lambda
df['churn_binary'] = df['churn'].apply(lambda x: 1 if x == True else 0)
print(df[['churn', 'churn_binary']].head())

# --- OUTPUT / DELETE SECTION ---

# Export DataFrame to CSV
df.to_csv('output.csv', index=False)

# Export DataFrame to JSON
df.to_json('output.json', orient='records')

# Export DataFrame to HTML
df.to_html('output.html')

# Delete the DataFrame from memory
del df
