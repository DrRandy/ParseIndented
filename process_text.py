def process_indented_text(input_text, indent_spaces):
    """
        input_text = the indented text to be parsed 
            - the first line must not be indented
            - indentations should be spaces and not tabs
        indent_spaces = the number of spaces that equals one indentation level 
            - so if 4 spaces each, then 8 spaces would be two indentations
            - indentations must be a multiple of this number to parse correctly
    """
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
            current_indent -= indent_spaces

        # If is more indented than previously, create a new sublist
        if indent > current_indent:
            the_sublist = current_list[-1]['children']
            stack.append(the_sublist)
            current_indent += indent_spaces

        current_list = stack[-1]
        current_list.append({'section':line_content, 'children':[]})

    return result


def print_list_of_dictionaries(list_of_dictionaries):

    def helper(list_of_dictionaries, number_of_spaces):
        for dictionary in list_of_dictionaries:
            section = dictionary['section']
            children = dictionary['children']
            leading_spaces = " "*number_of_spaces
            output_line = leading_spaces + section
            print(output_line)
            if not children==[]:
                helper(children, number_of_spaces+4)

    helper(list_of_dictionaries, 0)

# textografo input
"""
    textografo input needs to be massaged; branches of decisions are not indented
"""
textografo_text = """
#flowchart PFT 
  #start  PFT interpretation
  <>  FVC > 80% predicted
    Yes 
      There is no restriction.
      <> FEV1/FVC > 0.7
        No
          Normal Spirometry
        Yes
          Obstruction
    No
      There is restriction or obstruction with air trapping.
      <> TLC > 80% predicted
        Yes
          Obstruction with air trapping
        No
          Restriction"""

# Example usage:
input_text = """
Constitutional
    General
    Vitals
HEENT
    Head
    Eyes
    Ears
    Nose
    Throat
Pulmonary
Cardiovascular
Gastrointestinal
    Inspection
    Auscultation
    Palpation
Genitourinary
Dermatologic
Musculoskeletal
Neurological
    Cranial Nerves
    Mental Status (Neuro)
    Sensory
    Motor
    Reflexes
        Upper Extremity Reflexes
            Biceps
            Brachioradialis
            Triceps
        Lower Extremity Reflexes
            Knee Jerks
            Ankle Jerk Reflexes
        Special Reflexes
    Cerebellar
Psychiatric"""
        
output = [{'section': '', 'children': []}, 
{'section': 'Constitutional', 'children': [
    {'section': 'General', 'children': []}, 
    {'section': 'Vitals', 'children': []}]}, 
{'section': 'HEENT', 'children': [
    {'section': 'Head', 'children': []}, 
    {'section': 'Eyes', 'children': []}, 
    {'section': 'Ears', 'children': []}, 
    {'section': 'Nose', 'children': []}, 
    {'section': 'Throat', 'children': []}]}, 
{'section': 'Pulmonary', 'children': []}, 
{'section': 'Cardiovascular', 'children': []}, 
{'section': 'Gastrointestinal', 'children': [
    {'section': 'Inspection', 'children': []}, 
    {'section': 'Auscultation', 'children': []}, 
    {'section': 'Palpation', 'children': []}]}, 
{'section': 'Genitourinary', 'children': []}, 
{'section': 'Dermatologic', 'children': []}, 
{'section': 'Musculoskeletal', 'children': []}, 
{'section': 'Neurological', 'children': [
    {'section': 'Cranial Nerves', 'children': []}, 
    {'section': 'Mental Status (Neuro)', 'children': []}, 
    {'section': 'Sensory', 'children': []}, {'section': 'Motor', 'children': []}, 
    {'section': 'Reflexes', 'children': [
        {'section': 'Upper Extremity Reflexes', 'children': [
            {'section': 'Biceps', 'children': []}, 
            {'section': 'Brachioradialis', 'children': []}, 
            {'section': 'Triceps', 'children': []}]}, 
        {'section': 'Lower Extremity Reflexes', 'children': [
            {'section': 'Knee Jerks', 'children': []}, 
            {'section': 'Ankle Jerk Reflexes', 'children': []}]}, 
        {'section': 'Special Reflexes', 'children': []}]}, 
    {'section': 'Cerebellar', 'children': []}]}, 
{'section': 'Psychiatric', 'children': []}]

result = process_indented_text(input_text, 4)
print(result == output)
result = process_indented_text(textografo_text, 2)
print_list_of_dictionaries(result)

quick_line = """`?+_%s`_? """

def generate_quick(list_of_dictionaries):

    def helper(list_of_dictionaries, tagroot):
        index = 0
        quick_output = "\n"
        for dictionary in list_of_dictionaries:
            index += 1
            fieldname = dictionary['section']
            tag = tagroot + fieldname[0:4] + '{:02d}'.format(index)
            children = dictionary['children']
            section_declaration = """%s="%s"\n""" % (tag, fieldname)
            children_declaration = helper(children, tag)
            line_contents = section_declaration + children_declaration
            output_line = quick_line % line_contents
            quick_output = quick_output + output_line
        return quick_output
    
    result = helper(list_of_dictionaries, "")
    return result

quick_result = generate_quick(output[1:])
print(quick_result)