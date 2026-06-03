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
python3 scripts/update-gallery.py   # baixa as 8 últimas fotos + atualiza _data/instagram_posts.yml
git add assets/img/gallery/ _data/instagram_posts.yml && git commit -m "Atualiza galeria" && git push
```

## Deploy

Push na `main` → GitHub Actions publica no Pages. Repositório precisa ser **público** (plano free).
