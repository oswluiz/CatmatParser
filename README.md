CatmatParser
============

A simple Catmat (SIASG) XML Parser

Installation:

```
git clone https://github.com/oswluiz/CatmatParser
cd CatmatParser
sudo python setup.py install
```

Usage:

> "Treinamento":

```python
from catmat.submitter import Submitter
s = Submitter()

# Getting by item code:
s.get_by_cod('000396636')

# Getting by item "radicals":
s.get_by_radical('lapis', 'preto')
```



> "Produção" (Under development):

```python
from catmat.submitter import Submitter
s = Submitter(ambiente='produção', cpf='1231231231', password='123')

# Getting by item code:
s.get_by_cod('000396636')

# Getting by item "radicals":
s.get_by_radical('lapis', 'preto')
```
