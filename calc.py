#!/usr/bin/env python3

import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
parser.add_argument('nbr_of_days')
args = parser.parse_args()
filename = args.file_name
nbr_of_days = int(args.nbr_of_days)

f = open(filename)
d = list(csv.reader(f))
f.close()

nbr_of_lns = len(d)
sum_red = 0
sum_yel = 0
sum_grn = 0
sum_ttl = 0
sum_wt = 0.0
sum_x = 0
if nbr_of_lns < nbr_of_days:
    nbr_of_days = nbr_of_lns
start = nbr_of_lns - nbr_of_days 
for x in range(start, nbr_of_lns):
    (date, red, yel, grn, ttl, wt) = d[x]
    sum_red = sum_red + int(red)
    sum_yel = sum_yel + int(yel)
    sum_grn = sum_grn + int(grn)
    sum_ttl = sum_ttl + int(ttl)
    sum_wt = sum_wt + float(wt )
    sum_x = sum_x + x
mean_red = sum_red / nbr_of_days
mean_yel = sum_yel / nbr_of_days
mean_grn = sum_grn / nbr_of_days
mean_ttl = sum_ttl / nbr_of_days
mean_wt = sum_wt / nbr_of_days
mean_x = sum_x / nbr_of_days
red_num = 0.0
com_den = 0.0
yel_num = 0.0
grn_num = 0.0
ttl_num = 0.0
wt_num = 0.0
for x in range(start, nbr_of_lns):
    (date, red, yel, grn, ttl, wt) = d[x]
    com_den = com_den + (x - mean_x)**2
    red_num = red_num + (int(red) - mean_red) * (x - mean_x)
    yel_num = yel_num + (int(yel) - mean_yel) * (x - mean_x)
    grn_num = grn_num + (int(grn) - mean_grn) * (x - mean_x)
    ttl_num = ttl_num + (int(ttl) - mean_ttl) * (x - mean_x)
    wt_num = wt_num + (float(wt) - mean_wt ) * (x - mean_x)
red_slope = red_num / com_den 
yel_slope = yel_num / com_den
grn_slope = grn_num / com_den
ttl_slope = ttl_num /com_den
wt_slope = wt_num / com_den

print(d[nbr_of_lns -1])

print("           Mean    Slope")
print("Red:    {0:+7.0f}   {1:+5.1f}".format(mean_red, red_slope))
print("Yel:    {0:+7.0f}   {1:+5.1f}".format(mean_yel, yel_slope))
print("Grn:    {0:+7.0f}   {1:+5.1f}".format(mean_grn, grn_slope))
print("Ttl:    {0:+7.0f}   {1:+5.1f}".format(mean_ttl, ttl_slope))
print("Weight:   {0:+7.1f}  {1:+5.2f}".format(mean_wt, wt_slope))
input()
