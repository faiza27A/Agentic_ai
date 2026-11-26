
import pandas as pd
import requests
from io import StringIO

def decode_secret_message(document_url):

    # Step 1: Fetch the published Google Doc
    response = requests.get(document_url, timeout=30)
    response.raise_for_status()

    # Step 2: Extract the HTML table
    tables = pd.read_html(StringIO(response.text), header=0)

    if not tables:
        raise ValueError("No table found.")

    df = tables[0]

    # Step 3: Identify columns
    df.columns = [str(col).strip().lower() for col in df.columns]

    x_col = next(c for c in df.columns if "x" in c)
    y_col = next(c for c in df.columns if "y" in c)
    char_col = next(
        c for c in df.columns
        if "character" in c or "char" in c
    )

    # Step 4: Convert coordinates
    df[x_col] = pd.to_numeric(df[x_col])
    df[y_col] = pd.to_numeric(df[y_col])

    # Step 5: Create coordinate dictionary
    coordinates = {}

    for _, row in df.iterrows():
        x = int(row[x_col])
        y = int(row[y_col])
        character = str(row[char_col])

        coordinates[(x, y)] = character

    # Step 6: Find grid dimensions
    max_x = max(x for x, y in coordinates)
    max_y = max(y for x, y in coordinates)

    # Step 7: Print grid
    print("\nDECODED SECRET MESSAGE:\n")

    for y in range(max_y, -1, -1):
        line = ""

        for x in range(max_x + 1):
            line += coordinates.get((x, y), " ")

        print(line)


# Step 8: Run function
document_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

decode_secret_message(document_url)
