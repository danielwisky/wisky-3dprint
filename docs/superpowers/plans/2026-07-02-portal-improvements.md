# Melhorias no Portal Wisky 3D Print — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Adicionar WhatsApp como CTA principal, calculadora de estimativa de preço, FAQ, JSON-LD (SEO), estrutura de depoimentos e `alt` único na galeria ao portal Jekyll da Wisky 3D Print.

**Architecture:** Site estático Jekyll. Tudo data/config-driven: valores de negócio em `_config.yml` e `_data/`. Novos includes Liquid, JS vanilla no `footer-scripts.html`, estilos aditivos no `style.scss` reaproveitando os tokens existentes. FAQ funciona sem JS; a calculadora é a única peça que exige JS.

**Tech Stack:** Jekyll (Liquid, kramdown), SCSS (`sass: compressed`), JavaScript vanilla, Python 3 (script de galeria), plugins `jekyll-seo-tag` + `jekyll-sitemap`.

## Global Constraints

- Idioma da interface: **pt-BR**. Moeda formatada como `R$ 37,41` (`Intl.NumberFormat('pt-BR')`).
- **Sem frameworks ou dependências novas** (nem CSS nem JS).
- Reusar tokens de CSS existentes: `--surface`, `--surface-soft`, `--border`, `--border-strong`, `--text`, `--muted`, `--gradient`, `--cyan`, `--on-accent`, `--shadow-soft`. Suportar tema claro E escuro (os tokens já trocam via `[data-theme]`).
- Reusar classes existentes: `.container`, `.section`, `.section-header`, `.section-header-center`, `.section-tag`, `.btn`, `.btn-gradient`, `.btn-ghost`, `.reveal`, `.reveal-stagger`.
- Todo link externo usa `target="_blank" rel="noopener noreferrer"`.
- Constantes da calculadora (todas em `_config.yml`, editáveis): filamento R$129/kg, potência 80 W, tarifa R$0,80/kWh, desgaste R$2,00 (fixo), margem 100%, montagem R$20.
- Número WhatsApp: `5511986349616`.
- Verificação padrão de cada task: `bundle exec jekyll build` deve completar sem erro (gera `_site/`).

---

## Task 1: WhatsApp como CTA principal

**Files:**
- Modify: `_config.yml` (adicionar bloco `whatsapp`)
- Create: `_includes/whatsapp-link.html`
- Modify: `index.html` (hero, passo 3, CTA final)
- Modify: `_includes/navbar.html` (nav-cta)
- Modify: `_includes/footer.html` (link WhatsApp)

**Interfaces:**
- Produces: include `whatsapp-link.html` que aceita `class` (default `btn btn-gradient`), `label` (default `Pedir orçamento no WhatsApp`) e `message` (default `site.whatsapp.message`). Renderiza um `<a>` para `https://wa.me/<number>?text=<message url_encode>` com ícone SVG do WhatsApp.

- [ ] **Step 1: Adicionar config do WhatsApp**

Em `_config.yml`, após o bloco `instagram:` (linha ~13), adicionar:

```yaml
whatsapp:
  number: "5511986349616"
  message: "Olá! Vim pelo site da Wisky 3D Print. Quero um orçamento — segue o link do modelo no MakerWorld: "
```

- [ ] **Step 2: Criar o include `_includes/whatsapp-link.html`**

```liquid
{%- assign wa_message = include.message | default: site.whatsapp.message -%}
{%- assign wa_class = include.class | default: "btn btn-gradient" -%}
{%- assign wa_label = include.label | default: "Pedir orçamento no WhatsApp" -%}
<a class="{{ wa_class }}" href="https://wa.me/{{ site.whatsapp.number }}?text={{ wa_message | url_encode }}" target="_blank" rel="noopener noreferrer">
  <svg class="wa-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" width="18" height="18">
    <path d="M17.5 14.4c-.3-.15-1.77-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51l-.57-.01c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.22 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.77-.72 2.02-1.42.25-.7.25-1.3.17-1.42-.07-.13-.27-.2-.57-.35zM12 2a10 10 0 00-8.6 15.05L2 22l5.05-1.32A10 10 0 1012 2z"/>
  </svg>
  <span>{{ wa_label }}</span>
</a>
```

