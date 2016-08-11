# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def cumulative_sum(list_num):
    
    limit = len(list_num)
    sum_list = [0]*limit

    for count in range(0, limit):
        sum_list[count] = sum(list_num[:count+1])
    return sum_list
        


def main():
    ...
    #print(cumulative_sum([1, 2, 3, 5]))
 
if __name__ == '__main__':
    main()
