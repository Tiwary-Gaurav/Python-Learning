# def rotate_arr(arr, shift):
#     temp = arr[shift:]+arr[0:shift]
#     print(temp)

# arr = [1,2,3,4,5,6,7]
# rotate_arr(arr, 2)


# for explaining difference between return and yield
def add(x, y):
    return x+y;

def count_down(n):
    while(n>0):
        n -= 1
        print(" first ", n)
        n = n - 1
        print(" second ", n)

#print("Adding: ",add(1, 3))

value = count_down(10)
# for v in value:
#     print("t-",v)
