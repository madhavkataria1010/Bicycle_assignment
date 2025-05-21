import json
import itertools
import pandas as pd


def generate_bicycles(excel_path: str) -> str:

    id_df = pd.read_excel(excel_path, sheet_name='ID', dtype=str)
    id_df = id_df.dropna(how='all', axis=0).dropna(how='all', axis=1)

    designators = list(id_df.columns)

    values_lists = []
    for col in designators:
        values = id_df[col].dropna().tolist()
        values_lists.append(values)

    general_df = pd.read_excel(excel_path, sheet_name='GENERAL', dtype=str)
    general_df = general_df.dropna(how='all', axis=0).dropna(how='all', axis=1)
    common_fields = dict(zip(general_df.columns, general_df.iloc[0]))
    dep_sheets = pd.ExcelFile(excel_path).sheet_names
    dep_sheets = [s for s in dep_sheets if s not in ('ID', 'GENERAL')]
    dependent_tables = []
    for sheet in dep_sheets:
        df = pd.read_excel(excel_path, sheet_name=sheet, dtype=str)
        df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)
        # First column header is the designator name for this dependency
        designator_name = df.columns[0]
        field_names = df.columns[1:]
        # Build mapping: designator_value -> dict of field_name: value
        mapping = {}
        for _, row in df.iterrows():
            key = row[designator_name]
            if pd.isna(key):
                continue
            entry = {}
            for field in field_names:
                val = row[field]
                if not pd.isna(val):
                    entry[field] = val
            mapping[key] = entry
        dependent_tables.append((designator_name, mapping))

    # For all bycle combinations generation 
    bikes = []
    for combo in itertools.product(*values_lists):
        bike = {}

        bike_id = ''.join(combo)
        bike['ID'] = bike_id

        bike.update(common_fields)

        combo_map = dict(zip(designators, combo))

        for designator_name, mapping in dependent_tables:
            value = combo_map.get(designator_name)
            if value in mapping:
                bike.update(mapping[value])
        bikes.append(bike)

    # Conversion to JSON
    return json.dumps(bikes, indent=4)
