def unique_el(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

#Let's try code 
input_list = [1, 2, 3, 2, 4, 1, 5, 3] 
output_list = unique_el(input_list)  
print(output_list)  
