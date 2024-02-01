#!/usr/bin/env python3

def greet(where):
    print(f'Welcome to the {where}!')

def main():
    greet('Brain Games')
    

if __name__ == '__main__':
    main()

from ..cli import *

print(welcome_user())
