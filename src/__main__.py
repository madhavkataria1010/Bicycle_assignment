import sys
from .generator import generate_bicycles

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python -m src <path_to_excel> <output_json_file>")
        sys.exit(1)
    excel_path, output_path = sys.argv[1], sys.argv[2]
    try:
        data = generate_bicycles(excel_path)
        with open(output_path, 'w') as f:
            f.write(data)
        print(f"Generated JSON output and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
