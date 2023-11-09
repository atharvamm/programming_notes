from scipy import stats


x = [8,4,0,-4]
y = [-16,-12,-10,2]
x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)
x_min_xmean_sq = sum([(ele - x_mean)**2 for ele in x])
y_min_ymean_sq = sum([(ele - y_mean)**2 for ele in y])
den = (x_min_xmean_sq*y_min_ymean_sq)**0.5
num = sum([(elex - x_mean)*(eley - y_mean) for elex,eley in zip(x,y)])
# print(num/den)

correlation_coefficient, p_value = stats.pearsonr(x, y)
print("Pearson's correlation coefficient:", correlation_coefficient)

print("X:",x)
print("Y:",y)
print("X Mean:",x_mean)
print("Y Mean:",y_mean)
print("Numerator:",num)
print("Denominator:",den,x_min_xmean_sq,y_min_ymean_sq)

