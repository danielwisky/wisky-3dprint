# Melhorias no portal Wisky 3D Print — Design

**Data:** 2026-07-02
**Status:** Aprovado (aguardando revisão do spec escrito)

## Contexto

Site Jekyll estático (landing page única) de impressão 3D sob encomenda,
publicado em `3dprint.danielwisky.com.br` via GitHub Actions. Funil atual
depende 100% de DM no Instagram. Base técnica sólida: tema claro/escuro,
`IntersectionObserver` para animações `reveal`, lazy loading, modal de galeria
com teclado, "Carregar mais", `jekyll-seo-tag`, og-image gerada por script.

Objetivo: aumentar conversão e captação (WhatsApp, calculadora, FAQ, prova
social) e melhorar SEO/acessibilidade — sem introduzir framework novo,
seguindo os padrões existentes (includes Liquid, JS vanilla em
`footer-scripts.html`, tokens de CSS em `style.scss`, dados em `_data/`).

## Princípios

- **Data/config-driven:** valores de negócio ficam em `_config.yml` e `_data/`,
  editáveis sem tocar em código.
- **Progressive enhancement:** FAQ funciona sem JS (`<details>/<summary>`); a
  calculadora é a única peça que exige JS e degrada de forma limpa.
- **Zero conteúdo falso:** depoimentos só aparecem quando preenchidos.
- **Consistência visual:** reaproveita variáveis, gradiente, tema e animações
  já existentes.

## Nova ordem das seções

`hero → como funciona → estimativa (calculadora) → galeria → FAQ →
depoimentos (some enquanto vazio) → CTA`

---

## 1. WhatsApp como CTA principal

**Config (`_config.yml`):**
```yaml
whatsapp:
  number: "5511986349616"
  message: "Olá! Vim pelo site da Wisky 3D Print. Quero um orçamento — segue o link do modelo no MakerWorld: "
```

**Novo include `_includes/whatsapp-link.html`** — monta a URL
`https://wa.me/{{ number }}?text=<message URL-encoded>` usando o filtro
`url_encode` do Liquid. Aceita parâmetros opcionais (`class`, `label`) para
reuso.

**Pontos que passam a apontar para WhatsApp (primário):**
- Hero: botão primário (gradiente) vira "Pedir orçamento no WhatsApp";
  "Explorar MakerWorld" continua como botão secundário (ghost).
- Passo 3 do "Como funciona": título "Envie no Instagram" → "Envie no
  WhatsApp"; texto atualizado para enviar o link via WhatsApp.
- CTA final (`#contato`): botão vira WhatsApp.
- Navbar: `nav-cta` vira WhatsApp.

**Instagram permanece** como link secundário (portfólio) no menu da navbar, no
footer e no rótulo da galeria ("Ver todos em @wisky.3dprint").

**Ícone:** SVG do WhatsApp inline, mantendo o gradiente da marca.

## 2. Calculadora de estimativa

**Nova seção `#estimativa`** + include `_includes/price-calculator.html`.

**Entradas do cliente:** peso (g) e tempo de impressão (h) — `type="number"`,
`min`, `step`, `inputmode="decimal"`, labels associadas.

**Constantes escondidas (`_config.yml`):**
```yaml
calculadora:
  custo_filamento_kg: 129
  potencia_w: 80
  tarifa_kwh: 0.80
  desgaste: 2.00
  margem_pct: 100
  montagem: 20
```

**Fórmula (idêntica à da objeto3d, engenharia reversa do bundle deles):**
```
custo_filamento = (peso_g / 1000) * custo_filamento_kg
custo_energia   = (potencia_w * tempo_h / 1000) * tarifa_kwh
custo_desgaste  = desgaste                      # valor fixo, NÃO multiplica pelo tempo
subtotal        = custo_filamento + custo_energia + custo_desgaste
total           = subtotal * (1 + margem_pct/100) + montagem
```
Referência objeto3d desminificada:
`Ya=grams/1000*costKg; Qa=powerW*hours/1000*rate; un=wearFlat;
subtotal=Ya+Qa+labor+un; margin=subtotal*pct/100;
total=subtotal+margin+packaging+shipping`. Mão de obra, embalagem e frete = 0
no nosso caso; "montagem" ocupa a posição pós-margem (packaging).

**Caso de verificação:** peso 50 g, tempo 4 h →
`(6.45 + 0.256 + 2.00) * 2 + 20 = 37.412 → R$ 37,41`.

**JS:** função pura em `footer-scripts.html` que lê as constantes de
`data-*` attributes no formulário (renderizados pelo Liquid), calcula no
`input`/submit, formata em `pt-BR` (`R$ 37,41`). Sem dependências.

