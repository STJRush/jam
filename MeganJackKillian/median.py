61,61,31,15,42,6973,18,26,68,13,19,59,87,94,28,81,93,47,92,31,34,37,71,51,39,13,78,83,63,84,10,53,72,79,91,52,41,22,37,74,16,74,18,68,71,68,48,66,31,31,55,38,83,61,62,59,21,55,68,86,84,41,19,86,85,49,51,19,14,84,37


n_num = [61,61,31,15,42,6973,18,26,68,13,19,59,87,94,28,81,93,47,92,31,34,37,71,51,39,13,78,83,63,84,10,53,72,79,91,52,41,22,37,74,16,74,18,68,71,68,48,66,31,31,55,38,83,61,62,59,21,55,68,86,84,41,19,86,85,49,51,19,14,84,37]

n = len(n_num)
n_num.sort()

if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))