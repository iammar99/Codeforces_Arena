import os

def generate_table():
    # Define the base path for problem folders
    base_path = "problems"
    
    # Initialize the table header
    table = "| Problem # | Problem Name | Solution |\n"
    table += "|:----------|:-------------|:---------|\n"
    
    # Iterate through all problem folders
    for folder in sorted(os.listdir(base_path)):
        if os.path.isdir(os.path.join(base_path, folder)):
            # Extract problem number and name from the folder name
            problem_number, problem_name = folder.split(" - ", 1)
            
            # Generate the problem link (assuming Codeforces format)
            problem_link = f"https://codeforces.com/problemset/problem/{problem_number.split('_')[0]}/{problem_number.split('_')[1]}"
            
            # Generate the solution link
            solution_link = f"./{base_path}/{folder}/solution.py"
            
            # Add a row to the table
            table += f"| {problem_number} | [{problem_name}]({problem_link}) | [Solution]({solution_link}) |\n"
    
    return table

def update_readme(readme_path, table):
    with open(readme_path, "r") as file:
        content = file.read()
    
    # Find the start and end of the table section
    start_marker = "<!-- TABLE_START -->"
    end_marker = "<!-- TABLE_END -->"
    
    start_index = content.find(start_marker)
    end_index = content.find(end_marker)
    
    if start_index != -1 and end_index != -1:
        # Replace the old table with the new one
        new_content = (
            content[:start_index + len(start_marker)] +
            "\n" + table + "\n" +
            content[end_index:]
        )
        with open(readme_path, "w") as file:
            file.write(new_content)

if __name__ == "__main__":
    readme_path = "README.md"
    table = generate_table()
    update_readme(readme_path, table)