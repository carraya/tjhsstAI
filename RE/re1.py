import sys; args = sys.argv[1:]

idx = int(args[0])-30

myRegexLst = [
  r"/^0$|^100$|^101$/",
  r"/^[01]*$/", 
  r"/^.*0$/",
  r"/\w*[aeiou]\w*[aeiou]\w*/i",
  r"/^1[01]*0$|^0$/",
  r"/^[01]*?[01]*110+[01]*[01]*?$/",
  r"/^.{2,4}$/s",
  r"/^\s*?[0-9]{3}\s*?-?\s*?[0-9]{2}\s*?-?\s*?[0-9]{4}\s*?$/",
  r"/^.*?d\w*/im",
  r"/^1[01]+?1$|^0[01]+?0$|^0*$|^1*$/"
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])
