from collections import defaultdict

# Original data file, change list.txt to your file's name, also look through your data and format it properly. VEX Parts should be "xxx-xxxx-xxx" or "xxx-xxxx", if it prints something else then go through your .txt and reformat it

file_path = 'list.txt'

with open(file_path, 'r') as file:
    lines = file.read().strip().split('\n')

code_counts = defaultdict(int)

for line in lines:
    codes = [code.strip() for code in line.split() if code.strip()]
    for code in codes:
        code_counts[code] += 1

xxx_xxxx_xxx_counts = {k: v for k, v in code_counts.items() if len(k.split('-')) == 3}
xxx_xxxx_counts = {k: v for k, v in code_counts.items() if len(k.split('-')) == 2}

print("XXX-XXXX-XXX:")
for code, count in xxx_xxxx_xxx_counts.items():
    print(f"{code}: {count}")

print("\nXXX-XXXX:")
for code, count in xxx_xxxx_counts.items():
    print(f"{code}: {count}")
