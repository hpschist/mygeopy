from mygeopy.triangle import hypot 

def test_hypot():
    assert hypot(3, 4) == 5
    print("Test 1:", hypot(3, 4) == 5)

    assert hypot(5, 12) == 13
    print("Test 2:", hypot(5, 12) == 13)

    assert hypot(8, 15) == 17
    print("Test 3:", hypot(8, 15) == 17)

    assert hypot(4, 3) == 5
    print("Test 4:", hypot(4, 3) == 5)

    assert hypot(0, 0) == 0
    print("Test 5:", hypot(0, 0) == 0)

    assert hypot(0, 5) == 5
    print("Test 6:", hypot(0, 5) == 5)

    assert hypot(7, 0) == 7
    print("Test 7:", hypot(7, 0) == 7)

    assert hypot(-3, 4) == 5
    print("Test 8:", hypot(-3, 4) == 5)

    assert hypot(3, -4) == 5
    print("Test 9:", hypot(3, -4) == 5)

    assert hypot(-3, -4) == 5
    print("Test 10:", hypot(-3, -4) == 5)