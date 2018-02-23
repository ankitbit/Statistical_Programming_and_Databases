def range_function(num):
    i = 0
    while i < num:
        yield i
        i = i+1

gen_num = range_function(20)

# printing the output of custom range function
for i in range(20):
    print gen_num.next()
