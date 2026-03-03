import pandas as pd
import glob

files = glob.glob("data/*.csv")

dataframes = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Remove $ and convert price to float
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

    # Calculate sales
    df["sales"] = df["price"] * df["quantity"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    dataframes.append(df)

# Combine all files
final_df = pd.concat(dataframes)

# Save output
final_df.to_csv("formatted_sales.csv", index=False)

print("Data processing complete")