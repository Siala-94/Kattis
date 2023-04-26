def satisfy(clauses, n, variables):
    if n == 0:
        for clause in clauses:
            fulfilled = False
            for var in clause:
                if variables[var[0]] == var[1]:
                    fulfilled = True
            if not fulfilled:
                return False
        return True

    variables[n - 1] = 1
    if satisfy(clauses, n - 1, variables):
        return True

    variables[n - 1] = 0
    if satisfy(clauses, n - 1, variables):
        return True

    return False


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    variables = [-1] * n
    clauses = []

    for j in range(m):
        line = input().strip()
        clause = []
        for literal in line.split(' v '):
            tilde = False
            if literal[0] == '~':
                tilde = True
                literal = literal[1:]
            num = int(literal[1:]) - 1
            clause.append((num, not tilde))
        clauses.append(clause)


    print('satisfiable' if satisfy(clauses, n, variables) else 'unsatisfiable')
  
