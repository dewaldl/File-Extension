def read_file(file_dir: str) -> dict:
    if file_dir.rfind(file_extension) == -1:
        print("\nERROR: Incorrect file extension\n")
        return {}
    
    # Open File and set up variables
    file = open(file_dir, 'r')
    dict_to_return: dict = {}
    end_of_file = False
    file_content = file.read()
    
    while not end_of_file:
        # Indexes of chars  ':', '{' and '}'
        colon = file_content.index(':')
        first_bracket = file_content.index('{')
        second_bracket = file_content.index('}')

        # Find key, data and type from indexes
        key = file_content[:colon].strip()
        data_type = file_content[colon+1:first_bracket].strip()
        data = file_content[first_bracket+1:second_bracket].strip()

        # Typecasting based on indicated data type
        match data_type:
            case "int": data = int(data)
            case "str": data = str(data)
            case "float": data = float(data)
            case _: data = str(data)

        # Update dict_to_return with new data
        dict_to_return.update({key: {'data':data, "type":data_type}})

        file_content = file_content[second_bracket+1:]
        if len(file_content) <= 1:
            end_of_file = True
            #break


    return dict_to_return

#----------------------------------------------------------------------------
file_extension: str = ".abc"
data: dict = read_file("demo.abc")
print(data)
