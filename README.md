This repository contains source code for the paper 'Unsupervised Context-Sensitive Spelling Correction for Clinical Free-Text with Word and Character N-Gram Embeddings', which will be presented at the [BioNLP Workshop at ACL 2017](http://www.aclweb.org/aclwiki/index.php?title=BioNLP_Workshop). The source code offered here contains a script to extract our manually annotated MIMIC-III data.

# License

MIT

# Requirements

* Python 2.7

To extract our manually annotated MIMIC-III test data, you should have access to the [MIMIC-III database](https://mimic.physionet.org).

# Extracting the annotated test data

To extract the annotated test data, git clone this repository and run

```python2.7 extract_test.py [path to NOTEEVENTS.csv file from the MIMIC-III database]```

from inside the directory. This script preprocesses the **NOTEEVENTS.csv** data and stores the preprocessed data in the file **mimic_preprocessed.txt**. It then extracts the annotated 
test data, which is stored to the file **testcorpus.json** in four lists: correct replacements, misspellings, misspelling contexts, and line indices.
