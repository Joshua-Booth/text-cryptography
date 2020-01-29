import string
import logging
from operator import add, sub
from collections import defaultdict
from text_cryptography.log import debug_logger as logger


DEBUG = False
if DEBUG:
    logger.disabled = False
else:
    logging.disable(logging.CRITICAL)


class Cryptography:

    CHARS = string.ascii_letters + string.digits + string.punctuation + \
            " \n"

    def __init__(self, file=None, crypt_type=None, crypt_method=None,
                 key=None):
        self._file = file
        self._crypt_type = crypt_type
        self._crypt_method = crypt_method
        self._key = key
        self.crypt_methods = {"C": lambda: self.caesar_cipher(),
                              "M": lambda: self.monoalphabetic(),
                              "P": lambda: self.polyalphabetic()}

    def caesar_cipher(self):
        """
        Encrypts or decrypts the file using a caesar cipher.

        :return string: The encrypted/decrypted file data.
        """
        chars = list(self.CHARS * 2)
        data = ""
        crypt_operator = add if self.crypt_type == "encrypt" else sub

        for character in self.file_data:
            try:
                index = crypt_operator(chars.index(character), self.key)
                data += chars[index]
            except (ValueError, TypeError) as e:
                logger.error(e)
                print(f"Invalid character '{character}' in file {self.file}.")
        logger.info(f"data: {data}")
        return data

    def monoalphabetic(self):
        """
        Encrypts or decrypts the file using a monoalphabetic cipher.

        :return string: The encrypted/decrypted file data.
        """
        key = list(dict.fromkeys(self.key))
        cipher_text = list(self.CHARS)

        key = list(dict.fromkeys(key))
        for index, key_char in enumerate(key, 0):
            if key_char in self.CHARS:
                cipher_text.remove(key_char)
                cipher_text.insert(index, key_char)

        cipher = dict(zip(self.CHARS, cipher_text))
        logger.info(f"cipher: {cipher}")
        keys = cipher.keys()
        values = cipher.values()

        data = ""
        for character in self.file_data:
            try:
                if self.crypt_type == "encrypt":
                    data += list(keys)[list(values).index(character)]
                else:
                    data += list(values)[list(keys).index(character)]
            except (ValueError, TypeError) as e:
                logger.error(e)
                print(f"Invalid character '{character}' in file {self.file}.")
        logger.info(f"data: {data}")

        return data

    def polyalphabetic(self):
        """
        Encrypts or decrypts the file using a polyalphabetic cipher.

        :return string: The encrypted/decrypted file data.
        """
        sequence = []
        for key_char in self.key:
            for i, char in enumerate(self.CHARS, 0):
                if key_char == char:
                    sequence.append(i)

        map_data = []
        for data_char in range(0, len(self.file_data), 3):
            for char in sequence:
                map_data.append(char)

        pair_data = []
        for x in zip(self.file_data, map_data):
            pair_data.append(x)

        crypt_operator = add if self.crypt_type == "encrypt" else sub

        data = []
        chars = list(self.CHARS * 2)
        for pair in pair_data:
            try:
                char, shift = pair
                new_char_index = crypt_operator(self.CHARS.index(char), shift)
                data.append(chars[new_char_index])
            except (ValueError, TypeError) as e:
                logger.error(e)
                print(f"Invalid character '{character}' in file {self.file}.")
        logger.info(f"data: {data}")

        return "".join(data)

    @property
    def file(self):
        """
        Gets the file for the encryption/decryption method.

        :return string/int: The file.
        """
        return self._file

    @file.setter
    def file(self, value=None):
        """
        Sets the file to the specified value if it is valid.

        :param string value: The value to set as the file.
        :return None:
        """
        if Check.file_exists(value):
            self._file = value
        else:
            print(f"File '{value}' does not exist")
            raise SystemExit

    @property
    def file_data(self):
        """
        Gets the contents of the data file.

        :return string: The file contents.
        """
        return self.read(self.file)

    @property
    def crypt_type(self):
        """
        Gets the cryptography type, either encryption or decryption.

        :return string: The encryption/decryption type.
        """
        return self._crypt_type

    @crypt_type.setter
    def crypt_type(self, value=None):
        """
        Sets the cryptography type to either 'encrypt' or 'decrypt'.

        :param string value: The value to set as the cryptography type.
        :return None:
        """
        crypt_type = value.upper()
        fail_message = "You must choose either encryption or decryption."
        is_in, crypt_type = Check.is_in(crypt_type, 'E', 'D',
                                        error_message=fail_message)
        if is_in:
            if crypt_type == "E":
                self._crypt_type = "encrypt"
            elif crypt_type == "D":
                self._crypt_type = "decrypt"
            else:
                logger.error(f"crypt_type was: {self._crypt_type}")
                raise ValueError(f"crypt_type was: {self._crypt_type}")
        else:
            raise SystemExit

    @property
    def crypt_method(self):
        """
        Get the method of cryptography.

        :return string: The method of cryptography.
        """
        return self._crypt_method

    @crypt_method.setter
    def crypt_method(self, value=None):
        """
        Set the method of cryptography.

        :param value: The value to set as the method of cryptography.
        :return None:
        """
        message = """
Please choose from the following encryption/decryption methods:
Caesar Cipher: 'C'
Monoalphetic Cipher: 'M'
Polyalphabetic Cipher: 'P'"""

        value = value.upper() if value is not None else value
        is_valid_method, crypt_method = Check.is_in(value, 'C', 'M', 'P',
                                                    error_message=message)
        if is_valid_method:
            self._crypt_method = crypt_method
        else:
            raise SystemExit

    @property
    def key(self):
        """
        Gets the key for the encryption/decryption method.

        :return string/int: The key.
        """
        return self._key

    @key.setter
    def key(self, value=None):
        """
        Sets the ket to the specified value if it is valid.

        :param string value: The value to assign to the key.
        :return None:
        """
        if self.crypt_method == 'C':
            key_type = "number"
        else:
            key_type = "string"

        input_message = f"Please enter a {key_type} as a " \
            f"{self.crypt_type}ion key\n>> "
        if value is None:
            key = input(input_message)
        else:
            key = value

        is_valid_key, key = Check.is_valid_key(key, self.crypt_method)
        if is_valid_key:
            self._key = key
        else:
            raise ValueError(f"Key{key} is invalid")

    @staticmethod
    def read(file):
        """
        Read the file and return its contents.

        :param string file: The file to read.
        :return string: The file contents.
        """
        with open(file, 'r') as file:
            return file.read()

    @staticmethod
    def write(file, text):
        """
        Write to the given file.

        :param string file: The file to write to.
        :param string text: The content to write to the file.
        :return None:
        """
        with open(file, 'w') as f:
            f.write(text)


