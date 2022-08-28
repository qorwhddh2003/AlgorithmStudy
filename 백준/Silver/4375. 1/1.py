try :

    while True :
        n = int(input())

        count = 1
        while True :
            if int('1' * count) % n == 0 :
                print(count)
                break

            count += 1
except :
    exit()