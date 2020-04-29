import pickle
import bz2

my_string = """Per me si va ne la città dolente,
per me si va ne l'etterno dolore,
per me si va tra la perduta gente.
Giustizia mosse il mio alto fattore:
fecemi la divina podestate,
la somma sapienza e 'l primo amore;
dinanzi a me non fuor cose create
se non etterne, e io etterno duro.
Lasciate ogne speranza, voi ch'intrate."""

pickled = pickle.dumps(my_string)
compressed = bz2.compress(pickled)

print(len(my_string))
print(len(compressed))
