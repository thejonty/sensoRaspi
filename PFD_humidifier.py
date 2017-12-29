import numpy as np
#the beginning!!

#store previous N humidity points
humidity_list = []

set_pt = 0.6 #make it a variable?

err_list = []
kp = 0.5
ki = 0.5
Tu = 10
e_n = kp * (h_n - set_pt) + ki/Tu * int_err
#if int(err_list) > lh_thresh
#  turn_off
#elif int(err_list) > hl_thresh
# turn_on
