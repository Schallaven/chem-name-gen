---
title: 'Chem-name-gen: A Markov name generator for chemoinformatical projects'
tags:
  - Python
  - chemistry
  - chem-tech
  - Markov name generator
authors:
  - name: Sven Kochmann
    orcid: 0000-0001-7423-4609
    affiliation: 1
affiliations:
 - name: Department of Chemistry and Centre for Research on Biomolecular Interactions, York University, Toronto, Ontario M3J 1P3, Canada
   index: 1
date: 20 February 2019
bibliography: paper.bib
---

# Summary

Chemoinformatics became an important field during the last 50 years [@Willett2000,@Bajorath2015,@Gasteiger2016]. 
Chemists of all disciplines are adapting and developing chemoinformatical 
approaches and methods in their research. Methods are implemented in the form 
of programs, which eventually become published in respective repositories and 
journals such as Github [@github], Bitbucket [@bitbucket], Sourceforge [@sourceforge], 
Figshare [@figshare], Journal of Cheminformatics [@joc], Journal of Open Source Softare [@joss], 
and Journal of Open Research Software [@jors].

The first step of creating a program is still one of the hardest, i.e. finding
a program and/or project name. A project name - even just a preliminary one for 
internal use - is a mandatory requirement since all development environments and 
methods require one for organizing files and data. Furthermore, project names 
simplify housekeeping of project related matters internally (e.g. in meetings
and discussions)and externally (e.g. to funding organizations).

I personally used an element based system so far, e.g. for Beryllium, a program to 
create and managing safety data sheets [@Kochmann2014]. However, there is only a 
limited number of element names available. Moreover, an element name does not always 
fit a program and its purpose. There are other similar systems in use such as using first 
names for Linux Distributions (see e.g. Linux Mint [@linuxmint]); such systems have the same
limitations, though. 

Therefore, I developed ``chem-name-gen`` [@chemnamegen]. ``Chem-name-gen`` is a small and 
handy name generator for chemistry related programs. It is a Python-based command line tool 
using Markov chain generation [@Sinclair2012]. It uses modified versions of the chemistry 
dictionary published by Azman et al. [@Azman2012] as well as the free on-line dictionary 
of computing (FOLDOC) [@foldoc].

``Chem-name-gen`` was designed for inspiring chemical users with ideas for names for their projects
or just create a preliminary name for the initial developing phase(s). It is easy to use on any 
platform that supports Python: simply running it will provide 10 randomly generated names. Moreover, 
it can be configured through command line parameters that modify among others the length and number 
of the generate names, the chain lengths, and the weight of both dictionaries (chemistry and computing). 
Finally, it allows to generate names for given acronyms - chemists love acronyms! 

The program is released under the GNU General Public License 3 (GPLv3) and available at its Github 
repository [@chemnamegen]. The latest version has been archived to Zenodo [@chemnamegen-doi]. I hope 
that it is of use for the Chemistry community and can help to inspire the next generation(s) of 
chemoinformatical project names.



# References
