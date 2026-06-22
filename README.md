# Wisky 3D Print

Landing page de impressão 3D sob encomenda — [3dprint.danielwisky.com.br](https://3dprint.danielwisky.com.br)

Stack: Jekyll · deploy automático via GitHub Actions · galeria sincronizada com [@wisky.3dprint](https://www.instagram.com/wisky.3dprint)

## Local

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

Ruby 3.3+ (ver `.ruby-version`).

## Galeria

```bash
./scripts/update-gallery.sh
git add assets/img/gallery/ assets/img/og-image.jpg _data/instagram_posts.yml \
  && git commit -m "Atualiza galeria" && git push
```

O wrapper cria um virtualenv local em `.venv/` na primeira execução, instala
[Pillow](https://pillow.readthedocs.io/) e roda `scripts/update-gallery.py`,
que:

- baixa as fotos mais recentes (até 24) do feed do Instagram para
  `assets/img/gallery/`, paginando o feed por `max_id` (endpoint `feed/user`)
- regrava `_data/instagram_posts.yml`
- remove imagens órfãs (posts que saíram do feed), com trava de segurança que
  evita apagar em massa se a API falhar
- gera `assets/img/og-image.jpg` (1200×630) com grid 3×2 das primeiras fotos
  e título do site sobreposto — usada como preview ao compartilhar o link

### Exibição

A galeria mostra os primeiros posts e revela o resto com um botão **"Carregar
mais"** (sem recarregar a página). Os itens excedentes começam ocultos, então
suas imagens só são baixadas quando reveladas. Ajuste em `_config.yml`:

```yaml
instagram:
  max_posts: 24   # quantos posts entram na galeria

gallery:
  initial: 12     # quantos aparecem antes de "Carregar mais"
  batch: 12       # quantos cada clique revela
```

> O endpoint do Instagram é não-oficial e pode mudar; se a paginação falhar, o
> script mantém o que conseguiu (~primeira página) sem quebrar.

## Deploy

Push na `main` → GitHub Actions publica no Pages. Repositório precisa ser **público** (plano free).
