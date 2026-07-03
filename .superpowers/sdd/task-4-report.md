# Task 4 Report: JSON-LD para SEO

## Arquivos Criados/Modificados

1. **Criado:** `_includes/structured-data.html`
   - Contém dois blocos JSON-LD: ProfessionalService e FAQPage
   - Usa `jsonify` para escape seguro de strings
   - Condicional para FAQPage (verifica se `site.data.faq` existe e tem elementos)

2. **Modificado:** `_includes/head.html`
   - Adicionado `{% include structured-data.html %}` após `{% seo %}`
   - Linha 24 (agora na posição correta)

## Verificação do Build

```
bundle exec jekyll build 2>&1
Configuration file: /Users/daniel.wisky/Documents/Workspace/wisky-3dprint/_config.yml
            Source: /Users/daniel.wisky/Documents/Workspace/wisky-3dprint
       Destination: /Users/daniel.wisky/Documents/Workspace/wisky-3dprint/_site
                    done in 0.126 seconds.
```
**Status:** ✅ Build bem-sucedido, sem erros.

## Validação JSON-LD

### Grep Count
```bash
grep -c 'application/ld+json' _site/index.html
3
```
**Status:** ✅ 3 blocos encontrados (esperado: ≥2)

### Validação Python
```bash
python3 -c "import re,json; blocks=re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>', open('_site/index.html').read(), re.S); [json.loads(b) for b in blocks]; print('JSON-LD OK:', len(blocks), 'blocos')"
JSON-LD OK: 3 blocos
```
**Status:** ✅ Todos os 3 blocos são JSON válido e parseável.

## Blocos JSON-LD Gerados

1. **ProfessionalService:** Service schema com nome, descrição, URL, imagem, área servida (Brasil), tipo de serviço e links sociais
2. **FAQPage:** Schema com 6 questões/respostas importadas de `_data/faq.yml`
3. (O terceiro bloco é a inclusão adicional do jekyll-seo-tag do plugin)

## Commit

```bash
git add _includes/structured-data.html _includes/head.html
git -c commit.gpgsign=false commit -m "feat: adiciona JSON-LD (Service + FAQPage) para SEO"
```

**Hash do commit:** `2ceb3dd`

## Concerns

- Nenhum concern identificado. Todas as validações passaram.