- [ ] **Step 3: Trocar o CTA primário do hero**

Em `index.html`, substituir o bloco `hero-actions` (linhas 25-32) por:

```liquid
    <div class="hero-actions">
      {% include whatsapp-link.html class="btn btn-gradient" label="Pedir orçamento no WhatsApp" %}
      <a class="btn btn-ghost" href="{{ site.makerworld_url }}" target="_blank" rel="noopener noreferrer">
        Explorar MakerWorld
      </a>
    </div>
```

- [ ] **Step 4: Atualizar o passo 3 ("Como funciona")**

Em `index.html`, no passo 3 (linhas 94-98), substituir `<h3>` e `<p>` por:

```liquid
          <span class="step-label">Passo 03</span>
          <h3>Envie no WhatsApp</h3>
          <p>Mande o link para o nosso <a href="https://wa.me/{{ site.whatsapp.number }}" target="_blank" rel="noopener noreferrer"><strong>WhatsApp</strong></a> informando cor, tamanho e quantidade.</p>
```

- [ ] **Step 5: Trocar o botão do CTA final**

Em `index.html`, substituir o `<a>` do CTA final (linhas 143-145) por:

```liquid
        {% include whatsapp-link.html class="btn btn-gradient btn-lg" label="Chamar no WhatsApp" %}
```

- [ ] **Step 6: Trocar o nav-cta**

Em `_includes/navbar.html`, substituir o `<li>` do `nav-cta` (linhas 25-29) por:

```liquid
      <li>
        {% include whatsapp-link.html class="nav-cta" label="WhatsApp" %}
      </li>
```

- [ ] **Step 7: Adicionar WhatsApp no footer**

Em `_includes/footer.html`, dentro de `footer-links` (após a linha do Instagram, linha 11), adicionar:

```liquid
        <a href="https://wa.me/{{ site.whatsapp.number }}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
```

- [ ] **Step 8: Build e verificação**

Run: `bundle exec jekyll build`
Expected: build completa sem erro.

Run: `grep -o 'wa.me/5511986349616[^"]*' _site/index.html | head -1`
Expected: uma URL contendo `?text=Ol%C3%A1` (mensagem URL-encoded).

- [ ] **Step 9: Commit**

```bash
git add _config.yml _includes/whatsapp-link.html index.html _includes/navbar.html _includes/footer.html
git commit -m "feat: adiciona WhatsApp como CTA principal"
```

---

## Task 2: Calculadora de estimativa de preço

**Files:**
- Modify: `_config.yml` (bloco `calculadora`)
- Create: `_includes/price-calculator.html`
- Modify: `index.html` (nova seção `#estimativa` entre "como funciona" e galeria)
- Modify: `_includes/footer-scripts.html` (JS da calculadora)
- Modify: `assets/css/style.scss` (estilos da calculadora)

**Interfaces:**
- Consumes: nada de tasks anteriores; usa `site.whatsapp` (Task 1) para o botão auxiliar.
- Produces: `<form id="price-calc">` com `data-filamento-kg`, `data-potencia-w`, `data-tarifa-kwh`, `data-desgaste`, `data-margem-pct`, `data-montagem`; inputs `#calc-peso` e `#calc-tempo`; saída `#calc-result`. Fórmula: `((peso/1000)*kg + (potenciaW*horas/1000)*tarifa + desgaste) * (1+margem/100) + montagem`.

- [ ] **Step 1: Adicionar config da calculadora**

Em `_config.yml`, adicionar o bloco:

```yaml
calculadora:
  custo_filamento_kg: 129
  potencia_w: 80
  tarifa_kwh: 0.80
  desgaste: 2.00
  margem_pct: 100
  montagem: 20
```

- [ ] **Step 2: Criar o include `_includes/price-calculator.html`**

