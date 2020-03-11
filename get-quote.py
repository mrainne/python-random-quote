import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd = random.randint(0, last)
  print(quotes[rnd], end='')
  print(quotes[random.randint(0, len(quotes)-1)], end='')
if __name__== "__main__":
  primary()
