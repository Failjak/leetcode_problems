def test_cases(func, keyses: list, params: list, answers: list, debug: bool = True):
    n = len(params)
    if n != len(answers):
        print("Failed: Invalid params!")
        return 

    traceback = []
    for i in range(n):
        
        kwargs = dict(zip(keyses, params[i]))
        res = func(**kwargs)
        answ = answers[i]

        if debug and not res == answ: 
            traceback.append(f"Case: {kwargs}; Result: {res}; Right answer: {answ}")
    
    if debug and traceback:
        print("Failed:")
        for msg in traceback:
            print(msg)
    elif debug:
        print("Cases done sucessful!!")