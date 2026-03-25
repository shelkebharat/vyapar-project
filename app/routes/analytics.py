from fastapi import APIRouter
import pandas as pd
from app.utils import get_sales_df

# Define the router for analytics-related endpoints
router = APIRouter(prefix="/analytics")

@router.get("/top-products")
def top_products():
    """
    Identifies the top 5 products based on total revenue.
    If revenue column is missing, it calculates a proxy revenue based on quantity sold.
    """
    try:
        # Load sales data
        df = get_sales_df()
        
        if "revenue" in df.columns:
            # Group by product name and sum up revenue
            df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
            result = df.groupby("product_name").agg({"revenue": "sum"}).sort_values(by="revenue", ascending=False).head(5)
            
            # Formulate the response with rank and trend
            return [
                {"rank": i + 1, "name": name, "revenue": float(row["revenue"]), "trend": "up"}
                for i, (name, row) in enumerate(result.iterrows())
            ]
        else:
            # Fallback: Proxy revenue calculation (quantity * 100)
            result = df.groupby("product_name")["quantity_sold"].sum().sort_values(ascending=False).head(5)
            return [
                {"rank": i + 1, "name": name, "revenue": float(qty * 100), "trend": "up"}
                for i, (name, qty) in enumerate(result.items())
            ]
    except Exception as e:
        # Error handling
        return {"error": str(e)}

@router.get("/trend")
def trend():
    """
    Calculates monthly sales trends by grouping quantity sold by month.
    """
    try:
        # Load sales data
        df = get_sales_df()
        
        # Convert date column to datetime objects
        df['date'] = pd.to_datetime(df['date'])
        
        # Group sales by month (short name like 'Jan', 'Feb')
        trend = df.groupby(df['date'].dt.strftime('%b'))['quantity_sold'].sum()
        
        # Format for charting in the frontend
        return [{"month": k, "Sales": float(v)} for k, v in trend.items()]
    except Exception as e:
        return {"error": str(e)}