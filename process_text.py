def process_text(input_text):
    lines = input_text.split('\n')
    result = []
    stack = [result]  # Stack to keep track of current list or sublist
    current_indent = 0

    for line in lines:
        indent = len(line) - len(line.lstrip())
        line_content = line.strip()

        # Move to a new sublist
        while indent < current_indent:
            stack.pop()
            current_indent -= 4

        # If the line ends with a colon, create a new sublist
        if indent > current_indent:
            new_sublist = []
            current_list.append(new_sublist)
            stack.append(new_sublist)
            current_indent += 4

        current_list = stack[-1]
        current_list.append(line_content)

    return result

# Example usage:
input_text = """Fruit
    Apple
    Orange
Vegetable
    Carrot
    Broccoli
    Leafy Greens
        Spinach
        Kale"""
