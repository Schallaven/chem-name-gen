# chem-name-gen

[![DOI](https://zenodo.org/badge/164249470.svg)](https://zenodo.org/badge/latestdoi/164249470)

A Markov name generator with a chemistry dictionary to generate names for new projects related to chemistry. A name for a new project is always one of the hardest parts.

Use it like

```bash
$ ./chem-name-gen
```

and it will provide you with 10 generated random names such as 

```bash
Phoeneace
Featuran conate
Network assocky automariazepan
Decket analdehydropylide
Tript pres portate
Bromoisopropylbenzoylol
Sydel
Back pointerene
Paraic andixyridiphene
Methylethylene
```

There are some command line parameters available now to tailor the output a little bit:
```bash
$ ./chem-name-gen -h
usage: chem-name-gen.py [-h] [-v] [-n N] [-c N] [-l N] [-f F] [-a AB]
                        [--no_cut] [--remove_spaces]

A Markov name generator with a chemistry dictionary to generate names for new
projects related to chemistry.

optional arguments:
  -h, --help           show this help message and exit
  -v, --version        prints version information
  -n N, --names N      number of names to generate (default: 10)
  -c N, --chain N      chain length (default: 3)
  -l N, --length N     max length of generated name (default: 30)
  -f F                 cut down the word list from the chemistry dictionary to
                       F times of the word list of the FOLDOC dictionary; this
                       will allow to over- or under-emphasize the chemistry
                       part of the generated words (default: 1.0 = balanced)
  -a AB, --acronym AB  generate names to fit the given acronym
  --no_cut             do not cut down the word list from the chemistry
  --remove_spaces, -r  removes spaces from generated words

A name for a new project is always one of the hardest parts.
```

Have fun!

