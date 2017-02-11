import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ofxclient-python',
    version='0.0.7',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Open Financial Data Exchange (OFX) client API and command-line interface',
    long_description=README,
    url='https://github.com/denvaar/ofxclient-python',
    author='Denver Smith',
    author_email='denverpsmith@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
