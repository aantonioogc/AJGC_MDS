import json
import csv

def json_to_csv(json_file, csv_file, max_records=1000000):
    with open(json_file, 'r', encoding='utf-8') as jsonf, open(csv_file, 'w', newline='', encoding='utf-8') as csvf:
        csv_writer = csv.writer(csvf)
        records_written = 0
        
        for line in jsonf:
            data = json.loads(line)
            
            # Si hemos alcanzado el límite de registros, salimos del bucle
            if records_written >= max_records:
                break
            
            # Escribir la fila en el archivo CSV
            csv_writer.writerow(data.values())
            
            records_written += 1

    print(f"CSV file has been created successfully with {records_written} records.")

# Example usage:
json_file = "yelp_academic_dataset_review.json"  # Path to your JSON file
csv_file = "yelp_academic_dataset_review_transformed.csv"   # Path to save the CSV file

json_to_csv(json_file, csv_file)
