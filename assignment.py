#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time

def bubble_sort(arr):
  for i in range(len(arr) - 1):
    flg = 0
    for j in range(len(arr) - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        flg = 1
    if flg == 0: break
  return arr

def selection_sort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr

def insertion_sort(arr):
  for i in range(1, len(arr)):
    while arr[i-1] > arr[i]:
      arr[i-1], arr[i] = arr[i], arr[i-1]
      i -= 1
      if i == 0: break
  return arr


def test_it():
  n = 5000
  max = 100
  random_data=[random.randint(0, max) for _ in range(n)]
  sorted_data = list(range(n))
  reverse_data = list(reversed(range(n)))

  data = {'sorted_data': sorted_data, 'reverse_data': reverse_data, 'random_data':random_data}
  funs = {'bubble_sort': bubble_sort, 'selection_sort': selection_sort, 'insertion_sort': insertion_sort}

  for k,v in data.items():
    for name,fun in funs.items():
      start = time.time()
      fun(v)
      end = time.time()
      print(f'{name}\ton {k}\t {round(end-start, 2)} \tseconds')

test_it()