#Name: Christopher Arraya
#ID: 1767362

#Warmup-2 > string_times

def string_times(str, n):
  return str*n

#Warmup-2 > front_times

def front_times(str, n):
  return str[:3]*n or str*n

#Warmup-2 > string_bits

def string_bits(str):
  return str[::2]

#Warmup-2 > string_splosion

def string_splosion(str):
  return ''.join(str[:i] for i in range(1, len(str) + 1))

#Warmup-2 > last2

def last2(str):
  return sum(1 for x in range(len(str)-1) if str[x:x+2] == str[-2:] and x != len(str)-2)

#Warmup-2 > array_count9

def array_count9(nums):
  return nums.count(9)

#Warmup-2 > array_front9

def array_front9(nums):
  return  nums[:4].count(9)>=1 or len(nums)<4 and nums[:].count(9)>=1

#Warmup-2 > array123

def array123(nums):
  return set([1,2,3]).issubset(nums)

#Warmup-2 > string_match

def string_match(a, b):
  return sum(1 for x in range(min(len(a),len(b))-1) if a[x:x+2]==b[x:x+2])

#Logic-2 > make_bricks

def make_bricks(small, big, goal):
  return goal%5<=small and goal-big*5<=small

#Logic-2 > lone_sum

def lone_sum(a, b, c):
  return sum(x for x in [a,b,c] if [a,b,c].count(x)==1)

#Logic-2 > lucky_sum

def lucky_sum(a, b, c):
  return sum(i for i in [a,b,c,13][:[a,b,c,13].index(13)])

#Logic-2 > no_teen_sum

def no_teen_sum(a, b, c):
  return sum(x for x in [a,b,c] if x not in range(13,15) and x not in range(17,20))

#Logic-2 > round_sum

def round_sum(a, b, c):
  return int(round(a,-1)+round(b,-1)+round(c,-1)) #second parameter is to what place you wanna round (-1 because not rounding would be ones place, -1 would be one place bigger which is tens place)

#Logic-2 > close_far

def close_far(a, b, c):
  return (abs(abs(b)-abs(a))<=1 and abs(abs(c)-abs(a))>=2 or abs(abs(c)-abs(a))<=1 and abs(abs(b)-abs(a))>=2) and abs(abs(b)-abs(c))>=2 

#Logic-2 > make_chocolate

def make_chocolate(small, big, goal):
  return  goal - ((big if(5 * big <= goal) else goal / 5) * 5)  if small >= (goal - ((big if(5 * big <= goal) else goal / 5) * 5)) else -1

#String-2 > double_char

def double_char(str):
  return ''.join(char*2 for char in str) 

#String-2 > count_hi

def count_hi(str):
  return str.count('hi')

#String-2 > cat_dog

def cat_dog(str):
  return str.count('dog')==str.count('cat')

#String-2 > count_code

def count_code(str):
  return sum(1 for x in range(len(str)-3) if str[x:x+2]=='co' and str[x+3]=='e')

#String-2 > end_other

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

#List-2 > count_evens

def count_evens(nums):
  return sum(1 for n in nums if n%2==0)
 
#List-2 > big_diff

def big_diff(nums):
  return max(nums)-min(nums)

#List-2 > centered_average

def centered_average(nums):
  return (sum(nums)-max(nums)-min(nums))/(len(nums)-2)

#List-2 > sum13

def sum13(nums):
  return sum(x for x,i in zip(nums,[0]+nums)if 13 not in(x,i))

#List-2 > sum67

def sum67(nums):
  while 6 in nums: del nums[nums.index(6):nums[nums.index(6):].index(7)+nums.index(6)+1]
  return sum(i for i in nums)

#List-2 > has22

def has22(nums):
  return sum(1 for x in range(len(nums)-1) if nums[x]==nums[x+1]==2)>=1 