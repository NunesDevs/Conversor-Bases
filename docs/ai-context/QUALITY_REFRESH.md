# Memória técnica — revisão de qualidade

Revisão: 2026-11-08. Este arquivo descreve o código validado nesta rodada; inventários automáticos anteriores registram estados históricos.

Conversão decimal por divisões sucessivas para bases 2, 4, 8, 16 e 20. Zero, negativos e tipos inválidos tratados. API convert_decimal pura; conversao compatível e main protegido. O CLI aceita nova tentativa e encerra por EOF/interrupção sem traceback. Quatro testes, incluindo subprocesso real e referência int, passaram em Python 3.12. Não há dependências ou deploy web. Publicação apropriada: pacote de scripts com licença MIT e checksum.

Validações: comandos de teste do README, execução local sem dados reais, git diff --check e revisão dos arquivos antes do commit. Push/integração/publicação têm autorização explícita do titular nesta sessão. Nenhuma migração, seed ou serviço de produção foi executado.
