# Conversor-Bases

Conversor de números decimais positivos para as bases binária, quaternária, octal, hexadecimal e vigesimal.

## Funcionalidades verificadas

- Divisão inteira e restos.
- Conversão para cinco bases.
- Mapeamento de dígitos A até J.
- Menu para repetir conversões.

## Operação e arquitetura verificadas

Script único program.py; os dígitos são calculados por divisões sucessivas e impressos no console.

Arquivos principais: `program.py`.

### Requisitos e execução

Python 3; biblioteca padrão.

```text
python program.py
```



### Testes e estado

Não foi identificada uma suíte automatizada específica para os fluxos descritos; valide a execução e os casos de borda antes de publicar.

Estado: projeto de estudo/experimental. Deploy ativo não foi confirmado nesta revisão.

### Limitações conhecidas

- Zero e valores negativos não têm representação tratada.
- A condição v == 16 or 20 é sempre verdadeira; a validação de entradas deve ser revista.

### Licença e manutenção

Nenhum arquivo de licença foi identificado nesta revisão; não foi adicionada uma nova licença. Atualize comandos e limitações quando houver mudança de comportamento.
