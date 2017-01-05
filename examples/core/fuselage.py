# -*- coding: utf-8 -*-
# @Author: p-chambers
# @Date:   2016-11-09 16:09:51
# @Last Modified by:   Paul Chambers
# @Last Modified time: 2016-11-10 11:05:15
from airconics import Fuselage


if __name__ == '__main__':
    # The defaults will yield a fuselage geometry similar to that of the
    # Boeing 787-8.
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()

    Fus = Fuselage(NoseLengthRatio=0.182,
                   TailLengthRatio=0.293,
                   Scaling=[55.902, 55.902, 55.902],
                   NoseCoordinates=[0., 0., 0],
                   CylindricalMidSection=False,
                   Maxi_attempt=5)

    # Create plane to check symmetry:

#    P = gp_Pln(gp_Pnt(0, 0, 0),
#                          gp_Dir(gp_Vec(0, 1, 0)))
#    Fsym = act.make_face(P, -10, 10, 0, 100)
#    display.DisplayShape(Fsym, update=True)

#    Display Fuselage:
    Fus.Display(display)

    for section in Fus._Lguides:
        display.DisplayShape(section, color='Black')
    for support in Fus._Csections:
        display.DisplayShape(support, color='Blue')

    for pt in [Fus.SternPoint, Fus.BowPoint]:
        display.DisplayShape(pt)

    print(Fus.SternPoint.X(), Fus.SternPoint.Y(), Fus.SternPoint.Z())

    start_display()