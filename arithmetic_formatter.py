# Arithmetic Formatter solution for freeCodeCamp Scientific Computing with Python certification

def arithmetic_arranger(problems, show_res=False):
    allowed_operators = ["+", "-"]
    num_of_problems = 5

    # check for number of max. problems
    if len(problems) > num_of_problems:
        return "Error: Too many problems."

    results = []
    for i in problems:
        problem = i.split()

        # check for operators
        if problem[1] not in allowed_operators:
            return "Error: Operator must be '+' or '-'."

        # check for operand length
        if (len(problem[0]) > 4) or (len(problem[2]) > 4):
            return "Error: Numbers cannot be more than four digits."

        if len(problem[0]) > len(problem[2]):
            problem.append(len(problem[0]))
        else:
            problem.append(len(problem[2]))

        # check for digits
        try:
            problem[0] = int(problem[0])
            problem[2] = int(problem[2])
        except:
            return "Error: Numbers must only contain digits."

        # result
        if problem[1] == "+":
            result = problem[0] + problem[2]
            problem.append(result)
        else:
            result = problem[0] - problem[2]
            problem.append(result)

        results.append(problem)

    line1, line2, line3, line4 = "", "", "", ""
    j = 0
    for _ in results:
        l1 = f" " * (results[j][3] + 2 - len(str(results[j][0]))) + f"{results[j][0]}"
        l2 = f"{results[j][1]}" + f" " * (results[j][3] + 1 - len(str(results[j][2]))) + f"{results[j][2]}"
        l3 = f"-" * ((results[j][3]) + 2)
        l4 = f" " * (results[j][3] + 2 - len(str(results[j][4]))) + f"{results[j][4]}"

        if j == 0:
            line1 += l1
            line2 += l2
            line3 += l3
            line4 += l4
        else:
            line1 += f" " * 4 + l1
            line2 += f" " * 4 + l2
            line3 += f" " * 4 + l3
            line4 += f" " * 4 + l4
        j += 1

    if show_res:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        return arranged_problems

    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3
        return arranged_problems
