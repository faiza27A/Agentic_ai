import pandas as pd

# Step 1: Google Docs published URL
document_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"


# Step 2: Define the decoding function
def decode_secret_message(document_url):

    # Read the HTML table from Google Docs
    tables = pd.read_html(document_url, header=None)

    # Select the first table
    df = tables[0]
    print("Table columns:", df.columns)
    print("First 10 rows:")
    print(df.head(10))
    print("Available characters:")
    print(df.iloc[:, 1].unique())
    df.columns = ["x_coordinate", "character", "y_coordinate"]
    print(df["character"].unique())
    
    # Remove the header row if it appears as data
    first_row = [str(value).strip().lower() for value in df.iloc[0]]

    if "x-coordinate" in first_row[0]:
        df = df.iloc[1:].copy()

    # Assign column names
    df.columns = ["x", "character", "y"]

    # Convert coordinates into integers
    df["x"] = pd.to_numeric(df["x"])
    df["y"] = pd.to_numeric(df["y"])

    # Find grid dimensions
    max_x = int(df["x"].max())
    max_y = int(df["y"].max())

    # Create an empty grid
    grid = [[" " for x in range(max_x + 1)]
            for y in range(max_y + 1)]

    # Place characters at their coordinates
    for _, row in df.iterrows():

        x = int(row["x"])
        y = int(row["y"])
        character = str(row["character"]).strip()

        if character == "":
            grid[y][x] = "█"

    # Print the secret message
    print("\nDECODED SECRET MESSAGE:\n")

    for row in reversed(grid):
        print("".join(row))


# Step 3: Execute the function
decode_secret_message(document_url)
print("Table columns:", df.columns)
print("First 10 rows:")
print(df.head(10))
print("Available characters:")
print(df.iloc[:, 1].unique())