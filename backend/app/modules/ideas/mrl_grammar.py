# Gramática MRL-Ideia: define regras e ações executáveis para ideias

MRL_GRAMMAR = r"""
<rule> ::= 'IDEIA' <id> ':' <condicoes> '->' <acoes>

<condicoes> ::= <condicao> (('E' | 'OU') <condicao>)*
<condicao>  ::= <campo> <operador> <valor>
              | '(' <condicoes> ')'
              | 'EXISTE' '(' <campo> ')'
              | 'NAO' <condicao>
              | <evento>

<operador>  ::= '=' | '!=' | '>' | '<' | '>=' | '<=' | 'CONTEM' | 'EM'

<evento>    ::= 'AO_CRIAR' | 'AO_VOTAR' | 'AO_MUDAR_ESTADO'

<acoes>     ::= <acao> (',' <acao>)*
<acao>      ::= 'SETAR' <campo> '=' <expressao>
              | 'CRIAR' <recurso> 'COM' <propriedades>
              | 'NOTIFICAR' <destinatario> 'MENSAGEM' <texto>
              | 'DISPACHAR' <destino> 'POR' <motivo>
              | 'EXECUTAR' <funcao> '(' <argumentos> ')'

<expressao> ::= <numero> | <campo> | <expressao> ('+' | '-' | '*' | '/') <expressao>
"""