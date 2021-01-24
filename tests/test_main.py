import pytest
from src.main import BMI
import pandas as pd

@pytest.fixture
def create_bmi_object():
    data = [
                {"Gender":"Male","HeightCm":171,"WeightKg":96},
                {"Gender":"Male","HeightCm":161,"WeightKg":85},
                {"Gender":"Male","HeightCm":180,"WeightKg":77},
                {"Gender":"Female","HeightCm":166,"WeightKg":62},
                {"Gender":"Female","HeightCm":150,"WeightKg":70},
                {"Gender":"Female","HeightCm":167,"WeightKg":82},
            ]

    df = pd.DataFrame(data)
    bmi = BMI(df)
    return bmi

def check_new_columns(create_bmi_object):
    df = create_bmi_object.get_bmi_report()
    assert df.columns.tolist() == ['Gender', 'HeightCm', 'WeightKg', 'BMI(kg/m2)', 'BMI Category',
       'Health Risk']

def test_overweight_count(create_bmi_object):

    count = create_bmi_object.get_overweight_count()
    assert count == 0

def test_report(create_bmi_object):
    df = create_bmi_object.get_bmi_report()
    assert type(df) == pd.DataFrame

def test_bmi_calculation(create_bmi_object):
    df = create_bmi_object.bmi_calculator()
    assert type(df) == pd.DataFrame

