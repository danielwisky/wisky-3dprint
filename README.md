# Wisky 3D Print

Landing page de impressão 3D sob encomenda. Instagram: [@wisky.3dprint](https://www.instagram.com/wisky.3dprint).

Site estático com [Jekyll](https://jekyllrb.com/), publicado no GitHub Pages.

## Desenvolvimento local

```bash
bundle install
bundle exec jekyll serve
```

Acesse http://localhost:4000

> Use sempre `bundle exec jekyll` (não `jekyll` direto). Dependências: `bundle install`.

## Atualizar galeria do Instagram

A galeria exibe **somente as imagens** das últimas 8 publicações. Ao clicar, abre um **modal** com a foto ampliada e botão para ver o post no Instagram.

### Comando rápido

Na raiz do projeto, rode:

```bash
python3 scripts/update-gallery.py
```

O script:

1. Busca as 8 postagens mais recentes de [@wisky.3dprint](https://www.instagram.com/wisky.3dprint)
2. Baixa as fotos para `assets/img/gallery/`
3. Atualiza [`_data/instagram_posts.yml`](_data/instagram_posts.yml)

Depois, gere o site novamente:

```bash
bundle exec jekyll serve
```

### Fluxo completo (atualizar + publicar)

```bash
python3 scripts/update-gallery.py
bundle exec jekyll build
git add assets/img/gallery/ _data/instagram_posts.yml
git commit -m "Atualiza galeria Instagram"
git push
```

### Adicionar post manualmente

Edite [`_data/instagram_posts.yml`](_data/instagram_posts.yml) e salve a imagem em `assets/img/gallery/`:

```yaml
posts:
  - id: "ABC123xyz"
    type: "p"       # ou "reel"
    image: "/assets/img/gallery/ABC123xyz.jpg"
```

| Campo | Descrição |
|-------|-----------|
| `id` | Código do post na URL (`/p/ABC123xyz/` ou `/reel/...`) |
| `type` | `p` para foto/carrossel · `reel` para reels |
| `image` | Caminho local da imagem no site |

## Publicação

1. Repositório `danielwisky/wisky-3dprint` no GitHub
2. **Settings → Pages → GitHub Actions**
3. Push na branch `main` dispara o deploy

## Subdomínio

Arquivo [`CNAME`](CNAME): `3dprint.danielwisky.com.br`

| Tipo  | Nome      | Valor                   |
|-------|-----------|-------------------------|
| CNAME | `3dprint` | `danielwisky.github.io` |

No GitHub: **Settings → Pages → Custom domain** + **Enforce HTTPS**.
