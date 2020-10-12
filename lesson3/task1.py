import time

def auto_repeat(count_of_repeat):

    def actual_decorator(func):

        def wrapper(a, b):
            all_time = 0
            for i in range(count_of_repeat):
                start_time = time.time()
                print('function started')
                result = func(a,b) + i
                print('function ended')
                end_time = time.time() - start_time
                all_time += end_time
                print (f'Time to end {i+1} function - {end_time}')
            print(f'Time to end all function - {all_time}')

            return result

        return wrapper

    return actual_decorator


@auto_repeat(10)
def sum_(a, b):
    return a + b

result = sum_(10, 15)
print(sum_.__name__)
print(result)


