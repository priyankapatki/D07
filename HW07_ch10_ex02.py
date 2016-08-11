# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(list_string):
    new_list =[]
    limit = len(list_string)
    for count in range(0, limit):
        if 'str' in str(type(list_string[count])):
            upper_str = str(list_string[count].upper())
            new_list.append(upper_str)

        else:

             new_list = new_list + capitalize_nested(list_string[count])

    return new_list

def main():
    ...
    # s = ['apple', ['bear','dog',['animal']], 'cat']
    # print(capitalize_nested(s))

if __name__ == '__main__':
    main()