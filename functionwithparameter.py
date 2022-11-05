import math
def paint_calc(height,width,cover):
  cost=(height*width)/cover
  final=math.ceil(cost)
  print(f"The no of cans needed is {final}")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
