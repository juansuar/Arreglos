def frequencySort(nums):
    unique_nums = []
    frequencies = []
    
    for num in nums:
        if num in unique_nums:
            index = unique_nums.index(num)
            frequencies[index] += 1
        else:
            unique_nums.append(num)
            frequencies.append(1)

    
    pairs = [(num, freq) for num, freq in zip(unique_nums, frequencies)]


    pairs.sort(key=lambda x: (-x[1], nums.index(x[0])))


    result = []
    for num, freq in pairs:
        result.extend([num] * freq)

    print("Entrada: nums =", nums)
    print("Salida:", result)
    print("Explicación:")
    print("4 aparece 3 veces.")
    print("3 aparece 2 veces.")
    print("6 aparece 2 veces.")
    print("1 aparece 1 vez.")
    print("Se colocan en orden de frecuencia descendente, manteniendo el orden relativo en caso de empate.")

# Ejemplo de uso
frequencySort([4,3,1,6,3,4,4,6])
