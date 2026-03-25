import pandas as pd

# Directory where Excel data files are stored
BASE_PATH = "data"

def clean_df(df):
    """
    Normalizes dataframe columns by stripping whitespace and converting to lowercase.
    """
    df.columns = df.columns.str.strip().str.lower()
    return df

def filter_df(df, shop_id="SHOP_001", year=2024):
    """
    Filters the dataframe based on store ID and year.
    Defaults to SHOP_001 and year 2024 if not specified.
    """
    if 'store_id' in df.columns:
        df = df[df['store_id'] == shop_id]
    if 'year' in df.columns:
        df = df[df['year'] == year]
    return df

def get_sales_df():
    """
    Reads sales data from Excel, cleans it, and filters by default criteria.
    """
    try:
        df = pd.read_excel(f"{BASE_PATH}/Sales_Table.xlsx", header=1)
        return filter_df(clean_df(df))
    except Exception:
        # Returns an empty dataframe if file reading fails
        return pd.DataFrame()

def get_expense_df():
    """
    Reads expense data from Excel, cleans it, and filters by default criteria.
    """
    try:
        df = pd.read_excel(f"{BASE_PATH}/Expenses_Table.xlsx", header=1)
        return filter_df(clean_df(df))
    except Exception:
        return pd.DataFrame()

def get_customer_df():
    """
    Reads customer data from Excel, cleans it, and filters by default criteria.
    """
    try:
        df = pd.read_excel(f"{BASE_PATH}/Customers_Table.xlsx", header=1)
        return filter_df(clean_df(df))
    except Exception:
        return pd.DataFrame()

def get_inventory_df():
    """
    Reads inventory data from Excel, cleans it, and filters by default criteria.
    """
    try:
        df = pd.read_excel(f"{BASE_PATH}/Inventory_Table.xlsx", header=1)
        return filter_df(clean_df(df))
    except Exception:
        return pd.DataFrame()
