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
            new_sublist = []
            current_list.append(new_sublist)
            stack.append(new_sublist)
            current_indent += 4

        current_list = stack[-1]
        current_list.append(line_content)

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
        Special Refles
    Cerebellar
Psychiatric"""
        
print(process_text(input_text))


['', 
'Constitutional', 
[   'General', 
    'Vitals'], 
'HEENT', 
[   'Head', 
    'Eyes', 
    'Ears', 
    'Nose', 
    'Throat'], 
'Pulmonary', 
'Cardiovascular', 
'Gastrointestinal', 
[   'Inspection', 
    'Auscultation',     
    'Palpation'], 
'Genitourinary', '  
'Dermatologic', 
'Musculoskeletal', 
'Neurological', 
[   'Cranial Nerves', 
    'Mental Status (Neuro)', 
    'Sensory', 
    'Motor', 
    'Reflexes', 
    'Cerebellar'], 
    'Psychiatric']
