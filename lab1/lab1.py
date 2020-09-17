#Name: Christopher Arraya
#ID: 1767362

#Warmup-1 > sleep_in
def sleep_in(weekday, vacation):
  return not weekday or vacation

#Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

#Warmup-1 > sum_double
def sum_double(a, b):
  return 2*(a+b) if a==b else a+b

#Warmup-1 > diff21
def diff21(n):
  return 2*(n-21) if n>21 else 21-n

#Warmup-1 > parrot_trouble
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

#Warmup-1 > makes10
def makes10(a, b):
  return (a == 10 or b == 10) or (a+b == 10)

#Warmup-1 > near_hundred
def near_hundred(n):
  return (abs(n-100)<=10) or (abs(n-200)<=10)

#Warmup-1 > pos_neg
def pos_neg(a, b, negative):
  return (a < 0 and b < 0) if negative else (a<0 and b>0) or (a>0 and b<0)

#String-1 > hello_name
def hello_name(name):
  return 'Hello '+name+'!'

#String-1 > make_abba
def make_abba(a, b):
  return a+b+b+a

#String-1 > make_tags
def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'

#String-1 > make_out_word
def make_out_word(out, word):
  return out[:len(out)//2]+word+out[len(out)//2:]

#String-1 > extra_end
def extra_end(str):
  return str[len(str)-2:]*3

#String-1 > first_two
def first_two(str):
  return str if len(str)<2 else str[:2]

#String-1 > first_half
def first_half(str):
  return str[:len(str)//2]

#String-1 > without_end
def without_end(str):
  return str[1:len(str)-1]

#List-1 > first_last6
def first_last6(nums):
  return '6' == str(nums[0]) or '6' == str(nums[len(nums)-1])

#List-1 > same_first_last
def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[len(nums)-1])

#List-1 > make_pi
def make_pi(n):
    return list(map(int, [n for n in list('3141592653589'[:n])]))
    
#List-1 > common_end
def common_end(a, b):
  return (a[0] == b[0]) or (a[len(a)-1] == b[len(b)-1])

#List-1 > sum3
def sum3(nums):
  return sum(nums)

#List-1 > rotate_left3
def rotate_left3(nums):
  return nums if not nums else nums[1:] + nums[0:1]

#List-1 > reverse3
def reverse3(nums): 
  return nums[::-1]

#List-1 > max_end3
def max_end3(nums):
  return [max(nums[0], nums[-1])] * len(nums)

#Logic-1 > cigar_party
def cigar_party(cigars, is_weekend):
  return (is_weekend and cigars>=40) or (cigars>=40 and cigars <=60)

#Logic-1 > date_fashion
def date_fashion(you, date):
  return 2 if (you>=8 or date>=8) and (you>2 and date>2) else 0 if you<=2 or date<=2 else 1

#Logic-1 > squirrel_play
def squirrel_play(temp, is_summer):
  return (is_summer and 60<=temp<=100) or (not is_summer and 60<=temp<=90)

#Logic-1 > caught_speeding
def caught_speeding(speed, is_birthday):
  return 0 if (is_birthday and speed-5<=60) else 1 if (is_birthday and 61<=speed-5<=80) else 0 if (not is_birthday and speed<=60) else 1 if (not is_birthday and 61<=speed<=80) else 2

#Logic-1 > sorta_sum
def sorta_sum(a, b):
  return 20 if a+b in range(10,20) else a+b

#Logic-1 > alarm_clock
def alarm_clock(day, vacation):
  return '10:00' if (vacation and day in range(1,6)) else 'off' if (vacation and (day==6 or day==0)) else '7:00' if (not vacation and day in range (1,6)) else '10:00'

#Logic-1 > love6
def love6(a, b):
  return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

#Logic-1 > in1to10
def in1to10(n, outside_mode):
  return n<=1 or n>=10 if outside_mode else n in range(1,11)
