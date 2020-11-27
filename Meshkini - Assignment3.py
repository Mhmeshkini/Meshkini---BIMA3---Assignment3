#getting information from user
print("This program is designed to get the polygon nods location and give you it's geometrical characteristics")
n=int (input("please enter the number of nodes"))
print ("now it is required to input the nodes coordination in a  order that the polygon should not be intersectig")
x=[]
y=[]
for i in range (n):
    print (f"please enter the X of {i+1}th node")
    x.append(float (input()))
    print (f"please enter the y of {i+1}th node")
    y.append(float (input()))
x.append(x[0])
y.append(y[0])

#calculating the geometrical characteristics
Ax, Sx, Sy, Ix, Iy, Ixy, Xt, Yt, Ixt, Iyt, Ixyt=0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0
for i in range (n):
    Ax=0.5*(x[i+1]+x[i])*(y[i+1]-y[i])+Ax
    Sx=(-1/6)*(x[i+1]-x[i])*(y[i+1]**2+y[i]*y[i+1]+y[i]**2)+Sx
    Sy=(1/6)*(y[i+1]-y[i])*(x[i+1]**2+x[i]*x[i+1]+x[i]**2)+Sy
    Ix=(-1/12)*(x[i+1]-x[i])*(y[i+1]**3+y[i+1]**2*y[i]+y[i+1]*y[i]**2+y[i]**3)+Ix
    Iy=(1/12)*(y[i+1]-y[i])*(x[i+1]**3+x[i+1]**2*x[i]+x[i+1]*x[i]**2+x[i]**3)+Iy
    Ixy=(-1/24)*(y[i+1]-y[i])*((y[i+1]*(3*x[i+1]**2+2*x[i+1]*x[i]+x[i]**2)+y[i]*(3*x[i]**2+2*x[i+1]*x[i]+x[i+1]**2)))+Ixy
Xt=Sy/Ax
Yt=Sx/Ax
Ixt=Ix-Yt**2*Ax
Iyt=Iy-Xt**2*Ax
Ixyt=Ixy+Xt*Yt*Ax

#printin data points
print(f"Point          X              y")
print ("--------------------------------")
for i in range(n):
    print (f"{i+1}            {x[i]}            {y[i]}")

#print Geometric Characteristics
print ("Geometric Characteristics:")
print (f"Ax     {Ax:10.2F}")
print (f"Sx     {Sx:10.2F}")
print (f"Sy     {Sy:10.2F}")
print (f"Ix     {Ix:10.2F}")
print (f"Iy     {Iy:10.2F}")
print (f"Ixy     {Ixy:10.2F}")
print (f"Xt     {Xt:10.2F}")
print (f"Yt     {Yt:10.2F}")
print (f"Ixt    {Ixt:10.2F}")
print (f"Iyt    {Iyt:10.2F}")
print (f"Ixyt   {Ixyt:10.2F}")