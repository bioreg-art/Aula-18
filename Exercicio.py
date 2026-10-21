import pandas as pd

df1 = pd.read_csv(r"C:\Users\regina.alvarenga\Downloads\funcionarios.csv")
df2 = pd.read_csv(r"C:\Users\regina.alvarenga\Downloads\funcionarios_v2.csv")

resultado_vertical = pd.concat([df1, df2])

print(resultado_vertical)

# Created by https://www.toptal.com/developers/gitignore/api/venv
# Edit at https://www.toptal.com/developers/gitignore?templates=venv

### venv ###
# Virtualenv
# http://iamzed.com/2009/05/07/a-primer-on-virtualenv/
.Python
[Bb]in
[Ii]nclude
[Ll]ib
[Ll]ib64
[Ll]ocal
[Ss]cripts
pyvenv.cfg
.venv
pip-selfcheck.json

# End of https://www.toptal.com/developers/gitignore/api/venv