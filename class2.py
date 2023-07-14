class cylinder:
    pi=3.14
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
if __name__ =='__main__':
    c1=cylinder(2,20)
    c2=cylinder(20,50)
    print(f'Pi for c1:{c1.pi} and c2:1{c2.pi}')
    print(f'Radius for c1:{c1.radius} and c2:1{c2.radius}')
    print(f'Height for c1:{c1.height} and c2:1{c2.height}')
    print(f'Pi for  both c1 and c2 is:{cylinder.pi}')