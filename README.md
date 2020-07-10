# EasyS7





EasyS7 is a python library for reading datablocks from Siemens S7 series PLCs . It depends on python-snap7 library so you should first install the library.

## Installition 

Before installing EasyS7 you should follow the steps that are described in [documentation](https://python-snap7.readthedocs.io/en/latest/). After that, you can install EasyS7 over package manager [pip](https://pypi.org/) with the folowing command 

```bash
$ pip install EasyS7
```

## Usage

To be able to use this library, you should have a layout of your db that you want to read. This layout is used to get data types and their ofsets to be able to operate related byte converting operations.  This layout can be obtained by copying the db from the TIA portal in to a txt file. You should copy the first 3 columns that contains the name, data type and ofset informations. 
An example layout is :
```
dummy1	Real	0
dummy2	Int	4
dummy3	Int	6
dummy4	Real	8
dummy5	Real	12
dummy6	Real	16
dummy7	Real	20
dummy8	Int	24
dummy9	Int	26
dummy10	Int	28
dummy11	Int	30
dummy12	Int	32
dummy13	Int	34
dummy14	Int	36
dummy15	Int	38
dummy16	String[32]	40
dummy17	Bool	74.0
dummy18	Bool	74.1
dummy19	Bool	74.2
dummy20	Bool	74.3
dummy21	Bool	74.4
dummy22	Bool	74.5
dummy23	Bool	74.6
dummy24	Bool	74.7
dummy25	Bool	75.0
dummy26	Real	76
dummy27	Bool	80.0
dummy28	Bool	80.1
dummy29	Bool	80.2
```
You can read the related data with this example code
```python
from EasyS7.PLC import PLC 
plc = PLC('192.168.1.100',0,1) #create a PLC object with ip, rack and slot
plc.connect() #create a connection
data = plc.readDb('path/to/file.txt',130) #read db with layout and db number
```

The output dictionary is like:
```python
{'dummy1': 0.8399999737739563, 'dummy2': 15, 'dummy3': 120, 'dummy4': 14.0, 'dummy5': 4.510000228881836, 'dummy6': 2.7216904163360596, 'dummy7': 0.19440646469593048, 'dummy8': 2, 'dummy9': 0, 'dummy10': 0, 'dummy11': 0, 'dummy12': 0, 'dummy13': 0, 'dummy14': 0, 'dummy15': 0, 'dummy16': 'Kompozit 3', 'dummy17': False, 'dummy18': False, 'dummy19': False, 'dummy20': False, 'dummy21': False, 'dummy22': False, 'dummy23': False, 'dummy24': False, 'dummy25': False, 'dummy26': 67.78571319580078, 'dummy27': False, 'dummy28': False, 'dummy29': True}
```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# License
[MIT](https://choosealicense.com/licenses/mit/)