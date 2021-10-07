def fancy_divide(list_of_numbers, index):
    try:
        denom = list_of_numbers[index]
        return [simple_divide(item, denom) for item in list_of_numbers]
    except:
        for i in range(len(list_of_numbers)):
                list_of_numbers[i]=0
        return list_of_numbers

def simple_divide(item, denom):
   return item / denom
