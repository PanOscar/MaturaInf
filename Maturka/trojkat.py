from turtle import *

color("blue","white")
lt(180)
for n in range(3):
    for i in range(5):
        begin_fill()
        for j in range(3):
            fd(50*(i+1))
            rt(120)
    fd(250)
    rt(120)
end_fill()
done()