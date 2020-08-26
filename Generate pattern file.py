#!/usr/bin/env python
# coding: utf-8

# ### Importing Dependencies



import pandas as pd
import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English
##file to create and generate patterns with json file.
import createpattern 

##Initiating Spacy english version
nlp= English()
## Instantiating Entity ruler and adding to nlp via pipe
ruler= EntityRuler(nlp)
nlp.add_pipe(ruler)

##Create pattern class
pattern_class=createpattern.EntityPattern()

###Generate patterns in json file and save to disk
pattern_class.create_json('Role Names.csv', ruler, 'Entity Patterns')

