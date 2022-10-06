class mathCalcul:

    def math_calcul(self):
        return self


def fibonacciSuite(min: int, max: int):
    result = []
    tmp_min1 = min
    tmp_min2 = 0
    for i in range(max):
        if tmp_min1 < max:
            if tmp_min2 == 0:
                result.append({"value": i, "result": tmp_min2})
                tmp_min1 = 1
                result.append({"value": i + 1, "result": tmp_min1})
                tmp_min2 = tmp_min1
            else:
                result.append({"value": i + 1, "result": tmp_min1})
                tmp_min2 = tmp_min1
                tmp_min1 = result[i]["result"] + tmp_min2
    for i in range(len(result)):
        print("Valeur de la suite de pour le nombre :", result[i]["value"], " a pour résultats ", result[i]["result"])
    return None
