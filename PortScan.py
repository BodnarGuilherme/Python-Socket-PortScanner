import socket
import sys

# Lista de portas comuns (Top ports)
common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389, 8080]

def scan_target(ip):
    print(f"\nIniciando varredura em: {ip}")
    print("-" * 30)
    
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Timeout
        
        # connect_ex retorna 0 se sucesso (porta aberta)
        result = s.connect_ex((ip, port))
        
        if result == 0:
            try:
                # Tenta descobrir o nome do serviço (ex: 80 -> http)
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"[+] Porta {port} \tABERTA ({service})")
        # Não imprimimos as fechadas para não poluir a tela (clean output)
        
        s.close()

if __name__ == "__main__":
    # Permite passar o IP via terminal ou pergunta pro usuário
    target_ip = input("Digite o IP alvo: ") if len(sys.argv) < 2 else sys.argv[1]
    scan_target(target_ip)