import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

package_data = {
    'text_cryptography/tests': ['*'],
    'text_cryptography/tests/data': ['*.txt']
}

setuptools.setup(name='text_cryptography',
                 version='1.0',
                 author="Joshua Booth",
                 author_email="me@joshuabooth.nz",
                 url="http://www.joshuabooth.nz/",
                 description="A text encryption/decryption program",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 packages=setuptools.find_packages(),
                 include_package_data=True)
