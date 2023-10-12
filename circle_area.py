import math
def circle_calc(radius):
    area=round(math.pi*math.pow(radius,2),2)
    circumference=round(2*math.pi*radius)
    diameter=2*radius
    return circumference,area,diameter

def main():
    radius = input("enter the radius of the circle:\t")
    radius = int(radius)
    result= circle_calc(radius)
    print("\nThe cirumference is:"+ str(result[0])+"\n The area is:"+ str(result[1])+"\n The diameter is:"+ str(result[2]))
    print(type(result))
if __name__ == '__main__':
    main()