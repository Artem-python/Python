numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summa_before = sum(numbers[:4])
summa_after = sum(numbers[5:])
summa = summa_before + summa_after
Ср_арифметическое = summa / len(numbers)
numbers[4] = Ср_арифметическое
Ср_арифметическое = numbers[:] # TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", Ср_арифметическое)
