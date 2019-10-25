# Deck of Cards

A module with Card and Deck classes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gdeck package

```bash
pip install .
```

## Usage
To use it in a console, type the following:
```python
from gdeck import *
```
And now you can use the Deck() and Card() class
## Test
To test the module, pytest was used. Below shows the tests done and their respective coverage.
```
gdeck_test.py::test_card PASSED                                                                                                                                                       [ 16%]
gdeck_test.py::test_deck_size PASSED                                                                                                                                                  [ 33%]
gdeck_test.py::test_deck_iter PASSED                                                                                                                                                  [ 50%]
gdeck_test.py::test_deck_slice PASSED                                                                                                                                                 [ 66%]
gdeck_test.py::test_deck_repr PASSED                                                                                                                                                  [ 83%]
gdeck_test.py::test_def_choice PASSED                                                                                                                                                 [100%]

----------- coverage: platform win32, python 3.7.0-final-0 -----------
Name                                                  Stmts   Miss  Cover
-------------------------------------------------------------------------
C:\Users\TEU_USER\Documents\gdeck\gdeck\__init__.py       1      0   100%
C:\Users\TEU_USER\Documents\gdeck\gdeck\gdeck.py         26      0   100%
-------------------------------------------------------------------------
TOTAL                                                    27      0   100%
```
## Author
Wilcarl D. Lopez

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT]