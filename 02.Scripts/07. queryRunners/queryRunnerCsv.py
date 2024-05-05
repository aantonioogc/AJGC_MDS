import time
import csv
from crate import client

# Lista de consultas
queries = [
    # 3.1.1 (Filtering on a non-indexed column)
    "SELECT * FROM business_csv WHERE state = 'AZ' LIMIT 100;",
    # 3.1.2 (Filtering on a non-indexed column, range query)
    "SELECT * FROM review_csv WHERE stars BETWEEN 3 AND 5 LIMIT 100;",
    # 3.1.3 (Filtering on indexed column, exact match)
    "SELECT * FROM business_csv WHERE stars = 4 LIMIT 100;",
    # 3.1.4 (Filtering on indexed column, range query)
    "SELECT * FROM business_csv WHERE stars BETWEEN '4' AND '5' LIMIT 100;",
    
    # 3.2.1 (Use aggregation function count)
    "SELECT state, COUNT(DISTINCT business_id) AS total_businesses FROM business_csv GROUP BY state LIMIT 100;",
    # 3.2.2 (Use aggregation function max)
    "SELECT state, MAX(stars) AS max_stars FROM business_csv GROUP BY state LIMIT 100;",
    
    # 3.3.1 (Joining / traversal where two entities are connected by non-indexed columns)
    "SELECT b.name AS business_name, r.stars AS review_stars, r.text AS review_text FROM business_csv b JOIN review_csv r ON b.business_id = r.business_id LIMIT 100;",
    # 3.3.2 (Joining / traversal over indexed column)
    "SELECT r.review_id, r.text, b.name FROM review_csv r JOIN business_csv b ON r.business_id = b.business_id WHERE b.state = 'PA' LIMIT 100;",
    # 3.3.3 (Complex join involving multiple JOINS)
    "SELECT u.name AS user_name, r.stars AS review_stars, b.name AS business_name FROM user_csv u JOIN review_csv r ON u.user_id = r.user_id JOIN business_csv b ON r.business_id = b.business_id LIMIT 100;",
    # 3.3.4 (Recursive query)
    # Not supported by crateDB
    # 3.3.5 (Optional traversal, SQL: LEFT OUTER JOIN)
    "SELECT b.name AS business_name, c.date AS checkin_date FROM business_csv b LEFT OUTER JOIN checkin_csv c ON b.business_id = c.business_id LIMIT 100;",
    
    # 3.4.1 (Union)
    "SELECT business_id FROM business_csv UNION SELECT business_id FROM checkin_csv LIMIT 100;",
    # 3.4.2 (Intersect*)
    "SELECT b.business_id FROM business_csv b WHERE EXISTS (SELECT 1 FROM checkin_csv c WHERE b.business_id = c.business_id) LIMIT 100;",
    # 3.4.3 (Difference)
    "SELECT business_id FROM business_csv WHERE business_id NOT IN (SELECT business_id FROM checkin_csv) LIMIT 100;",
    
    # 3.5.1 (Sorting over non-indexed column)
    "SELECT * FROM business_csv WHERE review_count >= 100 ORDER BY review_count DESC LIMIT 100;",
    # 3.5.2 (Sorting over indexed column)
    "SELECT * FROM business_csv WHERE state = 'PA' ORDER BY name LIMIT 100;",
    
    # 3.6.1 (Apply distinct)
    "SELECT DISTINCT city FROM business_csv LIMIT 100;",
    
    # 3.7 (MapReduce or equivalent aggregation)
    "SELECT b.city, AVG(u.review_count) AS avg_reviews_per_user FROM business_csv b JOIN review_csv r ON b.business_id = r.business_id JOIN user_csv u ON r.user_id = u.user_id GROUP BY b.city LIMIT 100;"
]

num_iterations = 20

# Prepare the header for the CSV file based on number of runs
header = ['query_num'] + [f'run_{i+1}' for i in range(num_iterations)] + ['average']

# Connect to CrateDB
connection = client.connect("http://localhost:4200")
cursor = connection.cursor()

# Abrir el archivo CSV para escritura
with open('query_times_relational.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    
    # Para cada consulta en la lista de consultas
    for query_num, query in enumerate(queries, 1):
        print(f"Executing query {query_num}...")
        query_times = []
        
        # Ejecutar la consulta múltiples veces y registrar los tiempos
        for _ in range(num_iterations):
            start_time = time.time()
            cursor.execute(query)
            result = cursor.fetchall()
            end_time = time.time()
            
            query_time = end_time - start_time
            query_times.append(query_time)
        
        # Calcular el tiempo promedio, excluyendo los valores máximo y mínimo para un promedio justo
        sorted_times = sorted(query_times)
        filtered_times = sorted_times[1:-1]  # Remover los tiempos atípicos
        average_time = sum(filtered_times) / len(filtered_times)
        
        # Preparar fila para esta consulta con cada tiempo en una columna separada
        row = [f'query_{query_num}'] + filtered_times + [average_time]
        writer.writerow(row)

print("Results exported to 'query_times_relational.csv'.")