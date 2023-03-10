##a+b+c=1000, 且a^2+b^2=c^2(a,b,c为自然数)，求a,b,c

# import time

# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a**2 + b**2 == c**2 and a + b + c == 1000:
#                 print("a, b, c: %d, %d, %d" % (a, b, c))

# end_time = time.time()
# print("elapsed: %f" % (end_time - start_time))
# print("complete")
                

# a, b, c: 0, 500, 500
# a, b, c: 200, 375, 425
# a, b, c: 375, 200, 425
# a, b, c: 500, 0, 500
# elapsed: 486.394912
# complete




## 算法的五大特性
# 1. 输入: 算法具有0个或多个输入
# 2. 输出: 算法至少有1个或多个输出
# 3. 有穷性: 算法在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成
# 4. 确定性：算法中的每一步都有确定的含义，不会出现二义性
# 5. 可行性：算法的每一步都是可行的，也就是说每一步都能够执行有限的次数完成       


import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 :
            print("a, b, c: %d, %d, %d" % (a, b, c))

end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete")             


# a, b, c: 0, 500, 500
# a, b, c: 200, 375, 425
# a, b, c: 375, 200, 425
# a, b, c: 500, 0, 500
# elapsed: 486.394912
# complete


