Web VPython 3.2


r = 2
t = 0

m1x = 1
m1y = 2
m1z = 0

m2x = 7
m2y = 2
m2z = 0

d = 0

center = vector(4, 2, 1)

mass1 = sphere(pos=center + vector(m1x, m1y, m1z), radius=r)
mass2 = sphere(pos=center + vector(m2x, m2y, m2z), radius=r)

rod = cylinder(pos=mass1.pos, axis=mass2.pos - mass1.pos, radius=0.5)

trajectory_graph = graph(title='Trajectory', xtitle='X', ytitle='Y')
trajectory_curve = gcurve(color=color.red)

scene.center = center

scene.autoscale = False  # Disable autoscaling of the scene

while t < 1000:
    rate(20)
    d = d + 0.1308996939

    center_of_mass = (mass1.pos + mass2.pos) / 2.0

    relative_pos1 = mass1.pos - center_of_mass
    relative_pos2 = mass2.pos - center_of_mass

    centrifugal_force1 = cross(vector(0, 0, -1), relative_pos1)
    centrifugal_force2 = cross(vector(0, 0, -1), relative_pos2)

    mass1.pos = center_of_mass + vector(cos(d) * r + m1x, m1y, sin(d) * r + m1z) + centrifugal_force1
    mass2.pos = center_of_mass + vector(cos(d) * r + m2x, m2y, sin(d) * r + m2z) + centrifugal_force2

    # Update rod position and axis
    

    mass1.rotate(angle=0.01, axis=vector(1, 0, 0), origin=center)
    mass2.rotate(angle=0.01, axis=vector(1, 0, 0), origin=center)
    mass1.rotate(angle=0.01, axis=vector(0, 0, 1), origin=center)
    mass2.rotate(angle=0.01, axis=vector(0, 0, 1), origin=center)
    
    rod.axis = mass2.pos - mass1.pos
    rod.pos = mass1.pos

    trajectory_curve.plot(pos=(mass1.pos.x, mass1.pos.y))

    # Update camera position and orientation
    scene.camera.pos = center_of_mass + vector(0, -10, 5)  # Set camera position behind the center of mass
    scene.camera.axis = center_of_mass - scene.camera.pos  # Set camera orientation towards the center of mass

    t = t + 1