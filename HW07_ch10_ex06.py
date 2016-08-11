# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def is_sorted(list_name):
    sorted_list = sorted(list_name)
    limit = len(list_name)
    for count in range(0, limit):
        if sorted_list[count] == list_name[count]:
            continue
        else:
            return False
    else:
        return True



def main():
    ...
    # print(is_sorted([1,2,3]))
    # print(is_sorted([1,6,3]))


if __name__ == '__main__':
    main()