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

    stime = time.time()

    for word in WORDS:
        print(hash(word))

    etime = time.time()
    print(f'time taken:\t{etime - stime}')

    #---------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()