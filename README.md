Membangun Dataset NER Indonesia Secara Otomatis Dari Data Wikipedia dan DBpedia dengan Metode Entities Expansion pada DBpedia

Format dataset sesuai dengan Stanford-NER (https://nlp.stanford.edu/software/CRF-NER.shtml) 
Terdapat empat jenis entitas:
  - Person untuk nama orang
  - Place untuk nama tempat
  - Organisation untuk nama organisasi
  - O untuk other

Data yang Digunakan

- File "20k_wiki.txt" berisi token-token NE Wikipedia Indonesia yang dibuat Alfina et al. 2016 sebagai sumber korpus dataset NER.
- Untuk referensi pelabelan NE menggunakan data DBpedia instance types yang di download pada link http://id.dbpedia.org/download/release/idwiki-20130508-instance-types.nt.gz
- File "gazetteers person.txt" adalah data gazetteers entitas person terdiri dari 4.190 nama orang daftar KTP elektronik Kota Palangkaraya yang sudah dicetak sampai dengan 29 Maret 2017, https://dukcapil.palangkaraya.go.id/index.php/pages/category/4-dokumen
- File "gazetteers org.txt" dan "gazetteers place.txt" adalah data gazetteers entitas place dan organization mengambil data dari situs-situs web mengikuti Alfina et al. 2017
- File "goldstandard-0811.txt" adalah data gold standard untuk menguji dataset NER Indonesia yang dibuat oleh Luthfi et al. 2014

Ika Alfina, Septiviana Savitri, and Mohamad Ivan Fanany, "Modified DBpedia Entities Expansion for Tagging Automatically NER Dataset", in Proceeding of 9th International Conference on Advanced Computer Science and Information Systems 2017. ICACSIS 2017. (accepted).

https://www.researchgate.net/publication/320131070_Modified_DBpedia_Entities_Expansion_for_Tagging_Automatically_NER_Dataset 
https://github.com/ialfina/ner-dataset-modified-dee

Melakukan Ekspansi data DBpedia:

- Parsing Data DBpedia:
  - data DBpedia instance types yang di download pada link http://id.dbpedia.org/download/release/idwiki-20130508-instance-types.nt.gz
Untuk Entitas Person:

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
