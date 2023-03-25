from math import pi

def ellipse_area():
    a = float(input("Zadej poloměr a:"))
    b = float(input("Zadej poloměr b:"))
    obsah = a * b * pi
    print("Obsah elipsy je", obsah)


def test_ellipse_area_circle_is_pi():
    assert ellipse_area(1,1) == pi

def test_ellipse_area_circle_is_0():
    assert ellipse_area(0,0) == 0

def test_ellipse_area_flat_is_0():
    assert ellipse_area(0,12345) == 0