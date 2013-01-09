"""
Python module generating passwords


Copyright 2013 Sebastian Dahlgren

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from random import sample

ALPHNUM = (
    'abcdefghijklmnopqrstuvwxyz' + \
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
    '01234567890'
)

def generate(count=1, length=12, chars=ALPHNUM):
    """ Generate password

    Kwargs:
        count (int)::
            How many passwords should be returned?
        length (int)::
            How many characters should the password contain
        allowed_chars (str)::
            Characters

    Returns:
        String with the password. If count > 1 then the return value will be auto_now=
        list of strings.
    """
    if count == 1:
        return ''.join(sample(chars, length))
    
    passwords = []
    while count > 0:
        passwords.append(''.join(sample(chars, length)))
        count -= 1

    return passwords