```liquid
<form id="price-calc" class="calc reveal"
  data-filamento-kg="{{ site.calculadora.custo_filamento_kg }}"
  data-potencia-w="{{ site.calculadora.potencia_w }}"
  data-tarifa-kwh="{{ site.calculadora.tarifa_kwh }}"
  data-desgaste="{{ site.calculadora.desgaste }}"
  data-margem-pct="{{ site.calculadora.margem_pct }}"
  data-montagem="{{ site.calculadora.montagem }}">
  <div class="calc-fields">
    <div class="calc-field">
      <label for="calc-peso">Peso da peça (g)</label>
      <input type="number" id="calc-peso" name="peso" min="0" step="1" inputmode="decimal" placeholder="ex: 50">
    </div>
    <div class="calc-field">
      <label for="calc-tempo">Tempo de impressão (h)</label>
      <input type="number" id="calc-tempo" name="tempo" min="0" step="0.1" inputmode="decimal" placeholder="ex: 4">
    </div>
  </div>
  <div class="calc-result-box">
    <span class="calc-result-label">Estimativa</span>
    <output id="calc-result" class="calc-result" for="calc-peso calc-tempo">—</output>
  </div>
  <p class="calc-disclaimer">Valor apenas uma estimativa. O orçamento final é confirmado no WhatsApp, conforme o modelo escolhido.</p>
  {% include whatsapp-link.html class="btn btn-gradient" label="Pedir orçamento no WhatsApp" %}
</form>
```

- [ ] **Step 3: Adicionar a seção na index (entre "como funciona" e galeria)**

Em `index.html`, entre o fechamento da seção `#como-funciona` (linha 115, `</section>`) e a abertura de `#galeria` (linha 117), inserir:

```liquid
<section id="estimativa" class="section section-calc">
  <div class="container">
    <header class="section-header section-header-center reveal">
      <span class="section-tag">Estimativa</span>
      <h2>Calcule o preço aproximado</h2>
      <p>Informe o peso e o tempo de impressão do modelo para uma estimativa rápida.</p>
    </header>
    {% include price-calculator.html %}
  </div>
</section>
```

- [ ] **Step 4: Adicionar o JS da calculadora**

Em `_includes/footer-scripts.html`, antes da tag `</script>` final (linha 224), adicionar um novo IIFE:

```javascript
  (function () {
    var form = document.getElementById("price-calc");
    if (!form) return;

    var peso = document.getElementById("calc-peso");
    var tempo = document.getElementById("calc-tempo");
    var out = document.getElementById("calc-result");
    var d = form.dataset;
    var fmt = new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" });

    function calc() {
      var g = parseFloat(peso.value);
      var h = parseFloat(tempo.value);
      if (!isFinite(g) || !isFinite(h) || g <= 0 || h < 0) {
        out.textContent = "—";
        return;
      }
      var filamento = (g / 1000) * parseFloat(d.filamentoKg);
      var energia = (parseFloat(d.potenciaW) * h / 1000) * parseFloat(d.tarifaKwh);
      var desgaste = parseFloat(d.desgaste);
      var subtotal = filamento + energia + desgaste;
      var total = subtotal * (1 + parseFloat(d.margemPct) / 100) + parseFloat(d.montagem);
      out.textContent = fmt.format(total);
    }

    form.addEventListener("input", calc);
    form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });
  })();
```

- [ ] **Step 5: Verificar a fórmula numericamente (fora do Jekyll)**

Run:
```bash
node -e 'var g=50,h=4,kg=129,pw=80,tar=0.80,des=2,marg=100,mont=20;var f=(g/1000)*kg,e=(pw*h/1000)*tar,s=f+e+des,t=s*(1+marg/100)+mont;console.log(t.toFixed(2))'
```
Expected: `37.41`

- [ ] **Step 6: Adicionar estilos da calculadora**

Em `assets/css/style.scss`, no fim do arquivo, adicionar:

```scss
.section-calc { background: var(--section-tint); }

.calc {
  max-width: 640px;
  margin: 0 auto;
  padding: 2rem;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  box-shadow: 0 20px 40px -30px var(--shadow-soft);
}
.calc-fields {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
@media (max-width: 520px) {
  .calc-fields { grid-template-columns: 1fr; }
}
.calc-field { display: flex; flex-direction: column; gap: 0.4rem; }
.calc-field label { font-size: 0.85rem; color: var(--muted); font-weight: 600; }
.calc-field input {
  padding: 0.7rem 0.9rem;
  background: var(--surface-soft);
  border: 1px solid var(--border-strong);
  border-radius: 12px;
  color: var(--text);
  font: inherit;
}
.calc-field input:focus-visible {
  outline: none;
  border-color: var(--cyan);
}
.calc-result-box {
  margin-top: 1.5rem;
  padding: 1.25rem;
  text-align: center;
  background: var(--surface-soft);
  border-radius: 14px;
}
.calc-result-label {
  display: block;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
}
.calc-result {
  display: block;
  margin-top: 0.25rem;
  font-size: 2rem;
  font-weight: 800;
  background: var(--gradient);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
.calc-disclaimer {
  margin: 1rem 0 1.25rem;
  font-size: 0.8rem;
  color: var(--muted-soft);
  text-align: center;
}
.calc .btn { width: 100%; }
```

