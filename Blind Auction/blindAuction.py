dict = {}
print("Welcome to squid game auction")

val = True

while(val):
    name = input("Please enter your name :\n")
    bid = int(input("please place your bid :\n"))
    dict[name] = bid 
    ask = input("Anyone else bidding ?\n")

    if(ask == "no"):
      val = False
      m = 0
      for element in dict:
        m = max(m,dict[element])
      print(dict)  
      print(f"the highest bid is {m}")
 
