import sys
import io
from student import calculate_grade, main


# 🔹 Test grade calculation logic
def test_grade_S():
    assert calculate_grade(95) == "S"

def test_grade_A():
    assert calculate_grade(85) == "A"

def test_grade_B():
    assert calculate_grade(70) == "B"

def test_grade_C():
    assert calculate_grade(55) == "C"

def test_grade_D():
    assert calculate_grade(45) == "D"

def test_grade_F():
    assert calculate_grade(30) == "F"


# 🔹 Test main program output using pytest capsys
def test_main_output(capsys, monkeypatch):
    test_args = [
        "student.py",
        "swapna",
        "ICA",
        "3",
        "85",
        "78",
        "90"
    ]

    # Mock command-line arguments
    monkeypatch.setattr(sys, "argv", test_args)

    # Run main program
    main()

    # Capture output
    captured = capsys.readouterr()
    output = captured.out

    # ✅ Assertions
    assert "GRADING CRITERIA" in output
    assert "STUDENT DETAILS" in output
    assert "Name       : swapna" in output
    assert "Department : ICA" in output
    assert "Semester   : 3" in output
    assert "Average    : 84.33" in output
    assert "Grade      : A" in output