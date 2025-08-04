"""
Minicontratos Rule Language (MRL) - Gramática Avançada

<rule>           ::= "RULE" <id> [ ":" <tags> ] ":" <when_clause> "=>" <action_list> [ "#" <comment> ]
<tags>           ::= "[" <tag> { "," <tag> } "]"
<tag>            ::= IDENT

<when_clause>    ::= <event> [ "WHEN" <conditions> ]
<event>          ::= "ON" <entity> "." <trigger>
<entity>         ::= IDENT
<trigger>        ::= IDENT

<conditions>     ::= <condition> { ( "AND" | "OR" ) <condition> }
<condition>      ::= <operand> <operator> <operand>
                  | "(" <conditions> ")"
                  | "NOT" <condition>
                  | <function>
                  | <interval_condition>
                  | <collection_condition>

<operand>        ::= <field> | <value> | <function>
<field>          ::= IDENT { "." IDENT }
<operator>       ::= "==" | "!=" | ">=" | "<=" | ">" | "<" | "IN" | "NOT IN" | "CONTAINS" | "DURING" | "AFTER" | "BEFORE"
<value>          ::= NUMBER | STRING | DATE | BOOL | LIST

<function>       ::= <func_name> "(" <args> ")"
<func_name>      ::= "AVG" | "SUM" | "COUNT" | "MIN" | "MAX" | "EXISTS" | "UNIQUE" | "DATEDIFF" | "DATEADD" | "MATCHES" | "LAST" | "FIRST" | "RANDOM" | "ESCALATE"
<args>           ::= <operand> { "," <operand> }

<interval_condition> ::= <field> "DURING" <date_interval>
<date_interval>      ::= "BETWEEN" <value> "AND" <value>
<collection_condition> ::= <field> "CONTAINS" <value> | "HAS" <function>

<action_list>    ::= <action> { "," <action> }
<action>         ::= "SET" <field> "=" <expression>
                  | "CREATE" <entity> "WITH" <properties>
                  | "UPDATE" <field> "TO" <expression>
                  | "DISPATCH" <target> [ "WITH" <properties> ]
                  | "NOTIFY" <recipient> "MESSAGE" <string>
                  | "ACTIVATE" <trigger>
                  | "EXECUTE" <workflow>
                  | "ESCALATE" <entity> "TO" <role>
                  | "AUDIT" <entity> "FOR" <reason>
                  | "ROLLBACK" <entity> "TO" <snapshot>

<expression>     ::= <operand> { ( "+" | "-" | "*" | "/" | "%" ) <operand> }

<properties>     ::= <key_value> { "," <key_value> }
<key_value>      ::= <field> "=" <value>
<recipient>      ::= IDENT | <function>
<string>         ::= STRING
<workflow>       ::= IDENT
<role>           ::= STRING | ENUM

<comment>        ::= any text (ignored by parser)
"""