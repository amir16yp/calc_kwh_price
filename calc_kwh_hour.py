#!/usr/bin/python3

def uptime2():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds / 3600

kwh_price = 0.5066
uptime = uptime2()
watt_hour = 4.0
price = ((kwh_price / 1000) * watt_hour) * uptime 
print("uptime: " + str(uptime) + " hours")
print("kwh price: " + str(kwh_price))
print("price (including VAT): " + str(price))
