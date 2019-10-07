# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import time
start_time = time.time()
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    # t1 = threading.Thread(target=print_square, args=(10,)) 
    # t2 = threading.Thread(target=print_cube, args=(10,)) 
    
    myThreads = []
    for i in range (100):
        threading.Thread(target=print_square, args=(i,)).start()
        
    # for t in myThreads:
    #     t.join()


    # # starting thread 1 
    # t1.start() 
    # # starting thread 2 
    # t2.start() 
  
    # # wait until thread 1 is completely executed 
    # t1.join() 
    # # wait until thread 2 is completely executed 
    # t2.join() 
  
    # both threads completely executed 
    print ("My program took", time.time() - start_time, "to run")
    print("Done!") 