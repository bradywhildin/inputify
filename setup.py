from setuptools import setup, find_packages

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='inputify',
    version='0.0.0',
    description='Simple command line validation tool',
    long_description='inputify can check if given value meets specified requirements and repeatedly prompt for user input until it meets specified requirements',
    url='https://github.com/bradywhildin/inputify',
    author='Vivek Khimani <vivekkhimani07@gmail.com>, Brady Whildin <bradwhil@gmail.com>',
    license='MIT',
    classifiers=classifiers,
    keywords='validate, command line, prompt',
    packages=find_packages(),
    install_requires=['']
)