- [ ] **Step 7: Build e verificação**

Run: `bundle exec jekyll build`
Expected: build sem erro.

Run: `grep -o 'data-filamento-kg="129"' _site/index.html`
Expected: `data-filamento-kg="129"` (config chegou ao HTML).

- [ ] **Step 8: Commit**

```bash
git add _config.yml _includes/price-calculator.html index.html _includes/footer-scripts.html assets/css/style.scss
git commit -m "feat: adiciona calculadora de estimativa de preço"
```

---

## Task 3: FAQ acessível

**Files:**
- Create: `_data/faq.yml`
- Create: `_includes/faq.html`
- Modify: `index.html` (seção `#faq` após galeria)
- Modify: `_includes/navbar.html` (item de menu)
- Modify: `assets/css/style.scss` (estilos do acordeão)

**Interfaces:**
- Produces: `_data/faq.yml` como lista de `{ pergunta, resposta }` — consumido também pela Task 4 (JSON-LD FAQPage). Include `faq.html` renderiza `<details class="faq-item">`.

- [ ] **Step 1: Criar `_data/faq.yml`**

```yaml
- pergunta: "Quanto custa uma peça?"
  resposta: "O preço depende do peso e do tempo de impressão do modelo. Use a calculadora de estimativa aqui no site para ter uma ideia rápida — o valor final é confirmado no WhatsApp."
- pergunta: "Qual material vocês usam?"
  resposta: "Imprimimos em PLA, um plástico resistente e com bom acabamento, ideal para a maioria das peças decorativas e funcionais."
- pergunta: "Qual o prazo de entrega?"
  resposta: "Em média de 3 a 7 dias após a aprovação do orçamento, dependendo da fila e do tamanho da peça."
- pergunta: "Vocês entregam em todo o Brasil?"
  resposta: "Sim! Enviamos pelos Correios para todo o Brasil. O frete é combinado junto com o orçamento no WhatsApp."
- pergunta: "Tem tamanho máximo de peça?"
  resposta: "Não há um limite fixo — avaliamos cada modelo. Peças maiores podem ser impressas em partes e montadas."
- pergunta: "Quais cores estão disponíveis?"
  resposta: "Você escolhe a cor e o acabamento que quiser; verificamos a disponibilidade sob consulta no WhatsApp."
```

- [ ] **Step 2: Criar `_includes/faq.html`**

```liquid
<div class="faq-list reveal-stagger">
  {%- for item in site.data.faq -%}
  <details class="faq-item">
    <summary>
      <span>{{ item.pergunta }}</span>
      <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
        <path d="M6 9l6 6 6-6"/>
      </svg>
    </summary>
    <div class="faq-answer">{{ item.resposta | markdownify }}</div>
  </details>
  {%- endfor -%}
</div>
```

- [ ] **Step 3: Adicionar a seção FAQ na index (após galeria, antes do CTA)**

Em `index.html`, entre o fechamento de `#galeria` (linha 133, `</section>`) e a abertura de `#contato` (linha 135), inserir:

```liquid
<section id="faq" class="section section-faq">
  <div class="container">
    <header class="section-header section-header-center reveal">
      <span class="section-tag">Dúvidas</span>
      <h2>Perguntas frequentes</h2>
      <p>As respostas rápidas antes de você chamar no WhatsApp.</p>
    </header>
    {% include faq.html %}
  </div>
</section>
```

- [ ] **Step 4: Adicionar item de menu do FAQ na navbar**

Em `_includes/navbar.html`, após o `<li>` da Galeria (linha 12), adicionar:

