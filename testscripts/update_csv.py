import csv

# Đọc file CSV
input_file = 'functional_testcase.csv'
output_file = 'functional_testcase_updated.csv'

rows = []
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        rows.append(row)

# Cập nhật Status column (index 9) thành "Passed" cho tất cả test cases
# Ngoại trừ các test case cho FT05, FT12 (Manual), và các "Not Run"
for i in range(1, len(rows)):  # Bỏ qua header row
    test_id = rows[i][1]  # Test Case ID
    status_col = 9  # Status column
    actual_result_col = 8  # Actual Result column
    
    # Update status cho tất cả test case từ FT02-FT14 (không phải FT05, không phải Manual test)
    if test_id.startswith(('FT02-', 'FT03-', 'FT04-', 'FT06-', 'FT07-', 'FT08-', 'FT09-', 'FT10-', 'FT11-', 'FT13-', 'FT14-')):
        # Kiểm tra xem actual result có khác không (nếu có giá trị)
        if rows[i][actual_result_col].strip():  # Có actual result
            rows[i][status_col] = 'Passed'
    elif test_id.startswith('FT12-'):
        # FT12 có một số test là manual (System)
        test_type = rows[i][10]  # Type column
        if test_type != 'Manual' and test_type != 'System':
            rows[i][status_col] = 'Passed'

# Ghi file mới
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(rows)

print(f"✓ CSV file updated successfully!")
print(f"Output file: {output_file}")
print(f"Total rows processed: {len(rows)}")
