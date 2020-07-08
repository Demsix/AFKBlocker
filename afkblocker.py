from pynput.keyboard import Key, Controller
from datetime import datetime, timedelta
import random
import time


keyboard = Controller()
# set some movement keys to be pushed randomly
movement_keys = ['e','s','d','f','\\','z','g']
movement_key_list = []


def main():
  random_wait(1,300)
  random_keys = build_keys(movement_keys)
  random_move(random_keys)


def random_wait(min, max):
  wait_time = random.randint(min, max)
  next_execution_time = datetime.now() + timedelta(seconds=wait_time)
  print("Next execution: " + next_execution_time.strftime('%Y-%m-%d %H:%M:%S'))	
  time.sleep(wait_time)


def build_keys(movement_keys):
  movement_key_list = []
  for i in range(random.randint(5, 15)):
    movement_key_list.append(random.choice(movement_keys))
  return movement_key_list


def random_move(random_keys):
  for key in random_keys:
    keyboard.press(key)   
    bonus_keys()		
    time.sleep(random.uniform(0, 0.50))
    keyboard.release(key)
    print("Key pressed: " + key)


def bonus_keys():
  if random.random() > 0.4: 
    bonus_key = random.choice(movement_keys)
    keyboard.press(bonus_key)
  
    if random.random() > 0.2:
      keyboard.press(Key.space)
      keyboard.release(Key.space)
      print("Bonus Jump!")
  
    time.sleep(random.uniform(0, 0.50))
    keyboard.release(bonus_key)
    print("Bonus key: " + bonus_key)
	

while(True):
  main()
