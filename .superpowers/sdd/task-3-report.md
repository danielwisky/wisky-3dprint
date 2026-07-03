# Task 3 — FAQ Acessível — Relatório

## Status
**DONE**

## Arquivos Alterados
1. `_data/faq.yml` — Criado (6 perguntas/respostas em YAML)
2. `_includes/faq.html` — Criado (template Liquid com `<details>/<summary>`)
3. `index.html` — Modificado (seção #faq inserida entre #galeria e #contato)
4. `_includes/navbar.html` — Modificado (item "Dúvidas" adicionado ao menu)
5. `assets/css/style.scss` — Modificado (estilo .faq-* adicionado no fim)

## Verificação Build
```
bundle exec jekyll build
# ✓ Incremental build: disabled. Enable with --incremental
# ✓ Generating... done in 0.176 seconds.
# ✓ Auto-regeneration: disabled. Use --watch to enable.
```
Resultado: **SEM ERRO**

## Verificação Grep
```
grep -c '<details class="faq-item">' _site/index.html
```
Resultado: **6** (esperado: 6) ✓

## Commit
```
git -c commit.gpgsign=false commit -m "feat: adiciona seção de FAQ"
```
Hash: **a9583be**
Ref: `feat/portal-improvements`

## Detalhes da Implementação

### Passo 1: `_data/faq.yml`
- 6 items (pergunta, resposta) conforme especificação
- Cobertura completa: preço, material, prazo, entrega, tamanho, cores

### Passo 2: `_includes/faq.html`
- Usa Liquid `for` para iterar sobre `site.data.faq`
- Elemento semântico `<details class="faq-item">`
- SVG chevron com `aria-hidden="true"` para acessibilidade
- Sem JavaScript — funcionalidade nativa do browser

### Passo 3: `index.html`
- Seção #faq inserida corretamente entre #galeria (line 142) e #contato (line 144)
- Classes aplicadas: `.section .section-faq .container`
- Header com `.section-header .section-header-center .reveal`
- Include `faq.html` renderizado

### Passo 4: `_includes/navbar.html`
- Menu item `<li><a href="#faq">Dúvidas</a></li>` adicionado
- Posicionado logo após `#galeria`, antes de `#contato` (linha 12-13)

### Passo 5: `assets/css/style.scss`
- 46 linhas adicionadas ao final do arquivo
- Classes: `.faq-list`, `.faq-item`, `.faq-item summary`, `.faq-chevron`, `.faq-answer`
- Usa tokens CSS existentes:
  - `--surface` (background)
  - `--border` (border color)
  - `--text` (text color)
  - `--muted` (secondary text)
  - `--cyan` (focus outline)
- Transição suave do chevron (rotate 180deg)
- Focus visible com outline 2px cyan
- Rem-based sizing (14px border-radius, 20px chevron, etc.)

## Concerns
**Nenhum**

- Build clean ✓
- Grep count correto ✓
- Sem dependências novas ✓
- Semântica HTML preservada ✓
- Acessibilidade (details/summary/aria-hidden) ✓
- Reutilização de classes existentes ✓
- Pt-BR correto ✓
