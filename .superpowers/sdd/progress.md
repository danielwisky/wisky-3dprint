# Progresso — Melhorias no Portal (feat/portal-improvements)

Base: 0ab9704 (main @ 0ab9704)
Plano: docs/superpowers/plans/2026-07-02-portal-improvements.md

## Tasks
- Task 1 (WhatsApp CTA): COMPLETE (d47696d)
- Task 2 (Calculadora): COMPLETE (04b7f02)
- Task 3 (FAQ): COMPLETE (a9583be)
- Task 4 (JSON-LD): COMPLETE (2ceb3dd)
- Task 5 (Depoimentos): COMPLETE (eaf3c51)
- Task 6 (Alt galeria): COMPLETE (39ed3ce)

## Log
- Task 1: COMPLETE (commit d47696d, base 0ab9704, review spec ✅). Fix aplicado: parágrafo #contato e hero-lead → WhatsApp.
  Minor p/ review final: (a) link inline do Passo 03 usa wa.me direto — INTENCIONAL (link em prosa, não botão); (b) nav-cta label "WhatsApp" genérico; (c) svg WhatsApp sem focusable="false" (segue padrão do projeto).
- Task 2: COMPLETE (commit 04b7f02, base d47696d, review spec ✅ qualidade ✅). Fix: guard h<=0 (consistência com g<=0). Fórmula verificada 50g/4h=R$37,41.
- Task 3: COMPLETE (commit a9583be, base 04b7f02, review spec ✅ qualidade ✅). 6 itens FAQ, sem JS.
  Nota p/ review final: revisor marcou outline-offset:-2px como Important (risco de corte pelo overflow:hidden). Adjudicado: outline é inset, fica DENTRO do summary — foco visível, padrão válido. Não alterado. Reconferir no review final se quiser.
- Task 4: COMPLETE (commit 2ceb3dd, base a9583be, review spec ✅ qualidade ✅). 3 blocos JSON-LD válidos (ProfessionalService + FAQPage + seo-tag).
  Minor p/ futuro: serviceType hardcoded; sem guard site.instagram nulo.
- Task 5: COMPLETE (commit eaf3c51, base 2ceb3dd, review spec ✅ qualidade ✅). Seção oculta quando vazia (0/1/0 verificado), sem conteúdo falso.
  Minor p/ futuro: considerar `| escape` em item.texto/item.nome (dados owner-controlled, risco baixo).
- Task 6: COMPLETE (commit 39ed3ce, base eaf3c51, review spec ✅ qualidade ✅). Retrocompat confirmada (24 alts fallback). Fix: sanitiza barra invertida na caption (evita YAML não fechado).

## Review final (branch inteira, Opus)
Veredicto: PRONTO PARA MERGE, sem Critical. 2 fixes aplicados:
- I1: hero-stats "Contato" → WhatsApp (era Instagram). commit final.
- I2: .nav-cta display:inline-flex + gap (ícone+texto do include desalinhavam). commit final.
Minor aceitos como followup: nav-cta focusable, serviceType hardcoded, guard site.instagram, |escape depoimentos, data-gallery-caption vazio. Todos sem impacto atual.
