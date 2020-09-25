import os
if os.path.exists("AppData\personal.ini"):
  os.remove("AppData\personal.ini")
else:
  print("RWI already reset !")
