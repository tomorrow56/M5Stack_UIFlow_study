from m5stack import *
from m5ui import *
import time, _thread, machine


clear_bg(0x222222)


btnA = M5Button(name="ButtonA", text="ButtonA", visibility=False)
btnB = M5Button(name="ButtonB", text="ButtonB", visibility=False)
btnC = M5Button(name="ButtonC", text="ButtonC", visibility=False)


rtc = machine.RTC()
print("Synchronize time from NTP server ...")
lcd.println("Synchronize time from NTP server ...")
rtc.ntp_sync(server="ntp.nict.jp", tz='JST-9')

lcd.clear()
lcd.setBrightness(200)
lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=16, width=2)

while True:
  d = time.strftime("%Y-%m-%d", time.localtime())
  t = time.strftime("%H:%M:%S", time.localtime())
  t2 = time.strftime("%H:%M:%S", time.gmtime())
  lcd.font(lcd.FONT_7seg, fixedwidth=False, dist=8, width=1)
  lcd.print(d, 10, 50, lcd.ORANGE)
  lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=16, width=2)
  lcd.print(t, lcd.CENTER, 100, lcd.CYAN)

  lcd.font(lcd.FONT_7seg, fixedwidth=False, dist=8, width=1)
  lcd.print(t2, lcd.RIGHT, lcd.BOTTOM, lcd.GREEN)
  time.sleep(1)
