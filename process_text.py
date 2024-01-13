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

        # If is more indented than previously, create a new sublist
        if indent > current_indent:
            the_sublist = current_list[-1]['children']
            stack.append(the_sublist)
            current_indent += 4

        current_list = stack[-1]
        current_list.append({'section':line_content, 'children':[]})

    return result

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

result = process_text(input_text)
print(result == output)
