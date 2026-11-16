def leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def test_leap():
    assert leap(2024) == True
    assert leap(2023) == False
    assert leap(1900) == False
