import unittest
import os
import logging

from text_cryptography.__main__ import Cryptography as crypt
from text_cryptography.__main__ import Check as chk
from text_cryptography.__main__ import DEBUG
from text_cryptography.tests.log import test_logger as logger

if DEBUG:
    logger.disabled = False
else:
    logging.disable(logging.CRITICAL)


class CryptographyTest(unittest.TestCase):

    def setUp(self):
        self.test_1 = crypt("test.txt", "encrypt", 'C')
        self.test_2 = crypt("test2.txt", "decrypt", 'C')

        self.test_3 = crypt("test3.txt", "encrypt", 'M')
        self.test_4 = crypt("test4.txt", "decrypt", 'M')

        self.test_5 = crypt("test5.txt", "encrypt", 'P')
        self.test_6 = crypt("test6.txt", "decrypt", 'P')

    def tearDown(self):
        for file in os.listdir(path='.'):
            if "test" not in file:
                os.remove(file)

    def test_caesar_cipher(self):
        logger.info("Testing 'caesar_cipher' method...")
        test1_text = "6=XtrjdYjCy;e7=XtrjdRtwjdYjCy;e8=JAjsdRtwjdYjCy="
        self.test_1.key = 5
        self.assertEqual(self.test_1.caesar_cipher(), test1_text)

        test2_text = """Top 10 Programming Languages 2017 (hackernoon.com)
1- Python - Python Software Foundation
2- C - Dennis Ritchie & Bell Labs
3- Java - Oracle Corporation
4- C++ - Bell Labs
5- C# - Microsoft
6- R - R Core Team
7- JavaScript - Netscape
8- PHP - Zend Technologies
9- Go - Google
10- Swift - Apple"""
        self.test_2.key = 43
        self.assertEqual(self.test_2.caesar_cipher(), test2_text)

        fail_text = ""
        self.test_2.key = 98
        self.assertNotEqual(self.test_2.caesar_cipher(), fail_text)

        fail_text = "6=XtrjdYjCy;e7=XtrjdRtwjdYjCy;e8=JAjsdRtwjdYjCy+"
        self.test_2.key = 36
        self.assertNotEqual(self.test_2.caesar_cipher(), fail_text)

    def test_monoalphabetic(self):
        logger.info("Testing 'monoalphabetic' method...")
        test3_text = """1.Sqob Tbxa,
2.Sqob Mqtb Tbxa,
3.Evbp Mqtb Tbxa."""
        self.test_3.key = "test"
        self.assertEqual(self.test_3.monoalphabetic(), test3_text)

        test4_text = """Top 10 Programming Languages 2017 (hackernoon.com)
1- Python - Python Software Foundation
2- C - Dennis Ritchie & Bell Labs
3- Java - Oracle Corporation
4- C++ - Bell Labs
5- C# - Microsoft
6- R - R Core Team
7- JavaScript - Netscape
8- PHP - Zend Technologies
9- Go - Google
10- Swift - Apple"""
        self.test_4.key = "long_keyword"
        self.assertEqual(self.test_4.monoalphabetic(), test4_text)

        fail_text = ""
        self.test_4.key = "fail"
        self.assertNotEqual(self.test_4.monoalphabetic(), fail_text)

        fail_text = "6=XtrjdYjCy;e7=XtrjdRtwjdYjCy;e8=JAjsdRtwjdYjCy+"
        self.test_4.key = "fail_2"
        self.assertNotEqual(self.test_4.monoalphabetic(), fail_text)

    def test_polyalphabetic(self):
        logger.info("Testing 'polyalphabetic' method...")
        test5_text = """+<!HFiq#xBL}s6~"Hqwr5sJxrXwQM:r- INxGc4HKiq#xBL """
        self.test_5.key = "test"
        self.assertEqual(self.test_5.polyalphabetic(), test5_text)

        test6_text = """Top 10 Programming Languages 2017 (hackernoon.com)
1- Python - Python Software Foundation
2- C - Dennis Ritchie & Bell Labs
3- Java - Oracle Corporation
4- C++ - Bell Labs
5- C# - Microsoft
6- R - R Core Team
7- JavaScript - Netscape
8- PHP - Zend Technologies
9- Go - Google
10- Swift - Apple"""
        self.test_6.key = "long_keyword"
        self.assertEqual(self.test_6.polyalphabetic(), test6_text)

        fail_text = ""
        self.test_6.key = "fail"
        self.assertNotEqual(self.test_6.polyalphabetic(), fail_text)

        fail_text = "6=XtrjdYjCy;e7=XtrjdRtwjdYjCy;e8=JAjsdRtwjdYjCy+"
        self.test_6.key = "fail_2"
        self.assertNotEqual(self.test_6.monoalphabetic(), fail_text)

    def test_file(self):
        with self.assertRaises(SystemExit):
            self.test_1.file = "test"
            self.test_1.file = "fail.txt"

        self.test_1.file = "test.txt"
        self.assertEqual(self.test_1.file, "test.txt")

        self.test_2.file = "test2.txt"
        self.assertEqual(self.test_2.file, "test2.txt")

    def test_crypt_type(self):
        self.test_1.crypt_type = 'x'
        self.assertEqual(self.test_1.crypt_type, "decrypt")

        self.test_1.crypt_type = 'd'
        self.assertEqual(self.test_1.crypt_type, "decrypt")

        self.test_1.crypt_type = 'e'
        self.assertEqual(self.test_1.crypt_type, "encrypt")

    def test_crypt_method(self):
        self.test_1.crypt_method = 'x'
        self.assertEqual(self.test_1.crypt_method, "C")

        self.test_1.crypt_method = 'm'
        self.assertEqual(self.test_1.crypt_method, "M")

        self.test_1.crypt_method = 'p'
        self.assertEqual(self.test_1.crypt_method, "P")

    def test_key(self):
        logger.info("Testing 'key' method...")
        self.test_1.key = "test"
        self.assertNotEqual(self.test_1.key, "test_key")

        self.test_1.crypt_method = 'm'
        self.test_1.key = "test"
        self.assertEqual(self.test_1.key, "test")

        self.test_1.key = "long_keyword"
        self.test_1.crypt_method = 'p'
        self.assertEqual(self.test_1.key, "long_keyword")

    def test_read(self):
        logger.info("Testing 'read' method...")
        test1_text = """1.Some Text,
2.Some More Text,
3.Even More Text."""

        self.assertIsNotNone(crypt.read("test.txt"))
        self.assertEqual(self.test_1.read("test.txt"), test1_text)
        self.assertRaises(FileNotFoundError, crypt.read, "fail.txt")
        self.assertRaises(FileNotFoundError, crypt.read, "fail2.txt")

    def test_write(self):
        logger.info("Testing 'write' method...")
        self.assertIsNone(crypt.write("write.txt", "test"))
        self.assertRaises(FileNotFoundError, crypt.write("fail.txt", "test"))
        self.assertRaises(FileExistsError, crypt.write("fail2.txt", "test"))


