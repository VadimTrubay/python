from multiprocessing import cpu_count
from time import time

def factorize(*number):
    result = []
    for num in number:
        if num % 2 == 0: #Парне
            x = []
            for i in range(1,num+2,1):
                if num % i == 0:
                    x.append(i)
            if bool(x):
                result.append(x)

        if num % 2 == 1: #Не парне
            x = []
            for i in range(1,num+2,2):
                if num % i == 0:
                    x.append(i)
            if bool(x):
                result.append(x)
    return result


if __name__ == "__main__":
    timer = time()
    a,b,c,d,e,f,g,v,n,m = factorize(128,255,99999,10651060,1522288,3456886,6568868,8775788,6659000,6568765)
    print(time()- timer)
    #print(cpu_count())   #4ядра