```liquid
      <li><a href="#faq">Dúvidas</a></li>
```

- [ ] **Step 5: Adicionar estilos do acordeão**

Em `assets/css/style.scss`, no fim do arquivo, adicionar:

```scss
.faq-list {
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.faq-item {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
}
.faq-item summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1.1rem 1.3rem;
  cursor: pointer;
  font-weight: 600;
  color: var(--text);
  list-style: none;
}
.faq-item summary::-webkit-details-marker { display: none; }
.faq-item summary:focus-visible { outline: 2px solid var(--cyan); outline-offset: -2px; }
.faq-chevron {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  color: var(--muted);
  transition: transform 0.25s ease;
}
.faq-item[open] .faq-chevron { transform: rotate(180deg); }
.faq-answer {
  padding: 0 1.3rem 1.2rem;
  color: var(--muted);
  line-height: 1.6;
}
.faq-answer p { margin: 0; }
```

- [ ] **Step 6: Build e verificação**

Run: `bundle exec jekyll build`
Expected: build sem erro.

Run: `grep -c '<details class="faq-item">' _site/index.html`
Expected: `6`

- [ ] **Step 7: Commit**

```bash
git add _data/faq.yml _includes/faq.html index.html _includes/navbar.html assets/css/style.scss
git commit -m "feat: adiciona seção de FAQ"
```

---

## Task 4: JSON-LD (dados estruturados para SEO)

**Files:**
- Create: `_includes/structured-data.html`
- Modify: `_includes/head.html` (incluir o novo include)

**Interfaces:**
- Consumes: `_data/faq.yml` (Task 3) para o bloco `FAQPage`; `site.title`, `site.description`, `site.url`, `site.instagram.profile_url`.
- Produces: dois `<script type="application/ld+json">` no `<head>` (`ProfessionalService` + `FAQPage`).

- [ ] **Step 1: Criar `_includes/structured-data.html`**

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": {{ site.title | jsonify }},
  "description": {{ site.description | jsonify }},
  "url": {{ site.url | jsonify }},
  "image": {{ site.url | append: site.image | jsonify }},
  "areaServed": { "@type": "Country", "name": "Brasil" },
  "serviceType": "Impressão 3D sob encomenda",
  "sameAs": [ {{ site.instagram.profile_url | jsonify }} ]
}
</script>
{%- if site.data.faq and site.data.faq.size > 0 %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {%- for item in site.data.faq %}
    {
      "@type": "Question",
      "name": {{ item.pergunta | jsonify }},
      "acceptedAnswer": { "@type": "Answer", "text": {{ item.resposta | jsonify }} }
    }{% unless forloop.last %},{% endunless %}
    {%- endfor %}
  ]
}
</script>
{%- endif %}
```

- [ ] **Step 2: Incluir no head**

Em `_includes/head.html`, após a linha `{% seo %}` (linha 23), adicionar:

```liquid
  {% include structured-data.html %}
```

- [ ] **Step 3: Build e verificação**

Run: `bundle exec jekyll build`
Expected: build sem erro.

Run: `grep -c 'application/ld+json' _site/index.html`
Expected: número ≥ 2 (o `jekyll-seo-tag` já emite um; agora somam-se os dois novos).

Run (valida que o FAQPage é JSON parseável):
```bash
python3 -c "import re,json,sys; blocks=re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>', open('_site/index.html').read(), re.S); [json.loads(b) for b in blocks]; print('JSON-LD OK:', len(blocks), 'blocos')"
```
Expected: `JSON-LD OK: 3 blocos` (sem exceção de parsing).

- [ ] **Step 4: Commit**

```bash
git add _includes/structured-data.html _includes/head.html
git commit -m "feat: adiciona JSON-LD (Service + FAQPage) para SEO"
```

---

## Task 5: Estrutura de depoimentos

**Files:**
- Create: `_data/depoimentos.yml`
- Create: `_includes/depoimentos.html`
- Modify: `index.html` (seção condicional após FAQ)
- Modify: `assets/css/style.scss` (estilos dos cards)

**Interfaces:**
- Produces: `_data/depoimentos.yml` (lista de `{ nome, texto }`); seção `#depoimentos` que só renderiza se houver entradas.

