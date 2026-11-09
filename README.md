# Conversor de bases

Converte um inteiro decimal para binário, quaternário, octal, hexadecimal e vigesimal. O algoritmo usa divisões sucessivas e o alfabeto `0–9, A–J`, sem dependências externas.

```sh
python program.py
python -m unittest discover -s tests -v
```

Aceita zero e inteiros negativos. Entradas não inteiras são rejeitadas com mensagem e nova tentativa. EOF e interrupção encerram o menu sem traceback. Importar o módulo não abre o menu.

```python
from program import convert_decimal
assert convert_decimal(19, 20) == "J"
assert convert_decimal(-19, 2) == "-10011"
assert convert_decimal(0, 16) == "0"
```

`convert_decimal` é uma função pura. A função histórica `conversao(x, y, v)` continua imprimindo o resultado, atualiza a lista recebida e também devolve o texto. As bases aceitas são 2, 4, 8, 16 e 20.

Quatro testes cobrem zero, sinal, todas as bases, retorno para decimal com inteiros grandes e entradas inválidas. O programa usa apenas a biblioteca padrão de Python 3; não há frontend, backend ou serviço de deploy web. Para distribuir, basta o código Python e a licença MIT em `LICENSE`.

Memória técnica: `docs/ai-context/QUALITY_REFRESH.md`.
