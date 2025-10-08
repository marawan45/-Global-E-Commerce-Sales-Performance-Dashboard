
import pandas as pd
import numpy as np
from typing import Optional

if __name__ == '__main__':
	file_path = r"C:/Users/maraw/Downloads/Global E-Commerce Sales Performance Dashboard/Sample - Superstore.csv"
	df = pd.read_csv(file_path, encoding='ISO-8859-1')
	



print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.duplicated().sum())    
def clean_dataframe(df: pd.DataFrame, date_cols: Optional[list] = None) -> pd.DataFrame:
	"""Clean a Superstore-like DataFrame in-place and return it.

	Actions performed:
	- Trim whitespace from all string/object columns
	- Coerce date columns (if provided) to datetime (errors -> NaT)
	- Coerce numeric-like columns to numeric (errors -> NaN)
	- Fill common missing values with sensible defaults (mode for categoricals, mean for numerics)
	- Create Year and Month columns based on Order Date when available

	Args:
		df: input DataFrame
		date_cols: optional list of columns to coerce to datetime (defaults to ['Order Date','Ship Date'] if present)

	Returns:
		cleaned DataFrame (same object returned for convenience)
	"""

	# Trim whitespace from all object (string) columns
	obj_cols = df.select_dtypes(include=['object']).columns.tolist()
	for col in obj_cols:
		# Only apply strip to non-null values
		df.loc[:, col] = df[col].where(df[col].isnull(), df[col].astype(str).str.strip())

	# Default date columns if not provided
	if date_cols is None:
		date_cols = [c for c in ['Order Date', 'Ship Date'] if c in df.columns]

	# Coerce date columns
	for col in date_cols:
		if col in df.columns:
			df.loc[:, col] = pd.to_datetime(df[col], errors='coerce')

	
	probable_numeric = ['Sales', 'Quantity', 'Discount', 'Profit', 'Postal Code']
	numeric_cols = [c for c in probable_numeric if c in df.columns]
	
	for c in df.columns:
		if c not in numeric_cols and pd.api.types.is_numeric_dtype(df[c]):
			numeric_cols.append(c)

	
	for col in numeric_cols:
		df.loc[:, col] = pd.to_numeric(df[col], errors='coerce')

	for col in df.columns:
		if df[col].isnull().any():
			if col in numeric_cols:
				mean_val = df[col].mean()
				df.loc[:, col] = df[col].fillna(mean_val)
			elif pd.api.types.is_datetime64_any_dtype(df[col]):
			
				try:
					mode_val = df[col].mode()
					if not mode_val.empty:
						df.loc[:, col] = df[col].fillna(mode_val[0])
				except Exception:
					pass
			elif col.lower().endswith('id') or col.lower().endswith('name'):
				df.loc[:, col] = df[col].fillna('Unknown')
			else:
		
				try:
					mode_val = df[col].mode()
					if not mode_val.empty:
						df.loc[:, col] = df[col].fillna(mode_val[0])
					else:
						df.loc[:, col] = df[col].fillna('Unknown')
				except Exception:
					df.loc[:, col] = df[col].fillna('Unknown')


	if 'Order Date' in df.columns and pd.api.types.is_datetime64_any_dtype(df['Order Date']):
		df.loc[:, 'Year'] = df['Order Date'].dt.year
		df.loc[:, 'Month'] = df['Order Date'].dt.month_name()

	return df

df.columns = df.columns.str.strip()  

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')



cleaned = clean_dataframe(df)
print(cleaned.head())

df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Profit Margin as a percentage
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100

# Total discount value per order
df['Discount Amount'] = df['Sales'] * df['Discount']

# Sales after discount
df['Net Sales'] = df['Sales'] - df['Discount Amount']

df['Sales per Quantity'] = df['Sales'] / df['Quantity']
df['Profit per Quantity'] = df['Profit'] / df['Quantity']

# Save cleaned data to a new CSV file
out_path = r"C:/Users/maraw/Downloads/Global E-Commerce Sales Performance Dashboard/cleaned_superstore.csv"
cleaned.to_csv(out_path, index=False)
print(f"Data cleaning completed and saved to '{out_path}'")