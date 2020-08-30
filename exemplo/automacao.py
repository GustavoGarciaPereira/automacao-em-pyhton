import pandas

df = pandas.read_excel('dados_teste.xlsx')



texto_html = '''
    <div class="card" style="width: 18rem;">
        <img class="card-img-top" src="{}" alt="imagem do palestrante {}">
        <div class="card-body">
            <p class="card-text">O palestrante {} {} atualmente {}</p>
            <p>Um pouco mais sobre o que ele faz {}</p>
            <p>Dados fornecido para contato {}</p>
        </div>
    </div>
    <br>
    <br>
'''

print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
#
#df['nome']
#df['sobrenome']
#df['profissao']
#df['email']	
#df['decricao_funcao']
#df['imagem']

for i in range(len(df)):
    print(texto_html.format(df['imagem'][i],
                            df['nome'][i],
                            df['nome'][i],df['sobrenome'][i],
                            df['profissao'][i],
                            df['decricao_funcao'][i],
                            df['email'][i]
                            ))
    print("\n\n")