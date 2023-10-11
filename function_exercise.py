def area(shape_type,second,third):
    if shape_type=="rectangle"or'Rectangle':
        return 0.5*second*third
    elif shape_type=="triangle"or'Triangle':
        return second*third

shape=input("Enter the shape Triangle or Rectangle:\t")

if(shape=='rectangle'or shape=='Rectangle'):
    breadth=input('Enter the breadth of the rectangle:\t')
    length = input('Enter the length of the rectangle:\t')
    print(area(shape,int(breadth),int(length)))

elif(shape=='triangle' or shape=="Triangle"):
    height=input('Enter the height of the triangle:\t')
    base = input('Enter the base of the triangle:\t')
    print(area(shape,int(base),int(height)))

def star_formation(n):
    for i in range(n):
        s=''
        for j in range(i+1):
            s=s+'*'
        print(s)

n=int(input("enter the number of rows you want:"))
star_formation(n)