**UI:** exibe o valor + selo/disclaimer "Estimativa — o orçamento final é
confirmado no WhatsApp" + botão de WhatsApp genérico (sem passar os dados do
cálculo, conforme decidido). Trata entradas vazias/inválidas mostrando "—".

## 3. FAQ (acordeão acessível)

**`_data/faq.yml`** — lista de `{ pergunta, resposta }`. Include
`_includes/faq.html` renderiza com `<details>/<summary>` (acessível por
teclado, sem JS). Seção `#faq`.

Conteúdo inicial:
- **Preço:** como funciona + aponta para a calculadora (estimativa; final no
  WhatsApp).
- **Material:** PLA.
- **Prazo:** 3 a 7 dias após aprovação.
- **Entrega:** Correios, para todo o Brasil.
- **Tamanho:** sem limite fixo — avaliamos cada modelo (peças grandes podem ser
  feitas em partes).
- **Cores:** o cliente escolhe; cor/acabamento sob consulta.

## 4. JSON-LD (SEO)

**Novo include `_includes/structured-data.html`** no `<head>` (após `{% seo %}`):
- `Service` / `ProfessionalService`: nome, descrição, `areaServed: Brasil`,
  `provider` com URL e Instagram (`sameAs`), tipo de serviço "Impressão 3D sob
  encomenda".
- `FAQPage`: gerado a partir de `_data/faq.yml` (mesma fonte do item 3) →
  elegível a rich result no Google.

## 5. Depoimentos (estrutura pronta)

**`_data/depoimentos.yml`** com exemplo comentado (vazio por padrão). Include
`_includes/depoimentos.html` + seção que **só renderiza se
`site.data.depoimentos` tiver entradas**. Sem conteúdo inventado.

## 6. Alt único na galeria

- **`scripts/update-gallery.py`:** passa a capturar a legenda (caption) de cada
  post do feed e gravar o campo `caption:` em `_data/instagram_posts.yml`
  (truncada/limpa para uso como texto alternativo; sem quebrar posts sem
  legenda).
- **`_includes/instagram-post.html`:** usa `caption` como `alt` quando presente
  (fallback para o texto genérico atual). O modal (`gallery-modal`) exibe a
  legenda no título quando disponível.
- Retrocompatível: posts sem `caption` continuam funcionando.

## 7. Ajuste menor

- `_includes/instagram-feed.html`: `default: 8` → `default: 24` (alinha com
  `_config.yml`; puramente cosmético, sem efeito funcional).

---

## CSS (`assets/css/style.scss`)

Adicionar blocos reaproveitando variáveis/tokens existentes:
- botão WhatsApp (variante com ícone),
- calculadora (form, campos, card de resultado, selo de estimativa),
- FAQ (acordeão `details`/`summary` com marcador animado),
- depoimentos (grid de cards).

Manter tema claro/escuro e classes `reveal`/`reveal-stagger`.

## Arquivos afetados

| Arquivo | Ação |
|---|---|
| `_config.yml` | + blocos `whatsapp` e `calculadora` |
| `_includes/whatsapp-link.html` | **novo** |
| `_includes/price-calculator.html` | **novo** |
| `_includes/faq.html` | **novo** |
| `_includes/structured-data.html` | **novo** |
| `_includes/depoimentos.html` | **novo** |
| `_data/faq.yml` | **novo** |
| `_data/depoimentos.yml` | **novo** (exemplo comentado) |
| `index.html` | nova ordem de seções; CTAs → WhatsApp; passo 3; inclui calculadora, FAQ, depoimentos |
| `_includes/head.html` | inclui `structured-data.html` |
| `_includes/navbar.html` | `nav-cta` → WhatsApp; item de menu do FAQ |
| `_includes/footer.html` | link WhatsApp |
| `_includes/footer-scripts.html` | + JS da calculadora |
| `_includes/instagram-post.html` | `alt` a partir de `caption` |
| `_includes/gallery-modal.html` | título usa legenda quando houver |
| `_includes/instagram-feed.html` | default 8 → 24 |
| `scripts/update-gallery.py` | captura e grava `caption` |
| `assets/css/style.scss` | estilos das novas seções |

## Verificação

- `bundle exec jekyll build` compila sem erro.
- Calculadora: 50 g / 4 h → R$ 37,41; entradas vazias → "—".
- Links de WhatsApp abrem `wa.me` com a mensagem pré-preenchida (URL-encoded).
- FAQ abre/fecha por teclado; JSON-LD válido (estrutura `Service` + `FAQPage`).
- Galeria: posts com `caption` recebem `alt` único; posts sem `caption` usam o
  fallback.

## Fora de escopo (YAGNI)

- Integração calculadora → WhatsApp com dados preenchidos (decidido: só mostrar
  o preço).
- Analytics/pixel de conversão.
- Depoimentos reais (sem dados ainda).
- Preço por tamanho/cor (cliente escolhe; sem tabela fixa).
