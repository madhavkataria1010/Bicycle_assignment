# Bicycle Generator

This tool reads bicycle specifications from an Excel file and generates a JSON file containing all possible bicycle modifications.

## Prerequisites

- Python 3.10+
- `venv` module 

## Installation

1. Clone or download this repository.


2. Create and activate a virtual environment:

   ```zsh
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```zsh
   pip install -r requirements.txt
   ```

## Usage

You can run the generator in two ways:

### 1. As a module (recommended)

```zsh
python -m src <path_to_excel> <output_json_file>
``` 

- `<path_to_excel>`: Path to the input `.xlsx` file (e.g., `Bicycle.xlsx`).
- `<output_json_file>`: Desired output JSON filename (e.g., `bikes.json`).

Example:

```zsh
python -m src Bicycle.xlsx bikes.json
```

## Output

The generator produces a JSON array of objects, each representing a unique bicycle combination with:

- `ID`: Concatenated designator values
- Common fields from the `GENERAL` sheet
- Fields from dependent sheets based on designator mappings


