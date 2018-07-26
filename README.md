## Geral

Implementação da opção [b)](http://dojopuzzles.com/problemas/exibe/caixa-eletronico/) do teste técnico da zenvia, implementado em python 3, com testes utilizando o framework unittest, nativo ao python 3.

Arquivos de implementação estão no diretório `src`, arquivos de teste estão no diretório `test`.

## Descrição do problema:

Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

* Entregar o menor número de notas;
* É possível sacar o valor solicitado com as notas disponíveis;
* Saldo do cliente infinito;
* Quantidade de notas infinito;
* Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:
* Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
* Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.

Para rodar os testes, rode `python run_tests.py` no diretório raiz.
