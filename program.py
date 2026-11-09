"""Decimal para bases 2, 4, 8, 16 e 20, sem efeitos ao importar."""
DIGITS = "0123456789ABCDEFGHIJ"
BASES = {2: "Binário", 4: "Quaternário", 8: "Octal", 16: "Hexadecimal", 20: "Vigesimal"}


def convert_decimal(value, base):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("O valor deve ser inteiro")
    if isinstance(base, bool) or not isinstance(base, int) or base not in BASES:
        raise ValueError("Base não suportada")
    if value == 0:
        return "0"
    sign = "-" if value < 0 else ""
    value = abs(value)
    digits = []
    while value:
        value, remainder = divmod(value, base)
        digits.append(DIGITS[remainder])
    return sign + "".join(reversed(digits))


def conversao(x, y, v):
    """Compatibilidade com o exemplo original; retorna também o resultado."""
    result = convert_decimal(x, v)
    y[:] = list(result)
    print(f"{BASES[v]}:\n{result}\n")
    return result


def main():
    while True:
        try:
            value = int(input("Valor inteiro para converter: "))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando...")
            return
        for base in BASES:
            conversao(value, [], base)
        try:
            again = input("Deseja continuar? [S/N]: ").strip().casefold()
        except (EOFError, KeyboardInterrupt):
            again = "n"
        if again != "s":
            print("Encerrando...")
            return


if __name__ == "__main__":
    main()
