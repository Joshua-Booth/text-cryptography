# text-cryptography

This program takes a text file and either encrypts or decrypt it with a chosen method to an output file.

## Getting Started

These instructions will get you a copy of this project up and running on your local machine for development and testing purposes.

### Prerequisites

What you will need:

```
Language: Python 3.6+

Package:        Version:
pip             18.0+
setuptools      40.1.0+
```

### Installing


##### Install

```
C:\text-encryption> python -m setup.py install
```

### Usage

##### Running the program

To run the program, run the following command where "your_text_file.txt" is a file in the directory from where the command is called, any encrypted/decrypted files will also be placed here.

```
C:\>python -m text_cryptography.__main__ [your_text_file.txt]
```


## Running the tests


To test this application run the [test.py](tests/tests.py) file as shown:

````
C:\>python -m unittest discover text_cryptography.tests
````

Note: Some of these tests require user input.

## Distribution

To distribute this package, locate the directory containing [setup.py](setup.py) and run the following command:

````
C:\>python setup.py sdist
````

Note: Use the format flag ( --format) to select tha different format.


## Built With

* [Python](http://www.dropwizard.io/1.0.2/docs/) - The programming language used



## Author

* [Joshua-Booth](https://github.com/Joshua-Booth)


## Lisence
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details