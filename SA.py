import os
from art import logo
print(logo)
print("Welcome to the secret auction program")
dict={}
skr=True

def calc():
  temp=''
  max=0
  for key in dict:
    if(dict[key]>max):
      max=dict[key]
      temp=key
  print(f"The winner is {temp} with a bid of ${max}")
  
while(skr is True):
  a=input("What is your name?")
  b=int(input("What's your Bid? $"))
  dict[a]=b
  cont=input("Are there any other bidders? Type   'yes' or 'no'. ").lower()
  os.system('cls')
  if(cont=='no'):
    calc()
    skr=False

  
