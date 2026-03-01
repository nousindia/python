k=2
m=2
n=2
total=k+m+n
prob=0
term1= 1 - (((m + n) * (m + n - 1)) / (total * (total - 1)))
term2= ((m * (m - 1)) / (total * (total - 1))) * 0.75
term3= (2 * m * n) / ((k+m+n) * ((k+m+n) - 1))
print(term1,term2,term3)