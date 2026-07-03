# Task 5 — Depoimentos (Testimonials Section)

## Implementation Summary

Implemented the testimonials section structure as specified, with the section remaining hidden while the data list is empty.

## Files Modified/Created

1. **_data/depoimentos.yml** - Created
   - Contains only comments and empty list
   - Ready for customer testimonials to be added

2. **_includes/depoimentos.html** - Created
   - Renders testimonials grid with cards
   - Loops through `site.data.depoimentos` entries
   - Uses classes: `depoimentos-grid`, `reveal-stagger`, `depoimento-card`

3. **index.html** - Modified
   - Added conditional section between FAQ (#faq) and Contact (#contato)
   - Section only renders when `site.data.depoimentos` exists and has size > 0
   - Header uses reused classes: `.section-header`, `.section-header-center`, `.section-tag`

4. **assets/css/style.scss** - Modified
   - Appended 6 new CSS rules for testimonials styling
   - Grid layout: auto-fit with minmax(260px, 1fr)
   - Card styling with CSS tokens: `--surface`, `--border`, `--text`, `--muted`, `--cyan`
   - Blockquote with opening curly quote decoration

## Build Verification

- `bundle exec jekyll build` completed successfully without errors
- CSS syntax: Fixed curly quote encoding in blockquote::before rule

## Section Visibility Tests

| State | grep count | Status |
|-------|-----------|--------|
| Empty list | 0 | ✓ Section hidden as expected |
| With test entry | 1 | ✓ Section renders correctly |
| After test removal | 0 | ✓ Section hidden again |

## Git Commit

- Hash: `eaf3c51`
- Message: "feat: adiciona estrutura de depoimentos (oculta enquanto vazia)"
- Files: 4 changed, 47 insertions (+)
  - Created: `_data/depoimentos.yml`, `_includes/depoimentos.html`
  - Modified: `index.html`, `assets/css/style.scss`

## Test Data Handling

- ✓ Temporary test entry added to verify rendering (nome: "Teste", texto: "Depoimento de teste.")
- ✓ Test entry removed before commit
- ✓ Final state: file contains only comments, list is empty
- ✓ Verified section is hidden after removal (grep count = 0)

## Concerns

None. Implementation follows specifications exactly:
- Conditional rendering works correctly
- CSS tokens properly reused
- Build has no errors
- File structure matches requirements
