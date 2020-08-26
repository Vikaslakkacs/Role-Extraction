#!/usr/bin/env python
# coding: utf-8

import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English


nlp= English()
ruler= EntityRuler(nlp)
nlp.add_pipe(ruler)

### load patterns from disk
ruler.from_disk('Entity Patterns')

## Load comments below and get the results.

doc= nlp(u"Request you to please add 'CS - Supervisor Refund Appr' and 'QOM Administrator' role for userid VILAKKA")
role_list=[]
for ent in doc.ents:
    if ent.label_=='Role':
        role_list.append(ent.ent_id_)
        print(ent.text +'-->'+ ent.label_+'-->'+ ent.ent_id_)
    


