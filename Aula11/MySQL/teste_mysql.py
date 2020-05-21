# import da classe de conexão
from ConexaoBanco import BD


#iniciar um objeto 

bd = BD()

## inicia a conexão
bd.iniciaConexao()

# intrução SQL
SQL = """

SELECT * FROM pessoa;

"""
#executa a instrução
registros = bd.executaSQL(SQL)

for registro in registros:
    print('-----------------')
    print('ID:', registro['id_pessoa'])
    print('Nome:', registro['nome_pessoa'])
    print('Nacionalidade:', registro['nacionalidade_pessoa'])
    print('Idade:', registro['idade_pessoa'])

# fecha a conexão com o banco
bd.terminaConexao()

