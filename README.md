![Tests](https://github.com/Krishna-BR/BMICalculator/workflows/Tests/badge.svg) [![codecov](https://codecov.io/gh/Krishna-BR/BMICalculator/branch/main/graph/badge.svg)](https://codecov.io/gh/Krishna-BR/BMICalculator)

# python-bmi-calculator

## Quickstart
```
# Clone this repo and change directory
git clone git@github.com:Krishna-BR/BMICalculator.git
cd BMICalculator

# Create python environment (-B might be needed to execute)
make setup -B

# Run the suite of tests and checks
make check
```

Make a pull request to this repo to see the checks in action 😎 


## Running our checks

In it, we cover the following aspects of setting up a python project, including:

### Unit Tests

```python
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

def test_bmi_category(create_bmi_object):
    df = create_bmi_object.get_bmi_report()
    assert df['BMI Category'].unique().tolist() == ['Very severly obese', 'Severely obese']

def test_health_risk(create_bmi_object):
    df = create_bmi_object.get_bmi_report()
    assert df['Health Risk'].unique().tolist() == ['Very High Risk', 'High Risk']

def test_bmi():
    assert list(BMI.bmi_chart(10.29)) == ['Underweight', 'Malnutrition Risk']

def test_new_columns(create_bmi_object):
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
```

```shell
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.8.6, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /home/runner/work/BMICalculator/BMICalculator
plugins: cov-2.11.1
collected 7 items

tests/test_main.py .......                                               [100%]
============================== 7 passed in 0.57s ===============================
```

### Code Coverage
```
$ pytest --cov=src
============================= test session starts ==============================
----------- coverage: platform linux, python 3.8.6-final-0 -----------
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src/__init__.py       0      0   100%
src/main.py          37      6    84%   30-31, 33-34, 36-37
-----------------------------------------------
TOTAL                37      6    84%

Required test coverage of 80% reached. Total coverage: 83.78%

============================== 7 passed in 0.57s ===============================
```

### Linting
```
$ pylint src.data_prep.categorical --reports=y

Report
======
36 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |2      |NC         |NC         |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |1      |NC         |NC         |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|method   |5      |NC         |NC         |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+



External dependencies
---------------------
::

    pandas (src.main)



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |43     |40.57 |NC       |NC         |
+----------+-------+------+---------+-----------+
|docstring |36     |33.96 |NC       |NC         |
+----------+-------+------+---------+-----------+
|comment   |17     |16.04 |NC       |NC         |
+----------+-------+------+---------+-----------+
|empty     |10     |9.43  |NC       |NC         |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |NC       |NC         |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |NC       |NC         |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |0      |NC       |NC         |
+-----------+-------+---------+-----------+
|refactor   |0      |NC       |NC         |
+-----------+-------+---------+-----------+
|warning    |0      |NC       |NC         |
+-----------+-------+---------+-----------+
|error      |0      |NC       |NC         |
+-----------+-------+---------+-----------+




------------------------------------
Your code has been rated at 10.00/10

```

### Type Checking
```
$ mypy src
```

### Wrapping it in a Makefile
```
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*

clean: clean-pyc clean-test

test: clean
	. .venv/bin/activate && py.test tests --cov=src --cov-report=term-missing --cov-fail-under 80
```

### GitHub Actions with each `git push`
```
# .github/workflows/tests.yml
name: Tests
on: push
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v1
      with:
        python-version: 3.8
        architecture: x64
    - run: make setup
    - run: make check
    - run: bash <(curl -s https://codecov.io/bash)
```

