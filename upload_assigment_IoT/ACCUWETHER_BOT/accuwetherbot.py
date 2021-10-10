#required packages
import machine
import ujson as json
import urequests as requests
import ssd1306

#API Call & print infomation in shell
API="XZRyTFd0qQe6GvGnkkiJmkNlxgdxYHlL"

print("****CHENNAI REPORT****")

URL="http://dataservice.accuweather.com/forecasts/v1/daily/1day/206671?apikey="+API+"&details=true"

response=requests.get(URL)
data=response.json()
for i in data['DailyForecasts']:
    print("Temp.MAX","%0.2f"%(((i['Temperature']['Maximum']['Value'])-32)/1.8),"deg")
    print("Temp.MIN","%0.2f"%(((i['Temperature']['Minimum']['Value'])-32)/1.8),"deg")
    print("Total Rain","%0.2f"%(((i['Day']['Rain']['Value'])+(i['Night']['Rain']['Value']))*25.4),"mm")

#Initializing OLED(SSD 1306)
scl = machine.Pin(1, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(2, machine.Pin.OUT, machine.Pin.PULL_UP)
i2c = machine.I2C(scl=scl, sda=sda)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

#function for printing infomation in OLED
def printinfo(msg, x, y, clr):
    if clr:
        oled.fill(0)
    oled.text(msg, x, y)
    oled.show()

#Assigning variable for printing
for i in data['DailyForecasts']:
    tempma=(((i['Temperature']['Maximum']['Value'])-32)/1.8)
    tempmi=(((i['Temperature']['Minimum']['Value'])-32)/1.8)
    rain=(((i['Day']['Rain']['Value'])+(i['Night']['Rain']['Value']))*25.4)
    
#Displaying in OLED
printinfo('**Accuwewther-REP**', 3, 5, 1)
printinfo('Temp.Max:{} oC' .format(tempma), 3, 15, 0)
printinfo('Temp.Min:{} oC' .format(tempmi), 3, 25, 0)
printinfo('Total Rain:{} mm' .format(rain), 3, 35, 0)
