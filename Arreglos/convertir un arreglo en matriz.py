def findMatrix(nums):
    from collections import defaultdict
    freq = defaultdict(int)
    result = []

    for num in nums:
        if freq[num] == len(result):
            result.append([])
        result[freq[num]].append(num)
        freq[num] += 1

    print("Entrada: nums =", nums)
    print("Salida:", result)
    print("Explicación: Podemos crear una matriz 2D que contenga las siguientes filas:")
    for row in result:
        print("-", row)
    print("Se utilizaron todos los elementos de nums y cada fila de la matriz 2D contiene números enteros distintos, por lo que es una respuesta válida.")


findMatrix([1,3,4,1,2,3,1])
