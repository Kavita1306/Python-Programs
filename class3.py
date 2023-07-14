class cylinder:
    pi=3.14
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height

    def volume(self):
        return cylinder.pi *self.radius*2*self.height
    def description(cls):
        if __name__ =='__main__':
            c1=cylinder(4,2)

            print(f'Volume of Cylinder:{c1.volume()}')
            print(cylinder.description())
            print(c1.description())
