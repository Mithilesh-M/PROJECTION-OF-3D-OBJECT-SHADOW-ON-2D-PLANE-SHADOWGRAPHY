from graphics import *
Points=[]
New_points=[]
Light=[0,0,0]

def shadow_projection():
    r=-1/Light[2]
    for i in range(len(Points)):
        shadow_x = Points[i][0]/((r*Points[i][1])+1)
        shadow_y = Points[i][1]/((r*Points[i][1])+1)
        New_points.append([shadow_x,shadow_y,0])

def Matplot3D():
    from mpl_toolkits.mplot3d import Axes3D
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    import matplotlib.pyplot as plt
    from matplotlib import cm

    fig = plt.figure()
    ax1 = fig.gca(projection='3d')
    ax1.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)
    ax2 = fig.gca(projection='3d')
    ax2.plot_trisurf(x1, y1, z1, cmap=cm.jet, linewidth=0.2)
    ax3 = fig.gca(projection='3d')
    ax3.scatter(Light[0], Light[1], Light[2], c='r', marker='o')
    ax3.set_xlabel('X Label')
    ax3.set_ylabel('Y Label')
    ax3.set_zlabel('Z Label')
    ax3.view_init(elev=100, azim=-90)
    plt.show()
    return()



def Graphics2D():
    win1 = GraphWin("Window1", 1080, 1920)
    win2 = GraphWin("Window2", 1080, 1920)
    point_light=Point(Light[0],Light[1])
    point_light.draw(win1)
    for i in range(len(x)):
        line=Line(Point(x[i],y[i]),Point(Light[0],Light[1]))
        line.setOutline('Yellow')
        line.draw(win1)
    Point(Light[0], Light[1]).draw(win1)
    point_new = []
    point_old = []
    for i in range(len(x)):
        point_old.append(Point(x[i], y[i]))
    poly_old = Polygon(*point_old)
    poly_old.setFill('Red')
    poly_old.draw(win1)
    for i in range(len(x1)):
        point_new.append(Point(x1[i], y1[i]))
    poly_new = Polygon(*point_new)
    poly_new.setFill('Red')
    poly_new.draw(win2)
    win1.getMouse()
    win2.getMouse()
    win1.close()
    win2.close()


print("Enter the light position")
Light[0]=int(input("Enter the X"))
Light[1]=int(input("Enter the Y"))
Light[2]=int(input("Enter the Z"))
n=int(input("Enter the no.of points"))
for i in range(n):
    x=int(input("Enter the X"))
    y=int(input("Enter the Y"))
    z=int(input("Enter the Z"))
    Points.append([x,y,z])
shadow_projection()
x = []
y = []
z = []
x1 = []
y1 = []
z1 = []
for i in range(len(Points)):
    x.append(Points[i][0])
    y.append(Points[i][1])
    z.append(Points[i][2])
for i in range(len(New_points)):
    x1.append(New_points[i][0])
    y1.append(New_points[i][1])
    z1.append(New_points[i][2])
print(Points)
print(New_points)
Graphics2D()
Matplot3D()



