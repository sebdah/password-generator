"""
Setup script for PyPi
"""

from distutils.core import setup
setup(name='password-generator',
    version='0.1.0',
    license='Apache License, Version 2.0',
    description='Simple password generator for Python',
    author='Sebastian Dahlgren',
    author_email='sebastian.dahlgren@gmail.com',
    url='http://sebdah.github.com/password-generator/',
    keywords="password generator",
    py_modules=['password_generator'],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
