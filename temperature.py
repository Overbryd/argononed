#!/usr/bin/python3
def get_temp():
    try:
            tempfp = open("/sys/class/thermal/thermal_zone0/temp", "r")
            temp = tempfp.readline()
            tempfp.close()
            return float(int(temp)/1000.0)
    except IOError:
        return 0.0

if __name__ == "__main__":
    temp = get_temp()
    print(temp)
