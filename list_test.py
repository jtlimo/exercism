#!/usr/bin/python
# -*- coding: utf-8 -*-
def oi(num_list=[1,2,3], original_list=[], new_list=[]):
    if not original_list:
        print("first num list", num_list)
        original_list = num_list.copy()

    for index, num in enumerate(num_list):
        i = index + 1
        new_list.append(num_list)
        print("the new list when appending the num list value on the new list", new_list)
        if i > len(num_list) - 1:
            if num_list == original_list:
                print("printing the new list before break function", new_list)
                break
            oi(num_list, original_list)
        else:
            num_list[index] = num_list[index + 1]
            num_list[index + 1] = num
            print("num list", num_list)
            print("new list", new_list)

if __name__ == '__main__':
    oi()
