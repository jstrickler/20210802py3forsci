import os

starting_dir = "."

#  info_tuple = os.walk(start...)

file_sizes = []

for folder, subfolders, file_names in os.walk(starting_dir):
    if '.git' in subfolders:
        subfolders.remove('.git')
    print(folder)
    for file_name in file_names:
        if file_name == '__init__.py':
            continue  # skip it
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            if file_size > 500:
                print(f"    {file_size:6d} {file_name}")
            file_sizes.append(file_size)

print()
print(min(file_sizes), max(file_sizes))

