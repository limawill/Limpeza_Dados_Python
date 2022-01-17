import pandas as pd

filename = '/home/Universidades_do_Brasil.xlsx'
df = pd.read_excel(filename)

new_universidade = []
new_email = []
new_representante = []
new_procurador = []
new_dirigente = []

for row in df.itertuples():

    print(row.E_MAIL)

    if len(row.E_MAIL.split(';')) > 1:
        for index in row.E_MAIL.split(';'):
                new_universidade.append(row.UNIVERSIDADE)
                new_email.append(index)
                new_representante.append(row.REPRESENTANTE)
                new_procurador.append(row.PROCURADOR)
                new_dirigente.append(row.REITOR)
        else:
                new_universidade.append(row.UNIVERSIDADE)
                new_email.append(row.E_MAIL)
                new_representante.append(row.REPRESENTANTE)
                new_procurador.append(row.PROCURADOR)
                new_dirigente.append(row.REITOR)

    dffinal = pd.DataFrame({
        'Universidades': new_universidade,
        'E_mail': new_email,
        'Representante': new_representante,
        'Procurador': new_procurador,
        'Dirigente': new_dirigente,
    })




dffinal.to_excel('/home/Universidades_de_SP_EDITADA.xlsx')
