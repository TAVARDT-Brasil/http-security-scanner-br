# Scanner de Cabeçalhos de Segurança HTTP | TAVARDT Brasil

[![Escopo de Verificação Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/br/analise-cabecalhos-seguranca/)
[![Jurisdi%C3%A7%C3%A3o](https://img.shields.io/badge/Jurisdi%C3%A7%C3%A3o-Brasil-00C853.svg)](https://ag.tavardt.com/br/ciberseguranca/)

Auditoria automatizada de cabeçalhos de segurança HTTP alinhada com as diretrizes da ANPD e da LGPD para proteção perimetral de aplicações web no Brasil.

Desenvolvido e mantido pela divisão de cibersegurança e proteção de infraestruturas da **[TAVARDT Brasil](https://ag.tavardt.com/br/)**.

---

## 1. Escopo de Verificação Perimetral

Este utilitário de linha de comando avalia as diretrizes essenciais de proteção do navegador e cabeçalhos de resposta HTTP:

* **Strict-Transport-Security (HSTS):** Força comunicações encriptadas via HTTPS e impede ataques de downgrade e interceptação SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de arquivos derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados sensíveis contidos em URLs de referência contra vazamento para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmera, microfone e geolocalização).

---

## 2. Guia de Execução Rápida

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.com.br
```

---

## 3. Ferramentas Técnicas Online (Brasil)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [Verificador de Cabeçalhos de Segurança](https://tools.tavardt.com/br/analise-cabecalhos-seguranca/)
* [Validador de Consent Mode v2 e LGPD](https://tools.tavardt.com/br/validador-consent-mode-v2-lgpd/)
* [Verificador DMARC e Autenticação de E-mail](https://tools.tavardt.com/br/verificador-dmarc-email/)
* [Varredura de Arquivos Sensíveis Expostos](https://tools.tavardt.com/br/verificador-arquivos-expostos/)
* [Portal Completo de Ferramentas Técnicas](https://tools.tavardt.com/br/)

---

## 4. Consultoria e Remediação Técnica

Para remediação técnica especializada, testes de intrusão e consultoria em segurança da informação no Brasil, entre em contato com a equipe da **[TAVARDT Brasil](https://ag.tavardt.com/br/contato/)**.
