import os

dir_path = r"D:\BI_AI_course\bi-ai-course\lesson3\homework"

os.makedirs(dir_path, exist_ok=True)
for i in range(1, 26):
    file_name = f"list{i}.py"
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'w') as file:
        file.write("# This is file " + file_name + "\n")

print("25 files created successfully in the specified directory.")
