import concurrent.futures
import time 

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds}sec')
    time.sleep(seconds)
    return f'done sleeping {seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5 , 4 , 3 , 2, 1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)
     
#executor implementation 2
#     secs = [5 , 4 , 3 , 2 , 1]
#     results = [executor.submit(do_something , sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

#executor implementation 1
    # f1 = executor.submit(do_something, 1)
    # f1 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f1.result())




finish = time.perf_counter()
print(f'Finished in {round (finish - start , 2)} seconds')