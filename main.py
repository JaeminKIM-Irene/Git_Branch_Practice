# 1. 둘 다 버린다.
# 2. 둘 다 살린다.
# 3. (완전히) 다른 대안을 선택한다.
def print_hello(num:int) :
    """
    Print hello
    """
    for i in range(num) :
        if i%2==0 : 
            print(f'{i}번째 안녕')

if __name__ == '__main__' :
    print_hello(10)
