# Task 2 Report — Calculadora de estimativa de preço

## Arquivos alterados

| Arquivo | Operação |
|---|---|
| `_config.yml` | Modificado — bloco `calculadora` adicionado |
| `_includes/price-calculator.html` | Criado |
| `index.html` | Modificado — seção `#estimativa` inserida entre `#como-funciona` e `#galeria` |
| `_includes/footer-scripts.html` | Modificado — IIFE da calculadora adicionado antes do bloco tema |
| `assets/css/style.scss` | Modificado — estilos `.calc*` e `.section-calc` adicionados no fim |

## Resultado do `node` (verificação da fórmula)

```
node -e 'var g=50,h=4,kg=129,pw=80,tar=0.80,des=2,marg=100,mont=20;...'
→ 37.41  ✓
```

## Resultado do build

```
bundle exec jekyll build
→ done in 0.111 seconds.  Sem erros.  ✓
```

## Resultado do grep

```
grep -o 'data-filamento-kg="129"' _site/index.html
→ data-filamento-kg="129"  ✓
```

## Hash do commit

`aab81ce` — feat: adiciona calculadora de estimativa de preço

## Self-review

- Seção `#estimativa` está ENTRE `</section>` de `#como-funciona` (linha 113) e `<section id="galeria"` (linha 126) em `index.html`. Confirmado.
- Include `whatsapp-link.html` reutilizado dentro de `price-calculator.html` exatamente como especificado. Confirmado.
- Apenas 5 arquivos foram staged e commitados; mudanças pendentes de galeria e docs não foram incluídas. Confirmado via `git add` seletivo.
- IIFE inserida antes do bloco de tema (`.theme-toggle`) no `footer-scripts.html`. Confirmado.

## Concerns

Nenhum. Todas as verificações passaram sem erros ou warnings.
