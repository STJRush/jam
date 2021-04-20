n_num = [784400000,156880000,5490800000,392200000,392200000,235320000,78440000]
n = len(n_num)
n_num.sort()
 
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))