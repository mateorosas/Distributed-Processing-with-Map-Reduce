# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()
print(cabecera.strip().split(","))
countYear = []
dateTransfer =[]
for line in sys.stdin:
  arreglo = line.strip().split(",")
  dateTransfer.append(arreglo[2])

for i in dateTransfer:
  date, hour = i.strip().split(" ")
  year, month, day = date.strip().split("-")
  countYear.append(year)

years_s = [str(i) for i in range(1994, 2018, 1)]
for i in years_s:
  repetidos = countYear.count(i)
  print(i, repetidos)