class Check:

    @staticmethod
    def file_exists(file):
        """
        Check if the file exists by reading it.

        :param string file: The file to check.
        :return True | False: Does the file exist?
        """
        try:
            Cryptography.read(file)
            return True
        except (FileNotFoundError, FileExistsError):
            return False

    @staticmethod
    def is_integer(value):
        """
        Checks if the value is an integer.

        :param string value: The value you want to check.
        :returns True & value | False: Is the value an integer?
        """
        try:
            return True, int(value)
        except (ValueError, TypeError):
            return False

    @staticmethod
    def is_in(entered, *required, error_message=None):
        """
        Checks entered values are valid by looking in the required values for a
        match.

        :param string entered: The entered values.
        :param string required: The values to check against.
        :param string error_message: An optional fail message.
        :return True & entered | False: Is the entered value in the required
                values?
        """
        try:
            while (str(entered).upper() not in required and
                   str(entered).lower() not in required):
                logger.info(f"entered: {entered} required: {required}")
                if error_message:
                    print(error_message)
                print("Please enter from the following:\n" +
                      ", ".join(char for char in required))
                entered = input(">> ").upper()
        except (ValueError, NameError):
            return False
        return True, entered

    @staticmethod
    def is_valid_key(key, crypt_method):
        """
        Checks if the key is valid based on the cryptography method.

        :param string | integer key: The key to check.
        :param string crypt_method: The type of encryption/decryption.
        :return True & string (key) | False: Is the key valid?
        """
        logger.info(f"key: {key}, crypt_method: {crypt_method}")
        if crypt_method == 'C':
            while type(key) is not int or key not in range(0, 95):
                try:
                    key = Check.is_integer(key)[1]
                    if key not in range(0, 95):
                        raise ValueError
                except (TypeError, ValueError):
                    print("You must enter an integer between 1 and 95!")
                    key = input("Enter an encryption key\n>> ")
        elif crypt_method in ('M', 'P'):
            pass
        else:
            return False
        return True, key


def main():
    """ Beginning of the program. """
    # file = None
    # for arg in sys.argv:
    #     if ".txt" in arg or ".py" not in arg or ".log" not in arg:
    #         file = arg

    file = input("Enter a file: ")

    file_data = Cryptography()
    file_data.file = file

    crypt_type = input("Please enter 'E' to encrypt or 'D' to decrypt\n>> ")
    file_data.crypt_type = crypt_type

    crypt_type = "encrypt" if crypt_type == 'E' else "decrypt"

    file_data.crypt_method = file_data.crypt_method

    key = input("Please enter a key for your data\n>> ")
    file_data.key = key

    print(f"crypt_method: {file_data.crypt_method}")
    new_data = file_data.crypt_methods[file_data.crypt_method]()

    crypt_methods = defaultdict(str,
                                {'C': "Caesar",
                                 'M': "Monoalphabetic",
                                 'P': "Polyalphabetic"})

    if DEBUG is False:
        crypt_method = crypt_methods[file_data.crypt_method]
        new_file_name = f"{crypt_method}_{crypt_type.capitalize()}ed.txt"
        logger.info(f"{type(new_data)}: {new_data}")
        Cryptography.write(new_file_name, new_data)
        print(f"Your new {crypt_type}ed file has been created as " +
              f"{new_file_name}.")


if __name__ == "__main__":
    main()
