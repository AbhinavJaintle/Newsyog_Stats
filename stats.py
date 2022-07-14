
import spacy
import spacy.cli
from collections import Counter 
import matplotlib.pyplot as plt



sp_sm = spacy.load('en_core_web_sm')

Dict = {}
News = {}
News_x = []
News_y = []
Ne = []
Ne_x = []
Ne_y = []

a = set()

def spacy_large_ner(document):
  for ent in sp_sm(document).ents:
     a.add(ent.text.strip())

f = open('jaipur_news.txt', 'r')
content = f.readlines()
example_document = {}

count = 0
display = 0

for line in content:
 
  count += 1
  


  spacy_large_ner(line)

  Dict[count]=a

  # print("News #",count,": ")
  var = 0;
  for value in Dict[count]:
    var+=1
    
    for ent in sp_sm(value).ents:
      if(ent.label_=='GPE'):
        Ne.append('"{}"'.format(ent))
      
  #     print(value," -- ",ent.label_,)
  # print("Frequency -- ",var)
  News_x.append(count)
  News_y.append(var)
  News[count] = var
  # print("\n")
  a=set()
  if count > 101:
    break

NE = Counter(Ne)

for key, value in NE.items():
  if len(key)>5:
    
    Ne_x.append(key[0:7])

  else:
    Ne_x.append(key)
  
  Ne_y.append(value)

f.close()

left = []
i = 1
while i < len(Ne_x)+1:
  left.append(i)
  i+=1



print("News : ",News)
print("\n")

print("NPE : ",NE)
print("\n")

print("News_x : ",News_x)
print('\n')

print("News_y : ",News_y)
print('\n')

print("Ne_x : ",Ne_x)
print('\n')
print("Ne_y : ",Ne_y)
print('\n')


plot1 = plt.figure(1)
plt.plot(News_x, News_y)
  
plt.xlabel('News Label #')

plt.ylabel('No. of NEs')
  
plt.title('News')
  


  
  
plot1 = plt.figure(2)
plt.bar(left, Ne_y, tick_label = Ne_x,
        width = 0.8, color = ['red', 'green'])
plt.xticks(range(1,len(Ne_y)+1), Ne_x, rotation='vertical')
  
plt.xlabel('NE Name')

plt.ylabel('NE Frequency')

plt.title('NEs')

plt.xticks(fontsize=5)

plt.show()