- [ ] **Step 1: Criar `_data/depoimentos.yml` (vazio, com exemplo comentado)**

```yaml
# Preencha para exibir a seção de depoimentos no site.
# A seção fica escondida enquanto esta lista estiver vazia.
# Exemplo:
# - nome: "Maria S."
#   texto: "Peça impecável e entrega rápida. Recomendo!"
# - nome: "João P."
#   texto: "Atendimento ótimo pelo WhatsApp, ficou exatamente como eu queria."
```

- [ ] **Step 2: Criar `_includes/depoimentos.html`**

```liquid
<div class="depoimentos-grid reveal-stagger">
  {%- for item in site.data.depoimentos -%}
  <figure class="depoimento-card">
    <blockquote>{{ item.texto }}</blockquote>
    <figcaption>{{ item.nome }}</figcaption>
  </figure>
  {%- endfor -%}
</div>
```

- [ ] **Step 3: Adicionar a seção condicional na index (após FAQ)**

Em `index.html`, entre o fechamento de `#faq` e a abertura de `#contato`, inserir:

```liquid
{%- if site.data.depoimentos and site.data.depoimentos.size > 0 -%}
<section id="depoimentos" class="section section-depoimentos">
  <div class="container">
    <header class="section-header section-header-center reveal">
      <span class="section-tag">Depoimentos</span>
      <h2>O que dizem os clientes</h2>
    </header>
    {% include depoimentos.html %}
  </div>
</section>
{%- endif -%}
```

- [ ] **Step 4: Adicionar estilos dos cards**

Em `assets/css/style.scss`, no fim do arquivo, adicionar:

```scss
.depoimentos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.25rem;
}
.depoimento-card {
  margin: 0;
  padding: 1.5rem;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
}
.depoimento-card blockquote {
  margin: 0 0 1rem;
  color: var(--text);
  line-height: 1.6;
}
.depoimento-card blockquote::before { content: "“"; color: var(--cyan); font-weight: 800; }
.depoimento-card figcaption { color: var(--muted); font-weight: 600; font-size: 0.9rem; }
```

- [ ] **Step 5: Verificar que a seção fica escondida quando vazia**

Run: `bundle exec jekyll build`
Expected: build sem erro.

Run: `grep -c 'id="depoimentos"' _site/index.html`
Expected: `0` (lista vazia → seção ausente).

- [ ] **Step 6: Verificar que renderiza quando preenchida (temporário)**

Adicionar temporariamente ao fim de `_data/depoimentos.yml`:

```yaml
- nome: "Teste"
  texto: "Depoimento de teste."
```

Run: `bundle exec jekyll build && grep -c 'id="depoimentos"' _site/index.html`
Expected: `1`

Depois **remover** a entrada de teste (deixar o arquivo só com os comentários do Step 1).

Run: `bundle exec jekyll build && grep -c 'id="depoimentos"' _site/index.html`
Expected: `0`

- [ ] **Step 7: Commit**

```bash
git add _data/depoimentos.yml _includes/depoimentos.html index.html assets/css/style.scss
git commit -m "feat: adiciona estrutura de depoimentos (oculta enquanto vazia)"
```

---

## Task 6: Alt único na galeria via legenda do Instagram

**Files:**
- Modify: `scripts/update-gallery.py` (capturar e gravar `caption`)
- Modify: `_includes/instagram-post.html` (usar caption como alt + data attribute)
- Modify: `_includes/instagram-feed.html` (passar caption; default 8→24)
- Modify: `_includes/footer-scripts.html` (modal usa legenda quando houver)

**Interfaces:**
- Consumes: nada.
- Produces: campo `caption` em cada post de `_data/instagram_posts.yml`; `instagram-post.html` renderiza `alt="{{ caption | default: genérico }}"` e `data-gallery-caption`.

- [ ] **Step 1: Capturar a legenda no coletor (Python)**

Em `scripts/update-gallery.py`, na função `collect_posts`, dentro do laço `for item in items:` (após a linha `post_type = ...`, linha ~89), substituir o `posts.append(...)` por:

```python
            post_type = "reel" if item.get("product_type") == "clips" else "p"
            caption_obj = item.get("caption") or {}
            caption = (caption_obj.get("text") or "").replace("\n", " ").strip()
            posts.append({"code": code, "type": post_type, "image_url": image_url, "caption": caption})
```

