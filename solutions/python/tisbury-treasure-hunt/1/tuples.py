def get_coordinate(record):
    return record[-1]

def convert_coordinate(coordinate):
    list1=[]
    for i in coordinate:
        list1.append(i)
    return tuple(list1)    
    
def compare_records(azara_record, rui_record):
    return tuple(convert_coordinate(azara_record[-1])) == tuple(rui_record[-2]) 

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"

def clean_up(combined_record_group):
    report = []
    for record in combined_record_group:
        cleaned_record = []
        for item in record:
            if isinstance(item, str) and len(item) == 2 and item[0].isdigit() and item[1].isalpha():
                continue
            cleaned_record.append(item)
        report.append(str(tuple(cleaned_record)))
    return "\n".join(report) + "\n"