import numpy as np
from random import random
import matplotlib.pyplot as plt
from argparse import ArgumentParser

def drunken_walk(n, p=0.7):
    x = 0
    hist = []

    for i in range(n):
        if random() < p:
            x += 1
        else:
            x -= 1
        hist.append(x)
        
    return np.asarray(hist)

def main():
    parser = ArgumentParser()
    
    parser.add_argument('-n', '--number', dest='n', type=int, help='Specify number of steps', default=1000)
    parser.add_argument('-p', dest='p', type=float, help='Specify forward propability', default=0.7)
    parser.add_argument('-z', dest='z', type=int, help='Specify number of drunkards', default=10)

    args = parser.parse_args()
    
    plt.title('Drunkard\'s Walk [z={:};p={:}]'.format(args.z, args.p))
    plt.plot(np.arange(args.n), np.repeat(0, args.n), color='#444444')
    for i in range(args.z):
        plt.plot(np.arange(args.n), drunken_walk(args.n, args.p))
    plt.show()

if __name__ == '__main__':
    main()