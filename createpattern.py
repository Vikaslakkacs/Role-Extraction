#!/usr/bin/env python
# coding: utf-8

# ### Importing Dependencies




import pandas as pd
import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English





##Initiating Spacy english version
nlp= English()
## Instantiating Entity ruler and adding to nlp via pipe
ruler= EntityRuler(nlp)
nlp.add_pipe(ruler)





##Creating Entity pattern
### To retrieve patterns from the text for NER
class EntityPattern():
    
    def dash_split(self,sentence):
        ##If pattern list has no value then split directly else loop the list and split each value
        if len(self.split_pattern_list) ==0:
            self.split_pattern_list=sentence.split('-')
        else:
            dash_list=[]
            for word in self.split_pattern_list:
                word_list= word.split('-')
                for split_word in word_list:
                    dash_list.append(split_word)
            
            self.split_pattern_list= dash_list
                
    
    def slash_split(self,sentence):

        if len(self.split_pattern_list) ==0:
            
            self.split_pattern_list=sentence.split('/')
        else:
            slash_list=[]
            for word in self.split_pattern_list:
                word_list= word.split('/')
                for split_word in word_list:
                    slash_list.append(split_word)
            
            self.split_pattern_list= slash_list
    
    def star_split(self,sentence):

        if len(self.split_pattern_list) ==0:
            
            self.split_pattern_list=sentence.split('*')
        else:
            star_list=[]
            for word in self.split_pattern_list:
                word_list= word.split('*')
                for split_word in word_list:
                    star_list.append(split_word)
            
            self.split_pattern_list= star_list
    
    def space_split(self,sentence):
        
        if len(self.split_pattern_list) ==0:
            
            self.split_pattern_list=sentence.split()
        else:
            space_list=[]
            for word in self.split_pattern_list:
                word_list= word.split(' ')
                for split_word in word_list:
                    space_list.append(split_word)
            
            self.split_pattern_list= space_list
    
    def pattern_creation(self,sentence):
        self.split_pattern_list=[]
        #print(sentence)
        #self.dash_split(sentence)
        #print(sentence)
        #print(self.split_pattern_list)
        self.slash_split(sentence)
        #print(sentence)
        #(self.split_pattern_list)
        self.star_split(sentence)
        #print(sentence)
        #print(self.split_pattern_list)
        self.space_split(sentence)
        #print(sentence)
        #print(self.split_pattern_list)
        
        
        patterns=[]
        
        for word in self.split_pattern_list:
            lower_case= word.lower()
            
            ##Creating patterns
            word_dict={'LOWER':lower_case}
            punct_dict={'IS_PUNCT':True, 'OP':'*'}
            
            patterns.append(word_dict)
            patterns.append(punct_dict)
        
        ##Removing last punctuation dict
        patterns= patterns[:-1]
        
        entity_rule=[{'label':'Role', 'pattern':patterns, 'id':sentence}]
        
        return entity_rule
    
    def create_json(self, path_name, ent_ruler, dest_path):
        ###Creating Dataframe 
        role_names= pd.read_csv(path_name, encoding='latin1')
        ##Converting Dataframe to list
        pattern_text= role_names['rolename'].to_list()
        for text in pattern_text:
            pattern= self.pattern_creation(text)
            ent_ruler.add_patterns(pattern)
        ###Save to disk
        
        ent_ruler.to_disk(dest_path)
        