#!/usr/bin/env python3
# chem-name-gen
# Copyright (C) 2019 by Sven Kochmann

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the  Free Software Foundation,  either version 3  of the License, or
# (at your option) any later version.

# This program  is distributed  in the hope  that it will  be  useful,
# but  WITHOUT  ANY  WARRANTY;  without even  the implied warranty  of
# MERCHANTABILITY  or  FITNESS  FOR  A  PARTICULAR  PURPOSE.  See  the
# GNU General Public License for more details.

# You  should  have  received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# This  script  is  based  on  the  public-domain  Markov  chains name 
# generator for Mines of Elderlore that can be found at:
# http://www.roguebasin.com/index.php?title=Markov_chains_name_generator_in_Python

import random

# Chemistry dictionary file is from DOI: 10.1021/ed2002994;  converted
# to plain ascii file by the following command:
# iconv -c -f utf-16 -t ascii chemistry.dic > chemistry2.dic
# Also, all terms with 4 characters or less were removed by
# sed -r '/^.{,4}$/d' chemistry2.dic > chemistry3.dic
chemistry_words = []
with open("chemistry3.dic", "r") as f:
	chemistry_words = f.readlines()

random.shuffle(chemistry_words)

# Dictionary class
class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)  

# Markov name chain generator
class MName:
    """
    A name from a Markov chain
    """
    def __init__(self, chainlen = 2):
        """
        Building the dictionary
        """
        if chainlen > 10 or chainlen < 1:
            print("Chain length must be between 1 and 10, inclusive")
            sys.exit(0)
    
        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen
    
        for l in chemistry_words:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")
    
    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()  

# Let's just print 10 generated names
for i in range(10):
    print(MName().New())
