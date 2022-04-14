i = "hello there"
blue = "\033[1;34;40m"
print(blue, i, end = '')
print("\033[0;32;40m" ,i , end='')
print("done")