class CheckTest(unittest.TestCase):

    def test_file_exits(self):
        logger.info("Testing 'file_exists' method...")
        os.chdir(os.getcwd() + "\\data")
        self.assertTrue(chk.file_exists('test.txt'))
        self.assertFalse(chk.file_exists('test'))

        self.assertTrue(chk.file_exists('test2.txt'))
        self.assertFalse(chk.file_exists('Caesar_Encrypted.txt'))
        self.assertFalse(chk.file_exists('Monoalphabetic_Encrypted.txt'))
        self.assertFalse(chk.file_exists('Polyalphabetic_Encrypted.txt'))

    def test_is_integer(self):
        logger.info("Testing 'is_integer' method...")
        self.assertTrue(chk.is_integer('5'))
        self.assertTrue(chk.is_integer(9))
        self.assertFalse(chk.is_integer('test'))

    def test_is_in(self):
        logger.info("Testing 'is_in' method...")
        self.assertTrue(chk.is_in('c', 'C'))
        self.assertTrue(chk.is_in('t', "test", "value2")[0])
        self.assertTrue(chk.is_in('E', 'E')[0])

    def test_is_valid_key(self):
        logger.info("Testing 'is_valid_key' method...")
        self.assertFalse(chk.is_valid_key('c', 'X'))
        self.assertFalse(chk.is_valid_key('c', 6))
        self.assertTrue(chk.is_valid_key(5, 'C'))
        self.assertTrue(chk.is_valid_key(100, 'C'))
        self.assertFalse(chk.is_valid_key(100, 'F'))


if __name__ == "__main__":
    unittest.main(warnings="ignore")
