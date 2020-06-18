# import multiprocessing
# import time
# from tqdm import tqdm

# # bar
# def bar():
#     for i in range(5):
#         # print ("Tick")
#         time.sleep(1)

# if __name__ == '__main__':
#     # Start bar as a process
#     p = multiprocessing.Process(target=bar)
#     p.start()
#     cnt = 0 
#     with tqdm(total=10,desc='Compilation',initial=0) as pbar:
#         for i in range(9):
#             time.sleep(1)
#             pbar.update(1)
#             cnt += 1
#             if not p.is_alive():
#                 pbar.update(10-cnt)
#                 break

#     # Wait for 10 seconds or until process finishes
    

#     # If thread is still active
#     if p.is_alive():
#         print ("running... let's kill it...")

#         # Terminate
#         p.terminate()
#         p.join()

# # import os

# # while True :
# #     cmd = input("-> ")

# #     if os.system(cmd) == 0:
# #         print("Done")
# #     else :
# #         print("Got problem")


import multiprocessing

def worker(procnum, return_dict):
    '''worker function'''
    print (str(procnum) + ' represent!')
    return_dict[procnum] = str(procnum)+'fuck'


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print (return_dict.values())