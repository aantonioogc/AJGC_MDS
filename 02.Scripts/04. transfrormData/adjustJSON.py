import json

def limit_json_records(input_file, output_file, max_records=1000000):
    with open(input_file, 'r', encoding='utf-8') as f_input, \
         open(output_file, 'w', encoding='utf-8') as f_output:
        
        count = 0
        for line in f_input:
            if line.strip():
                json_obj = json.loads(line)
                json.dump(json_obj, f_output)
                f_output.write('\n')
                count += 1
                if count >= max_records:
                    break

if __name__ == "__main__":
    input_file = 'yelp_academic_dataset_user.json'
    output_file = 'yelp_academic_dataset_user_transformed.json'
    limit_json_records(input_file, output_file)