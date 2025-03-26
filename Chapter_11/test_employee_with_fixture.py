from Employee import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee('Harsh','Tomar',50000)
    return employee

def test_give_default_raise(employee):
    # employee = Employee('Harsh','Tomar',50000)
    cpay = employee.annual_salary
    employee.give_raise()
    npay = employee.annual_salary
    assert npay-cpay == 5000

def test_give_custom_raise(employee):
    cpay = employee.annual_salary
    praise = 10000
    employee.give_raise(praise)
    npay = employee.annual_salary
    assert npay-cpay == praise