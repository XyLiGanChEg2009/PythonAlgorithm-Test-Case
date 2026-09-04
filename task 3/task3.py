from sys import argv, exit
import json

def read_and_serialise(path: str):
    with open(path, "r", encoding="utf-8") as f:
        content = json.load(f)
        return content

def extract_id_map(values: list):
    mapping = {}
    if isinstance(values, dict):
        for item in values["values"]:
            if "id" in item and "value" in item:
                mapping[item["id"]] = item["value"]
    
    return mapping
    

def replace_value_recursive(obj: dict, id_map: dict):
    if isinstance(obj, dict):
        if "id" in obj and "value" in obj and obj["id"] in id_map:
            obj["value"] = id_map[obj["id"]]
        
        if "values" in obj.keys():
            replace_value_recursive(obj["values"], id_map)
    
    if isinstance(obj, list):
        for item in obj:
            replace_value_recursive(item, id_map)

def write_report_in_file(path, report):
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(report, f, indent=2)
            


if __name__ == "__main__":
    args = argv[1:]
    if len(args) != 3:
        print("Ожидается 3 аргумента")
        exit(1)
    
    report = read_and_serialise(args[0])
    values = read_and_serialise(args[1])
    report_path = args[2]
    
    id_map = extract_id_map(values)
    replace_value_recursive(report["tests"], id_map)
    write_report_in_file(report_path, report)
    
    