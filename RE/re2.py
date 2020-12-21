import sys; args = sys.argv[1:]

idx = int(args[0])-40

myRegexLst = [
  r"/^[xo\.]{64}$/i",
  r"/^[xo]*\.[xo]*$/i",
  r"/^\.|\.$|^x+o*\.|\.o*x+$/i",
  r"/^.(..)*$/s", 
  r"/^(0|1[01])([01]{2})*$/",
  r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
  r"/^(0|10)*1*$/",
  r"/^[bc]+(a?[bc]*)$|^a[bc]*$/",
  r"/^[bc]*(a[bc]*a[bc]*|[bc])+$/",
  r"/^(2|1[02]*1)([02]*1[02]*1)*[02]*$/",
]   

if idx < len(myRegexLst):
  print(myRegexLst[idx])