import matplotlib.pyplot as plt
import math

while True:
    sigmax = float(input("enter sigma x: "))
    sigmay = float(input("enter sigma y: "))
    tauxy = float(input("enter tauxy: "))
    pt1 = (sigmax, abs(tauxy))
    pt2 = (sigmay, -abs(tauxy))
    center = (sigmax+sigmay)/2
    radxy = math.sqrt((center-sigmax)**2 + tauxy**2)
    sig1 = 0
    sig2 = center + radxy
    sig3 = center - radxy

    c12 = sig2/2
    r12 = abs(sig2)/2
    c13 = sig3/2
    r13 = abs(sig3)/2

    ele_angle = math.acos((pt1[0]-center)/radxy)
    ele_angle = math.degrees(ele_angle)/2

    print("sigma 1:", sig1, "sigma 2: ", sig2, "sigma 3: ", sig3)
    print("tau1: ", radxy, "tau2: ", r12, "tau3: ", r13)
    print(f"element angle: {ele_angle} deg")

    figure, axes = plt.subplots()
    draw_circle1 = plt.Circle((center, 0), radxy, fill=False, color = 'b')
    draw_circle2 = plt.Circle((c12, 0), r12, fill =False, color = 'k')
    draw_circle3 = plt.Circle((c13, 0), r13, fill = False, color = 'r')

    draw_line1 = plt.Line2D(xdata = [pt1[0], pt2[0]], ydata = [pt1[1], pt2[1]])

    plt.gcf().gca().add_artist(draw_circle1)
    plt.gcf().gca().add_artist(draw_circle2)
    plt.gcf().gca().add_artist(draw_circle3)
    plt.gcf().gca().add_artist(draw_line1)
    
    plt.title("RERrERE")
    plt.xlabel("plane stress")
    plt.ylabel("shear stress")

    axes.set_xlim(min(sig1, sig2, sig3), max(sig1, sig2, sig3))
    axes.set_ylim(-1*max(radxy, r12, r13, sig1/2, sig2/2, sig3/2), max(radxy, r12, r13, sig1/2, sig2/2, sig3/2))
    plt.grid()
    plt.gca().set_aspect('equal')
    plt.show()

