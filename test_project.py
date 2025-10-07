from project.project import rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10

def testing_rule1():
    assert rule1("steve") == True

def testing_rule2():
    assert rule2("steve9") == True

def testing_rule3():
    assert rule3("Steve9") == True

def testing_rule4():
    assert rule4("Steve9*") == True

def testing_rule5():
    assert rule5("Steve9*97") == True

def testing_rule6():
    assert rule6("Steve9*97March") == True

def testing_rule7():
    assert rule7("Steve9*97MarchV") == True

def testing_rule8():
    assert rule8("Steve9*97MarchV🌒") == True

def testing_rule9():
    assert rule9("Steve9*97MarchV🌒1400") == True

def testing_rule10():
    assert rule10("Steve9*97MarchV🌒1401level") == True