- [ ] **Step 2: Gravar a legenda no YAML (Python)**

Em `scripts/update-gallery.py`, na função `main`, no bloco que monta `lines` (linhas ~148-152), substituir por:

```python
        alt = post.get("caption", "")
        if len(alt) > 150:
            alt = alt[:147].rstrip() + "..."
        alt = alt.replace('"', "'")

        lines += [
            f'  - id: "{code}"',
            f'    type: "{post_type}"',
            f'    image: "{web_path}"',
        ]
        if alt:
            lines.append(f'    caption: "{alt}"')
```

- [ ] **Step 3: Verificar que o script ainda compila (sem chamar a API)**

Run: `python3 -m py_compile scripts/update-gallery.py && echo OK`
Expected: `OK`

- [ ] **Step 4: Usar a caption como alt no post**

Em `_includes/instagram-post.html`, substituir a tag `<img>` (linhas 11-17) por:

```liquid
    {%- assign img_alt = include.caption | default: "Trabalho impresso em 3D por @" | append: site.instagram.username -%}
    <img
      class="gallery-image"
      src="{{ include.image | relative_url }}"
      alt="{{ img_alt }}"
      loading="lazy"
      decoding="async"
    >
```

E na abertura do `<button>` (linha 4-10), adicionar o atributo `data-gallery-caption`:

```liquid
  <button
    type="button"
    class="gallery-trigger"
    data-gallery-image="{{ include.image | relative_url }}"
    data-gallery-url="{{ post_url }}"
    data-gallery-caption="{{ include.caption }}"
    aria-label="Ampliar publicação do Instagram"
  >
```

- [ ] **Step 5: Passar caption do feed para o post + corrigir default**

Em `_includes/instagram-feed.html`:

Linha 2, trocar o default de `max_posts`:

```liquid
{% assign max_posts = site.instagram.max_posts | default: 24 %}
```

Linhas 8-12, passar `caption` nos dois includes:

```liquid
    {% if forloop.index0 >= initial %}
      {% include instagram-post.html id=post.id type=post.type image=post.image caption=post.caption hidden=true %}
    {% else %}
      {% include instagram-post.html id=post.id type=post.type image=post.image caption=post.caption %}
    {% endif %}
```

- [ ] **Step 6: Modal usa a legenda quando houver**

Em `_includes/footer-scripts.html`, na função `showAt` (linhas 54-67), substituir a linha que define `modalTitle.textContent` (linha 62) por:

```javascript
      var caption = trigger.dataset.galleryCaption;
      modalTitle.textContent = caption && caption.length ? caption : "Publicação " + (currentIndex + 1) + " de " + total;
```

- [ ] **Step 7: Build e verificação**

Run: `bundle exec jekyll build`
Expected: build sem erro (posts atuais sem `caption` usam o alt genérico — retrocompatível).

Run: `grep -o 'alt="[^"]*"' _site/index.html | grep -c 'Trabalho impresso em 3D'`
Expected: número > 0 (fallback funciona nos posts sem legenda atuais).

- [ ] **Step 8: Commit**

```bash
git add scripts/update-gallery.py _includes/instagram-post.html _includes/instagram-feed.html _includes/footer-scripts.html
git commit -m "feat: alt único na galeria a partir da legenda do Instagram"
```

---

## Verificação final (após todas as tasks)

- [ ] `bundle exec jekyll build` completa sem erro.
- [ ] `bundle exec jekyll serve` → abrir `http://localhost:4000` e conferir visualmente: hero com botão WhatsApp, seção de estimativa calculando (50g/4h → R$ 37,41), FAQ abrindo/fechando, galeria intacta, tema claro/escuro ok.
- [ ] Nenhum depoimento aparece (lista vazia).
- [ ] `grep application/ld+json _site/index.html` mostra os blocos de dados estruturados.

## Notas de execução

- **Commits:** o dono do repositório pediu para não commitar automaticamente nesta sessão. Trate os steps de `git commit` como opcionais — confirme antes de rodar, ou deixe o dono commitar ao final.
- O deploy é automático (GitHub Actions no push para `main`); nada a fazer além do push quando o dono decidir.
