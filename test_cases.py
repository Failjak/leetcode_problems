def test_cases(func, cases: list):
    flag = True
    for case, answ in cases:
        res = func(*case)
        if not res == answ: 
            flag = False
            print(f"Case: {case}; Result: {res}; Right answer: {answ}")
    if flag:
        print("Cases done sucessful!!")