import csv
import json
import argparse
import sys
from pathlib import Path

def csv_to_json(csv_file_path, json_file_path=None, indent=2):
    """
    Convert CSV file to JSON format
    
    Args:
        csv_file_path (str): Path to the input CSV file
        json_file_path (str, optional): Path to the output JSON file. 
                                      If None, will use CSV filename with .json extension
        indent (int): Number of spaces for JSON indentation (default: 2)
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Validate input file
        csv_path = Path(csv_file_path)
        if not csv_path.exists():
            print(f"Error: CSV file '{csv_file_path}' not found.")
            return False
        
        # Set output file path if not provided
        if json_file_path is None:
            # Use 'test-output.json' as default filename in same directory as CSV
            json_file_path = csv_path.parent / 'test-output.json'
        
        # Read CSV and convert to JSON
        data = []
        
        with open(csv_file_path, 'r', encoding='utf-8', newline='') as csv_file:
            # Detect CSV dialect (comma, semicolon, etc.)
            sample = csv_file.read(1024)
            csv_file.seek(0)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            
            # Read CSV data
            csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
            
            for row in csv_reader:
                # Clean up any extra whitespace in keys and values
                cleaned_row = {key.strip(): value.strip() if value else value 
                             for key, value in row.items()}
                data.append(cleaned_row)
        
        # Write JSON file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=indent, ensure_ascii=False)
        
        print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'")
        print(f"Converted {len(data)} records")
        return True
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False

def main():
    """Main function to handle command line arguments"""
    parser = argparse.ArgumentParser(
        description="Convert CSV file to JSON format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python csv_to_json.py input.csv
  python csv_to_json.py input.csv output.json
  python csv_to_json.py input.csv --indent 4
        """
    )
    
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('json_file', nargs='?', help='Path to the output JSON file (optional)')
    parser.add_argument('--indent', type=int, default=2, 
                       help='Number of spaces for JSON indentation (default: 2)')
    
    args = parser.parse_args()
    
    # Convert CSV to JSON
    success = csv_to_json(args.csv_file, args.json_file, args.indent)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

# Quick usage with hardcoded path (uncomment and modify as needed)
# csv_to_json('your_file.csv', 'output.json')

if __name__ == "__main__":
    main()