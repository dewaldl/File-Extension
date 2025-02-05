def read_file(file_dir: str) -> dict:
    # Check File Extension
    if file_dir.rfind(file_extension) == -1:
        print("\nERROR: Incorrect file extension\n")
        return {}
    
    # Variables
    dict_to_return: dict = {}
    end_of_file: bool = False

    # File
    file = open(file_dir, 'r')
    file_content = file.read()
    
    # Extract All Data
    while not end_of_file:
        # Indexes of Characters
        colon: int = file_content.index(':')
        first_bracket: int = file_content.index('{')
        second_bracket: int = file_content.index('}')

        # Find key, data and type
        key: str = file_content[:colon].strip()
        data_type: str = file_content[colon+1:first_bracket].strip()
        data: str = file_content[first_bracket+1:second_bracket].strip()

        # Assign Indicated Types
        match data_type:
            case "int": data = int(data)
            case "str": data = str(data)
            case "float": data = float(data)
            case _: 
                data = str(data)
                data_type = "str"

        # Update Dictionary
        dict_to_return.update({key: {"data":data, "type":data_type}})

        # EOF Check
        file_content = file_content[second_bracket+1:]
        if len(file_content) <= 2:
            end_of_file = True

    file.close()
    
    # Get rid of duplicates in original file
    # (Ask Author for explanation as to why it works)
    write_file(file_dir, dict_to_return, append=False)

    return dict_to_return


def write_file(file_dir: str, dict_to_write: dict, append: bool=True) -> None:
    file = open(file_dir, mode='a' if append else 'w')
    
    # Format and Write Data
    for key, values in dict_to_write.items():
        file.write(f"{key} : {values["type"]}" + " {\n" + f"\t{values["data"]}" + "\n}\n\n")
        
    file.close()


#---------------------------------------------------------------------- ------

file_extension: str = ".dse"

# Uncomment this to test the write_file() function
# It won't crash if demo.*file_extension* already contains data
# Duplicate data is removed automatically
write_file(f"demo{file_extension}", {"name":{"data":"tristan", "type":"str"}, 
                                     "age":{"data":13, "type":"int"},
                                     "best_dad_ever":{"data":"dewald", "type":"str"},
                                     "beste_seun_ooit":{"data":"tristan", "type":"str"},
                                     "boodskap":{"data":"Geniet jou dag. Sien jou Donderdag. Pappa is baie lief vir jou!!", "type":"str"}}, 
                                     append=False)

data: dict = read_file(f"demo{file_extension}")
print(data)
