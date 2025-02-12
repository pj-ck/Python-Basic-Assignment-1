'''
Write a Python script which reads a csv file and Visualizes a table with proper indentations and borders. (make sure to don’t use any table making module or package)	
Example : CSV file like this
Name,Age,Department
Alice,30,HR
Bob,25,Engineering
Charlie,35,Marketing
Diana,28,Sales
'''


def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = [line.strip().split(',') for line in lines if line.strip()]  
    return data

def get_column_widths(data):
    num_columns = len(data[0])  
    return [max(len(str(row[i])) for row in data if len(row) > i) for i in range(num_columns)]

def print_table(data):
    col_widths = get_column_widths(data)
    border = '+' + '+'.join(['-' * (width + 2) for width in col_widths]) + '+'

    print(border)
    for i, row in enumerate(data):
        
        row += [''] * (len(col_widths) - len(row))
        row_line = '| ' + ' | '.join(f'{item:<{col_widths[j]}}' for j, item in enumerate(row)) + ' |'
        print(row_line)
        if i == 0:  
            print(border)
    print(border)

if __name__ == "__main__":
    file_path = input("Enter the CSV file path: ")
    try:
        data = read_csv(file_path)
        print_table(data)
    except FileNotFoundError:
        print(" File not found. Please check the path and try again.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")
