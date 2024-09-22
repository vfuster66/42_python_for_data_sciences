def NULL_not_found(obj: any) -> int:
    # Vérifier chaque type et afficher le résultat correspondant
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
    elif isinstance(obj, float) and obj != obj:  # Vérifier NaN (car NaN != NaN)
        print(f"Cheese: nan {type(obj)}")
    elif obj is False:
        print(f"Fake: {obj} {type(obj)}")
    elif obj == 0:
        print(f"Zero: {obj} {type(obj)}")
    elif obj == '':
        print(f"Empty: {obj} {type(obj)}")
    else:
        print("Type not Found")
        return 1
    
    return 0
