def CountFreq(li):
  freq = {}
  for items in li:
    freq[items] = li.count(items)
  print(freq)
li =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
CountFreq(li)