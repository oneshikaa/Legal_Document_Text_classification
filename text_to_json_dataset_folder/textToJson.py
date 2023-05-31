# import os
# import json

# # Path of the folder containing the files to be converted
# folder_path = '/home/kts/Desktop/code/projects/webscrap/regex/semantic-segmentation-master/data/text'

# # Path of the folder where converted files will be saved
# output_folder_path = '/home/kts/Desktop/code/projects/webscrap/regex/text_to_json_dataset_folder'

# # Create the output folder if it doesn't exist
# if not os.path.exists(output_folder_path):
#     os.makedirs(output_folder_path)

# # Iterate over all the files in the folder
# for file_name in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, file_name)
    
#     # Open the file and read its contents
#     with open(file_path, 'r') as f:
#         contents = f.read()
        
#     # Convert contents to a JSON object with field name "judgment"
#     json_obj = {
#         "judgment": contents
#     }
    
#     # Save the converted file in the output folder
#     output_file_path = os.path.join(output_folder_path, file_name + ".json")
#     with open(output_file_path, 'w') as f:
#         json.dump(json_obj, f)


# import json

# with open('/home/kts/Desktop/code/projects/webscrap/regex/semantic-segmentation-master/data/text/1953_L_1.txt', 'r') as file:
#     text = file.read()

# categories = {'Facts': [], 'Argument': [], 'Ratio of the decision': [], 'Precedent': [], 'Ruling by Present Court': []}
# current_category = None

# for line in text.split('\n'):
#     if line.endswith('Facts'):
#         current_category = 'Facts'
#         categories[current_category].append(line[:-5])
#     elif line.endswith('Argument'):
#         current_category = 'Argument'
#         categories[current_category].append(line[:-8])
#     elif line.endswith('Ratio of the decision'):
#         current_category = 'Ratio of the decision'
#         categories[current_category].append(line[:-8])
#     elif line.endswith('Precedent'):
#         current_category = 'Precedent'
#         categories[current_category].append(line[:-8])
#     elif line.endswith('Ruling by Present Court'):
#         current_category = 'Ruling by Present Court'
#         categories[current_category].append(line[:-8])
        
#     else:
#         categories[current_category][-1] += ' ' + line

# with open('categories.json', 'w') as file:
#     json.dump(categories, file, indent=4)

import os
import json

# Path of the folder containing the files to be converted
input_folder = '/home/kts/Desktop/code/projects/webscrap/regex/semantic-segmentation-master/data/text'

# Path of the folder where converted files will be saved
output_folder = '/home/kts/Desktop/code/projects/webscrap/regex/text_to_json_dataset_folder'

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(input_folder, filename), 'r') as file:
            text = file.read()

        categories = {'Facts': [], 'Argument': [], 'Ratio of the decision': [], 'Precedent': [], 'Ruling by Present Court': []}
        current_category = None

        for line in text.split('\n'):
            if line.endswith('Facts'):
                current_category = 'Facts'
                categories[current_category].append(line[:-5])
            elif line.endswith('Argument'):
                current_category = 'Argument'
                categories[current_category].append(line[:-8])
            elif line.endswith('Ratio of the decision'):
                current_category = 'Ratio of the decision'
                categories[current_category].append(line[:-21])
            elif line.endswith('Precedent'):
                current_category = 'Precedent'
                categories[current_category].append(line[:-8])
            elif line.endswith('Ruling by Present Court'):
                current_category = 'Ruling by Present Court'
                categories[current_category].append(line[:-23])
            else:
                categories[current_category][-1] += ' ' + line

        with open(os.path.join(output_folder, f'{filename}.json'), 'w') as file:
            json.dump(categories, file, indent=4)
