# Import the grade calculation function from main program
from student import calculate_grade

# ---------------- GRADE S TEST CASES ----------------

# Test lower boundary for Grade S (exactly 90)
def test_grade_S_lower_boundary():
    assert calculate_grade(90) == "S"

# Test middle value for Grade S
def test_grade_S_middle_value():
    assert calculate_grade(95) == "S"

# Test upper boundary for Grade S (exactly 100)
def test_grade_S_upper_boundary():
    assert calculate_grade(100) == "S"

# ---------------- GRADE A TEST CASES ----------------

# Test lower boundary for Grade A (exactly 80)
def test_grade_A_lower_boundary():
    assert calculate_grade(80) == "A"

# Test middle value for Grade A
def test_grade_A_middle_value():
    assert calculate_grade(85) == "A"

# Test upper boundary just below 90
def test_grade_A_upper_boundary():
    assert calculate_grade(89.99) == "A"

# ---------------- GRADE B TEST CASES ----------------

# Test lower boundary for Grade B (exactly 65)
def test_grade_B_lower_boundary():
    assert calculate_grade(65) == "B"

# Test middle value for Grade B
def test_grade_B_middle_value():
    assert calculate_grade(72) == "B"

# Test upper boundary just below 80
def test_grade_B_upper_boundary():
    assert calculate_grade(79.99) == "B"

# ---------------- GRADE C TEST CASES ----------------

# Test lower boundary for Grade C (exactly 50)
def test_grade_C_lower_boundary():
    assert calculate_grade(50) == "C"

# Test middle value for Grade C
def test_grade_C_middle_value():
    assert calculate_grade(58) == "C"

# Test upper boundary just below 65
def test_grade_C_upper_boundary():
    assert calculate_grade(64.99) == "C"

# ---------------- GRADE D TEST CASES ----------------

# Test lower boundary for Grade D (exactly 40)
def test_grade_D_lower_boundary():
    assert calculate_grade(40) == "D"

# Test middle value for Grade D
def test_grade_D_middle_value():
    assert calculate_grade(45) == "D"

# Test upper boundary just below 50
def test_grade_D_upper_boundary():
    assert calculate_grade(49.99) == "D"

# ---------------- GRADE F TEST CASES ----------------

# Test value below 40 should return Grade F
def test_grade_F_below_40():
    assert calculate_grade(30) == "F"
# Import the grade calculation function from main program
from student import calculate_grade

# ---------------- GRADE S TEST CASES ----------------

# Test lower boundary for Grade S (exactly 90)
def test_grade_S_lower_boundary():
    assert calculate_grade(90) == "S"

# Test middle value for Grade S
def test_grade_S_middle_value():
    assert calculate_grade(95) == "S"

# Test upper boundary for Grade S (exactly 100)
def test_grade_S_upper_boundary():
    assert calculate_grade(100) == "S"

# ---------------- GRADE A TEST CASES ----------------

# Test lower boundary for Grade A (exactly 80)
def test_grade_A_lower_boundary():
    assert calculate_grade(80) == "A"

# Test middle value for Grade A
def test_grade_A_middle_value():
    assert calculate_grade(85) == "A"

# Test upper boundary just below 90
def test_grade_A_upper_boundary():
    assert calculate_grade(89.99) == "A"

# ---------------- GRADE B TEST CASES ----------------

# Test lower boundary for Grade B (exactly 65)
def test_grade_B_lower_boundary():
    assert calculate_grade(65) == "B"

# Test middle value for Grade B
def test_grade_B_middle_value():
    assert calculate_grade(72) == "B"

# Test upper boundary just below 80
def test_grade_B_upper_boundary():
    assert calculate_grade(79.99) == "B"

# ---------------- GRADE C TEST CASES ----------------

# Test lower boundary for Grade C (exactly 50)
def test_grade_C_lower_boundary():
    assert calculate_grade(50) == "C"

# Test middle value for Grade C
def test_grade_C_middle_value():
    assert calculate_grade(58) == "C"

# Test upper boundary just below 65
def test_grade_C_upper_boundary():
    assert calculate_grade(64.99) == "C"

# ---------------- GRADE D TEST CASES ----------------

# Test lower boundary for Grade D (exactly 40)
def test_grade_D_lower_boundary():
    assert calculate_grade(40) == "D"

# Test middle value for Grade D
def test_grade_D_middle_value():
    assert calculate_grade(45) == "D"

# Test upper boundary just below 50
def test_grade_D_upper_boundary():
    assert calculate_grade(49.99) == "D"

# ---------------- GRADE F TEST CASES ----------------

# Test value below 40 should return Grade F
def test_grade_F_below_40():
    assert calculate_grade(30) == "F"
