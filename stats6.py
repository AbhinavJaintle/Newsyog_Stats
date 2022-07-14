import time
import spacy
import spacy.cli
# from collections import Counter 
# import math
import json


while 1>0:
 try:
  


  sp_sm = spacy.load('en_core_web_sm')


  a = set()
  LNE = []

  

  def spacy_large_ner(document):
    for ent in sp_sm(document).ents:
      if (ent.label_ == "NORP" or ent.label_ == "FAC" or ent.label_ == "ORG" or ent.label_ == "LOC" or ent.label_ == "EVENT"):
       
          a.add(ent.text.strip())
          LNE.append(ent.text.strip())
          
          
      

  f = open('jaipur_news.txt', 'r')
  content = f.readlines()


  g = open('numbers.txt', 'r')
  file = g.readlines()
  g.close()

  for lines in file:
    count = int(lines)

  files = open('numbers.txt', 'a')
  files.truncate(0)
  print(count+1,file=files)
        

  files.close()
# file_object = open('my_output.txt', 'r')
# file = file_object.readlines()
# for element in file:
#     file_object.close()
#     file_object = open('my_output.txt', 'a')
#     mat = json.loads(element)
#     length = len(mat["No_of_Words"])
# file_object.close()
  i = 0

  for line in content:
    if i>=count:
        material = json.loads(line)['title']+json.loads(line)['article']
        spacy_large_ner(material)
        for element in LNE:
          Allene = element
        

    # if count>length and count<600:
        

        file_object = open('lne_output.txt', 'r')

        file = file_object.readlines()

    

        for element in file:

            file_object.close()

            file_object = open('lne_output.txt', 'a')

            material = json.loads(element)
            material_No_of_Words = material["LNE"].append(Allene)
            file_object.truncate(0)
            print(json.dumps(eval(str(material).strip())),file=file_object)
        

        

            file_object.close()



            a = set()
            LNE = []
        count+=1 
        files = open('numbers.txt', 'a')
        files.truncate(0)
        print(count,file=files)
        

        files.close()   
        i+=1
    else:
        i+=1
        
        
 except:
    pass
 else:
    break
time.sleep(2)