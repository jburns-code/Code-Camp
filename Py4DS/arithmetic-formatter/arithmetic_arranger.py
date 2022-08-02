import operator

ops = {"+": operator.add, "-": operator.sub}


def arithmetic_arranger(problems, print_result=False):
    """
    Takes a list of strings of addition or subtraction equations,
    returns the equation in an arithmetic format,
    accepts optional True argument to print the result of the equation
    """
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        pass
        

    full_line1 = []
    full_line2 = []
    full_line3 = []
    full_line4 = []
    hypn = ''
    prob_width = 0

    # split problem into a list of strings
    for problem in problems:
        split_problem = problem.split(' ')

        # check if contains only integers
        for integer in split_problem[0]:
            if integer.isnumeric() == False:
                return 'Error: Numbers must only contain digits.'
            
        for integer in split_problem[-1]:
            if integer.isnumeric() == False:
                return 'Error: Numbers must only contain digits.'
                
        

        # check if length of input value is 4 chars or under
        if len(split_problem[0]) >= 5:
            return 'Error: Numbers cannot be more than four digits.'
        elif len(split_problem[-1]) >= 5:
            return 'Error: Numbers cannot be more than four digits.'
            

        # aliasing each item in split_problem list
        for item in split_problem:
            if item.isdigit() == True:
                if split_problem[0] == item:
                    item1 = item
                elif split_problem[-1] == item:
                    item2 = item
            elif item.isdigit() == False:
                operator = item


        # setting max width, adding 2 for operator and whitespace
        prob_width = max([len(item1),len(item2)]) + 2

        # formatting each of the main lines
        item1 = item1.rjust(prob_width)
        item2 = item2.rjust(prob_width - 2)

        # result line
        try:
            result = str(ops[operator](int(item1),int((item2)))).rjust(prob_width)
        except:
            return "Error: Operator must be '+' or '-'."
            
        
        line2 = f'{operator} {item2}'
        hypn = '-' * prob_width
        empty_space = "    "

        prob_line1 = item1 + empty_space
        prob_line2 = line2 + empty_space
        prob_line3 = hypn + empty_space
        prob_line4 = result + empty_space
        
        full_line1.append(prob_line1)
        full_line2.append(prob_line2)
        full_line3.append(prob_line3)
        full_line4.append(prob_line4)

    final_line1 = ''.join(full_line1)
    final_line2 = ''.join(full_line2)
    final_line3 = ''.join(full_line3)
    final_line4 = ''.join(full_line4)
    

    if print_result == True:
        arranged = f'{final_line1[:-4]}\n{final_line2[:-4]}\n{final_line3[:-4]}\n{final_line4[:-4]}'
    else:
        arranged = f'{final_line1[:-4]}\n{final_line2[:-4]}\n{final_line3[:-4]}'

    return arranged
