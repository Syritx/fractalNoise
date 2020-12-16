import math
import random

seed = random.randint(1,100000000)

class vector2:
    x = 0
    y = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

def interpolate(a, b, w):
    return pow(w,2)*(3 - 2 * w)*(b-a)+a


def generateGradient(ix, iy):
    rand = seed * math.sin(ix*21942+iy*171324+8912) * math.cos(ix*23157*iy*217832+6758)
    gradient = vector2(math.sin(rand), math.cos(rand))
    return gradient

def dotproduct(ix, iy, x, y):
    gradient = generateGradient(ix,iy)

    distancex = x - float(ix)
    distancey = y - float(iy)

    return (distancex*gradient.x + distancey*gradient.y)

def noise(x,y):
    x0 = int(x)
    x1 = x0+1
    y0 = int(y)
    y1 = y0+1

    sx = x - float(x0)
    sy = y - float(y0)

    d1 = dotproduct(x0,y0,x,y)
    d2 = dotproduct(x1,y0,x,y)
    int1 = interpolate(d1,d2,sx)

    d3 = dotproduct(x0,y1,x,y)
    d4 = dotproduct(x1,y1,x,y)
    int2 = interpolate(d3,d4,sx)

    val = interpolate(int1,int2, sy)
    return val

def main():

    width  = 1000
    height = 1000
    allrows = []

    for x in range(width):
        row = []

        for y in range(height):
            val = 0

            frequency = float(.5)
            amplitude = float(100)

            for layer in range(5):

                relx = (float(x)/float(width))*(frequency)
                rely = (float(y)/float(height))*(frequency)

                point = noise(relx,rely)*amplitude
                val = val + noise(interpolate(point, point+relx, relx), interpolate(point, point+rely, rely))*amplitude

                frequency *= 2
                amplitude *= .7

            row.append(str(val) + " ")
        allrows.append(row)

    try:
        file = open("noise.txt","w+")
        for line in allrows:
            for num in line:
                file.write(str(num))
            file.write("\n")

    except:
        print("data couldn't be written in the file")
    

if __name__ == "__main__":
    main()