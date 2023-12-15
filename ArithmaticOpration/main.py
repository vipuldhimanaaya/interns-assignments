import re

def evaluate_expression(expression):
    try:
        # Replace '^' with '**' for exponentiation
        expression = expression.replace('^', '**')
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def process_input_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        expressions = input_file.readlines()

    results = []
    for expression in expressions:
        expression = expression.strip()
        if expression:
            # Remove '=' from the expression
            expression_without_equals = expression.replace('=', '')
            try:
                result = evaluate_expression(expression_without_equals)
                results.append(f"{expression_without_equals} = {result}\n")  # Use expression_without_equals here
            except Exception as e:
                results.append(f"{expression_without_equals} = Error: {str(e)}\n")  # Use expression_without_equals here
    
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(results)
        print("Solved the espressions please check the output file")

if __name__ == "__main__":
    input_file_path = "input.txt"
    output_file_path = "output.txt"  

    process_input_file(input_file_path, output_file_path)
