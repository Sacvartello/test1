file = open("./test.txt", "r")
f =file.read().split()
a = int(f[0])
# plus = int(f[0])
# times = int(f[0])
# over = int(f[0])
f.pop(0)

for num in f:
    print("f", num)
    a = a - int(num) * 3
    # plus = plus + int(num)
    # times = times * int(num)
    # over = over / int(num)

out =open("./put.txt","w")
#res = str(plus)+ " "+ str(times)+"\n" + str(over)
res= str(a)
out.write(res)

file.close()
out.close()