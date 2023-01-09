#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
   new_tuple_a = tuple_a + (0, 0)
   new_tuple_b = tuple_b + (0,0)
   result_1= new_tuple_a[0] + new_tuple_b[0]
   result_2 = new_tuple_a[1] + new_tuple_b[1]
   return result_1, result_2

  