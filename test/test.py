#coding utf-8
class Test(object):

    def demo(self,a,b,c):
        d=a**2-4*b*c
        if d>0:
            print(d)


Test().demo(1,2,3)