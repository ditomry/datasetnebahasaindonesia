ner-dataset-modified-dee
Dataset to be used in Building the Indonesian NER 
(Dataset untuk Membangun Named Entity Recognizer (NER) untuk Bahasa Indonesia) 

The dataset conforms with dataset format of Stanford-NER (https://nlp.stanford.edu/software/CRF-NER.shtml) 
Four classes are used:

PERSON for person names
PLACE for place names
ORG for organizaion names
Other
The dataset may be used for free, but if you want to publish paper/publication using the dataset, please cite this publication: 

Ika Alfina, Septiviana Savitri, and Mohamad Ivan Fanany, "Modified DBpedia Entities Expansion for Tagging Automatically NER Dataset", in Proceeding of 9th International Conference on Advanced Computer Science and Information Systems 2017. ICACSIS 2017. (accepted).

https://www.researchgate.net/publication/320131070_Modified_DBpedia_Entities_Expansion_for_Tagging_Automatically_NER_Dataset 

We provide three versions of NER dataset as we explained on the paper:

dataset created using original DEE (our previous project), file name: 20k-dee.txt, with properties file: 20k-dee.prop
dataset created using Modified DEE (our project), file name: 20k-mdee.txt, with properties file: 20k-mdee.prop
dataset created using Modified DEE plus gazettes (our project), file name: 20k-mdee-gazz.txt, with properties file: 20k-mdee-gazz.prop

Each version of dataset consist of 20,000 sentences from Wikipedia articles in the Indonesian language that were labeled automatically. 

How to create NER model using the dataset?

You can use many methods to create NER model. One of them is using Stanford NER library.
The steps to create NER model using Stanford NER library are as follows:

Download Stanford NER (https://nlp.stanford.edu/software/CRF-NER.shtml)

Download the dataset and its properties file (file with .prop extension)

Use Stanford NER classifier to create the model. 
For example: 
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop 20k-mdee.prop 

I recommend to increase heap size so you can train the dataset on computer with limited RAM. Add option like "-Xmx1024m" on the command, for example:

java -Xmx1024m -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop 20k-mdee.prop 

if this still doesn't work, increase the number. For example: "-Xmx8000m". This works for me :)

Let say this step will create a NER model file named "idner-model-20k-mdee.ser.gz"

Create or use a testing dataset. Lets say the file name is "testing.txt"

Evaluate the NER model using Stanford NER library 
For example:
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier idner-model-20k-mdee.ser.gz -testFile testing.txt

Good Luck :)
