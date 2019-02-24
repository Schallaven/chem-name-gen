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
import argparse

# Argument setup and parsing to a dictionary
parser = argparse.ArgumentParser(
			description = 'A Markov name generator with a chemistry dictionary '
						  'to generate names for new projects related to chemistry.',
				 epilog = 'A name for a new project is always one of the hardest parts.')

parser.add_argument('-v', '--version', help = 'prints version information', action='version', version='chem-name-gen 1.0 by Sven Kochmann')

parser.add_argument('-n', '--names', metavar = 'N', help = 'number of names to generate (default: 10)', type = int, default = 10)
parser.add_argument('-c', '--chain', metavar = 'N', help = 'chain length (default: 3)', type = int, default = 3)
parser.add_argument('-l', '--length', metavar = 'N', help = 'max length of generated name (default: 30)', type = int, default = 30)
parser.add_argument('-f', metavar = 'F', help = 'cut down the word list from the chemistry dictionary to F times of the word list'
												' of the FOLDOC dictionary; this will allow to over- or under-emphasize the'
												' chemistry part of the generated words (default: 1.0 = balanced)', type = float, default = 1.0)

parser.add_argument('--no_cut', help = 'do not cut down the word list from the chemistry', action = 'store_false', dest = 'cutdown') 
parser.add_argument('--remove_spaces', '-r', help = 'removes spaces from generated words', action = 'store_true')

args = vars(parser.parse_args())

# Chemistry dictionary file is from DOI: 10.1021/ed2002994;  converted
# to plain ascii file by the following command:
# iconv -c -f utf-16 -t ascii chemistry.dic > chemistry2.dic
# Also, all terms with 4 characters or less were removed by
# sed -r '/^.{,4}$/d' chemistry2.dic > chemistry_words.dic
chemistry_words = []
with open("chemistry_words.dic", "r") as f:
	chemistry_words = f.readlines()

random.shuffle(chemistry_words)

# FOLDOC dictionary from http://foldoc.org/source.html; converted
# to a plain list by the following commands:
# cat foldoc.dic | grep -Pv '^\t' | grep -v '^$' > foldoc2.dic
# Also, all terms with 4 characters or less were removed by
# sed -r '/^.{,4}$/d' foldoc2.dic > foldoc_words.dic
# Some lines at the beginning and the end were removed manually
foldoc_words = []
with open("foldoc_words.dic", "r") as f:
	foldoc_words = f.readlines()

random.shuffle(foldoc_words)

# There are way more  chemistry words than foldoc words.  Therefore,
# we shorten the chemistry_words list to the same length and combine
# both then.
if args['cutdown']:
	chemistry_words = chemistry_words[:int(len(foldoc_words)*args['f'])] 

chemistry_words = chemistry_words + foldoc_words
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
    def __init__(self, chainlen = 3):
        """
        Building the dictionary
        """
        if chainlen > 10 or chainlen < 1:
            print("Chain length must be between 1 and 10, inclusive")
            sys.exit(0)
    
        self.mcd = Mdict()
        self.chainlen = chainlen
    
        for l in chemistry_words:
            l = l.strip()
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")
    
    def New(self, wordslen = 30):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > (wordslen-1):
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()  

# Let's just print 10 generated names
for i in range(args['names']):
	word = MName(chainlen = args['chain']).New(wordslen = args['length'])

	if args['remove_spaces']:
		word = word.replace(' ', '') 

	print(word)


