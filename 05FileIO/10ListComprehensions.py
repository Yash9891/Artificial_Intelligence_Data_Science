listi=[1,2,3,4,5,6,7,8,9,10]
sqr=[x*x for x in listi]
oddsqr=[x*x for x in listi if x%2!=0]
print(sqr)
print(oddsqr)

# ans = list(map(lambda x: x*x, [1,2,3,4,5]))
# print(ans)


nums=[-2,-4,5,6,-4]
ans=[0 if val <0 else val for val in nums]
print(ans)

words=["Yash", "Good", "Superman"]

words=[word.upper() for word in words]
print(words)