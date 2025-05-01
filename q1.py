from hashlib import sha512

import multiprocessing as mp
import time

WORDS = ['extra-large', 'invincible', 'furtive', 'stare', 'ruddy', 'adaptable', 'daily', 'letters', 'houses', 'grate', 'fog', 'stupendous']

def hash(word: str):
    hash_object = sha512()
    for _ in range(100):
        time.sleep(.01)
        byte_data = word.encode('utf-8')
        hash_object.update(byte_data)
        word = hash_object.hexdigest()
    return word

def main():

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------
    start = time.time() # start time
    with mp.Pool() as pool: # create parallel processes to hash WORDS
        results = pool.map(hash, WORDS)
    end = time.time() # end time
    total_time = (end - start)
    
    for i in results: # print words
        print(i)
    print("Total time: ", total_time) # print total time
    #---------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()