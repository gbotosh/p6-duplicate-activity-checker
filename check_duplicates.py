import pandas as pd
from rapidfuzz import fuzz
from itertools import combinations
from pathlib import Path

input_file = Path("data_raw/activity_list.xlsx")
output_folder = Path("outputs")
output_folder.mkdir(exist_ok=True)

if not input_file.exists():
    raise FileNotFoundError(
        "Please place activity_list.xlsx inside the data_raw folder."
    )

df = pd.read_excel(input_file)
df.columns = df.columns.str.strip()

required_columns = ["Activity ID", "Activity Name"]

for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")

df["Clean Activity Name"] = (
    df["Activity Name"]
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# Exact duplicates
exact_duplicates = (
    df.groupby("Clean Activity Name")
    .agg(
        Count=("Activity ID", "count"),
        Activity_IDs=("Activity ID", lambda x: ", ".join(x.astype(str))),
        Sample_Description=("Activity Name", "first"),
    )
    .reset_index()
)

exact_duplicates = exact_duplicates[exact_duplicates["Count"] > 1]
exact_duplicates = exact_duplicates[["Sample_Description", "Count", "Activity_IDs"]]

exact_duplicates.to_excel(
    output_folder / "exact_duplicate_activity_names.xlsx", index=False
)

# Near duplicates
results = []

for (_, row1), (_, row2) in combinations(df.iterrows(), 2):
    similarity = fuzz.token_sort_ratio(
        row1["Clean Activity Name"], row2["Clean Activity Name"]
    )

    if similarity >= 85:
        results.append(
            {
                "Activity ID 1": row1["Activity ID"],
                "Activity Name 1": row1["Activity Name"],
                "Activity ID 2": row2["Activity ID"],
                "Activity Name 2": row2["Activity Name"],
                "Similarity Score": similarity,
            }
        )

near_duplicates = pd.DataFrame(results)

near_duplicates.to_excel(
    output_folder / "near_duplicate_activity_names.xlsx", index=False
)

print("Duplicate checks completed.")
print(f"Exact duplicate descriptions found: {len(exact_duplicates)}")
print(f"Near duplicate pairs found: {len(near_duplicates)}")
print("Check the outputs folder.")
