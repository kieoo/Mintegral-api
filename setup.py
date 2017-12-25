# -*- coding: utf-8 -*-
'''
@author: redstar
'''
from setuptools import find_packages, setup

setup( 
    name="Mintegral_API_Test",
    version="1.0",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
                        'behave>=1.2.5',
                        'PyMySql>=0.7.1',
                        'paramiko>=1.15.2',
                        'pycrypto>=2.6.1',
                        'PyHamcrest>=1.8.2',
                        'pymongo>=2.8',
                        'requests>=2.6.0',
                        'demjson>=2.2.3'
                        ]
 )
