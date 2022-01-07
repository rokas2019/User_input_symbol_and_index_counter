# Stores input from User to list until ENTER/RETURN pressed
def user_input() -> []:
    list_of_symbols = []
    while True:
        entry = input("If You want to end operation press Enter/Return \n"
                      "Enter a sentence or a symbol: ")
        if len(entry) != 0:
            list_of_symbols.append(entry)
        if len(entry) == 0:
            break
    return list_of_symbols


# Function to print length and index of symbols from collected input list
def prints_list_items_and_lengths(any_list: []):
    for i in any_list:
        element_length = len(i)
        element_index = any_list.index(i)
        print(f'Length of {i} is: {element_length} symbols\n'
              f'Index of this element in list: {element_index}')


# Runs main program
if __name__ == '__main__':
    prints_list_items_and_lengths(user_input())
