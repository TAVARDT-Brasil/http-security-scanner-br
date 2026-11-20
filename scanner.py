#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Força comunicações encriptadas via HTTPS (HSTS).'), ('Content-Security-Policy', 'Restringe o carregamento de recursos contra ataques XSS.'), ('X-Frame-Options', 'Impede ataques de clickjacking bloqueando enquadramentos indevidos.'), ('X-Content-Type-Options', 'Bloqueia vulnerabilidades de MIME-sniffing no navegador.'), ('Referrer-Policy', 'Controla o vazamento de caminhos e dados sensíveis de referência.'), ('Permissions-Policy', 'Aplica o princípio do menor privilégio a APIs de hardware do navegador.')]

def scan_target(target_url):
    print(f"\n[TAVARDT Brasil] Iniciando auditoria perimetral de cabeçalhos de segurança para: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (pt-BR)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [CONFORME] {header_name}")
                    score += 1
                else:
                    print(f"  [AUSENTE] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT Brasil] Pontuação Final: {score}/{total}")
            print(f"\nVerificacao completa online: https://tools.tavardt.com/br/analise-cabecalhos-seguranca/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/br/ciberseguranca/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT Brasil] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
