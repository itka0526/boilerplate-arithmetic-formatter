def arithmetic_arranger(problems: list[str], display = False):
    results: list[str] = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        [first, operation, second] = problem.split(" ")

        if operation not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        elif first.isnumeric() == False or second.isnumeric() == False:
            return "Error: Numbers must only contain digits."
        elif len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        space = max( len(first), len(second) ) + 2

        showResult = f"{eval(problem):>{space}}" if display else ""
        r = f"""{first:>{space}}
{operation:>1}{second:>{space - 1}}
{"-"*( space ):>{space}}
{showResult}"""
        
        results.append(r)

    lines = {}

    for result in results:
        splitted = result.splitlines()

        for idx in range(len(splitted)):
            if lines.get(idx):
                lines[idx] = lines[idx] + " "*4 + splitted[idx]
            else: 
                lines[idx] = splitted[idx]

    final = ""
    for i in lines:
        final += lines[i] + '\n'
    return final[:-1]
