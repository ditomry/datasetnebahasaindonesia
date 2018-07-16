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

A. Luthfi, B. Distiawan, and R. Manurung. Building an indonesian named entity recognizer using wikipedia and dbpedia. In Asian Language Processing (IALP), 2014 International Conference on, pages 19–22. IEEE, 2014.

I. Alfina, R. Manurung, and M. I. Fanany.  Dbpedia entities expansion in automatically building dataset for indonesian ner. In Advanced Computer Science and Information Systems (ICACSIS), 2016 International Conference on, pages 335–340. IEEE, 2016.

Ika Alfina, Septiviana Savitri, and Mohamad Ivan Fanany, "Modified DBpedia Entities Expansion for Tagging Automatically NER Dataset", in Proceeding of 9th International Conference on Advanced Computer Science and Information Systems 2017. ICACSIS 2017. (accepted).

https://www.researchgate.net/publication/320131070_Modified_DBpedia_Entities_Expansion_for_Tagging_Automatically_NER_Dataset 
https://github.com/ialfina/ner-dataset-modified-dee

Melakukan Ekspansi data DBpedia:

Program entities expansion yang dibuat mengimplementasikan metode DBpedia Entities Expansion Alfina et al. 2016, 2017 yang ditambahkan dan dimodifikasi aturannya pada ekspansi entitas place dan person.

- Parsing Data DBpedia:
  - Data DBpedia instance types yang di download pada link http://id.dbpedia.org/download/release/idwiki-20130508-instance-types.nt.gz di ekstrak lalu dijadikan satu folder dengan program "parsing_DBpedia.py". 
  - Lalu jalankan program untuk menghasilkan file "person.txt", "place.txt", dan "org.txt".

- Ekspansi DBpedia Person:
  - Pindahkan file "person.txt" dari hasil parsing DBpedia dan file "kbbi.txt" ke dalam satu folder dengan program "expansion_person.py". 
  - Lalu jalankan program untuk menghasilkan file di antaranya "person_expansi_final.txt" sebagai hasil ekspansi DBpedia person dan file "add_organization.txt" untuk menambahkan referensi NE DBpedia organization.
  
- Ekspansi DBpedia Organization:
  - Tambahkan isi file "add_organization.txt" dari hasil program ekspansi DBpedia person kedalam file "org.txt" hasil parsing DBpedia. 
  - Pindahkan file "org.txt" dan "kbbi.txt" ke dalam satu folder dengan program "expansion_org.py". 
  - Lalu jalankan program untuk menghasilkan file di antaranya "org_expansi_final.txt" sebagai hasil ekspansi DBpedia organization.

- Ekspansi DBpedia Place:
  - Pindahkan file "place.txt" dari hasil parsing DBpedia dan file "kbbi.txt" ke dalam satu folder dengan program "expansion_place.py". 
  - Lalu jalankan program untuk menghasilkan file di antaranya "place_expansi_final.txt" sebagai hasil ekspansi DBpedia place.

Melakukan Pelabelan Otomatis:

Program pelabelan otomatis mengimplementasikan metode pelabelan otomatis penelitian sebelumnya (Alfina et al. 2016, 2017 dan Luthfi et al. 2014) yang ditambahkan metode deteksi nama yang mengandung kata diawali huruf kecil, contohnya "Ali bin Abi Thalib" dapat di deteksi sebagai satu nama yang lengkap. Pada pelabelan otomatis sebelumnya yang terdeteksi hanya "Ali" dan "Abi Thalib", sedangkan "bin" dikecualikan.

- File hasil eskpansi DBpedia yaitu "person_expansi_final.txt", "org_expansi_final.txt", dan "place_expansi_final.txt" ditambahkan isi filenya masing-masing sesuai jenis entitas dengan isi file "gazetteers person.txt", "gazetteers org.txt", dan "gazetteers place.txt".
- Pindahkan file "person_expansi_final.txt", "org_expansi_final.txt", dan "place_expansi_final.txt" ke dalam satu folder dengan file "20k_wiki.txt" dan program "pelabelan_otomatis.py".
- Lalu jalankan program untuk menghasilkan file diantaranya "20k_wiki_gazz.txt" sebagai hasil pembangunan dataset NER Indonesia secara otomatis. File "20k_wiki_gazz.txt" sudah saya upload pada github ini sebagai contoh hasil dataset NER Indonesia, karena membutuhkan waktu berjam-jam untuk menghasil data ini.

Evaluasi Dataset NER Indonesia:

- Download program Stanford NER (https://nlp.stanford.edu/software/CRF-NER.shtml)
- Ekstrak file program yang nantinya akan menghasilkan folder program.
- Pindahkan file "20k_wiki_gazz.txt", "goldstandard-0811.txt", dan "20k_wiki_gazz.prop" pada folder program tersebut.
- Buka cmd lalu arahkan pada folder program.
- Jalankan "java -Xmx8000m -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop 20k_wiki_gazz.prop" untuk membuat model NER dengan Stanford NER. Nantinya akan menghasilkan file model NER "idner-model-20k_wiki_gazz.ser.gz". Contoh hasil model NER dapat di download pada link dropbox https://www.dropbox.com/s/s9yctsfepgaii2u/idner-model-20k_wiki_gazz.ser.gz?dl=0. Saya upload juga model NER hasilnya sebagai contoh, karena dengan komputer spesifikasi yang cukup besar: "CPU Xeon E3" dan "RAM 32 GB" membutuhkan waktu sekitar 1 jam untuk membangun model NERnya.  
- Terakhir jalankan "java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier idner-model-20k_wiki_gazz.ser.gz -outputFormat tabbedEntities -testFile goldstandard-0811.txt > idner-model-20k_wiki_gazz.tsv" untuk menghasilkan akurasi precision, recall, dan F1-score.
