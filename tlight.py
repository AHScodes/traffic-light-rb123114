import pyfirmata
import time
import threading
aboard=pyfirmata.Arduino('/dev/cu.usbmodem14201')
g1=board.digital[1]
g2=board.digital[2]
g3=board.digital[3]
g4=board.digital[4]
y1=board.digital[5]
y2=board.digital[6]
y3=board.digital[7]
y4=board.digital[8]
r1=board.digital[9]
r2=board.digital[10]
r3=board.digital[11]
r4=board.digital[12]
def trafficlightrotation():
threading.Timer(86400.0,trafficlightrotation).start()
  #opposites green others red
  g1.write[1]
  g2.write[1]
  r3.write[1]
  r4.write[1]
  time.sleep(20)
  g1.write[0]
  g2.write[0]
  y1.write[1]
  y2.write[1]
  time.sleep(4)
  #red lights stay red
  y1.write[0]
  y2.write[0]
  r1.write[1]
  r2.write[1]
  time.sleep(1)
  r3.write[0]
  r4.write[0]
  g3.write[1]
  g4.write[1]
  time.sleep(18)
  g3.write[0]
  g4.write[0]
  y3.write[1]
  y4.write[1]
  time.sleep(3.5)
  y3.write[0]
  y4.write[0]
  r1.write[0]
  r2.write[0]

trafficlightrotation()
  
  


