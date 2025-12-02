# 🔍 Python Port Scanner

Um scanner de portas TCP simples e eficiente desenvolvido em **Python**. Esta ferramenta verifica a disponibilidade de portas comuns em um endereço IP alvo e identifica os serviços associados.

O projeto foi criado para fins educacionais, visando a prática de **Redes de Computadores** e manipulação de **Sockets** em baixo nível.

## ⚙️ Funcionalidades

- **Varredura Direcionada:** Foca nas portas mais críticas e comuns (Top Ports: 21, 22, 80, 443, etc.).
- **Identificação de Serviços:** Resolve o nome do serviço (ex: `http`, `ssh`, `ftp`) usando `socket.getservbyport`.
- **Clean Output:** Exibe apenas as portas que estão realmente abertas, evitando poluição visual no terminal.
- **Flexibilidade:** Aceita o IP alvo tanto via argumento de linha de comando quanto via input interativo.

---

## 🚀 Como Executar

Não é necessária nenhuma biblioteca externa, apenas o Python instalado.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
   ```
2. **Entre na pasta:**
   ```bash
   cd NOME-DO-REPO
   ```
3. **Execute o script:**
   ```bash
   python port_scanner.py
   # O programa pedirá o IP
   ```
   Via Argumento:
   ```bash
   python port_scanner.py 192.168.0.1
   ```

   ## 🛠️ Tecnologias Utilizadas
   - Python 3
   - Biblioteca <tt>socket</tt>: Para criação de conexões TCP e verificação de status.
   - Biblioteca <tt>sys</tt>: Para manipulação de argumentos de linha de comando.
  
   ## ⚠️ Aviso Legal (Disclaimer)
   Esta ferramenta foi desenvolvida estritamente para <tt>fins educacionais e de aprendizado</tt>. O uso de scanners de porta em redes de terceiros sem autorização prévia pode ser ilegal ou violar termos de          serviço. Utilize apenas em sua própria rede ou em ambientes onde você tenha permissão explícita para testes.

   <br>
   <div align="center"> Desenvolvido por <a href="https://github.com/bodnarguilherme">Guilherme Bodnar</a> </div>

