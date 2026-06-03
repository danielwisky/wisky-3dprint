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

- baixa as 12 fotos mais recentes do feed do Instagram para `assets/img/gallery/`
- regrava `_data/instagram_posts.yml`
- gera `assets/img/og-image.jpg` (1200×630) com grid 3×2 das primeiras fotos
  e título do site sobreposto — usada como preview ao compartilhar o link

## Deploy

Push na `main` → GitHub Actions publica no Pages. Repositório precisa ser **público** (plano free).
