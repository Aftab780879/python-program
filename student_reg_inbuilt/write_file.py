import json
def write_json(json_file,student_list):
    with open(json_file,'w') as file:
                file.write(json.dumps(student_list,indent=4))