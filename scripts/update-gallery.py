#!/usr/bin/env python3
"""Baixa as últimas 8 fotos do @wisky.3dprint e atualiza _data/instagram_posts.yml."""

import json
import os
import urllib.request

USERNAME = "wisky.3dprint"
MAX_POSTS = 8
GALLERY_DIR = "assets/img/gallery"
DATA_FILE = "_data/instagram_posts.yml"


def main():
    os.makedirs(GALLERY_DIR, exist_ok=True)

    req = urllib.request.Request(
        f"https://www.instagram.com/api/v1/users/web_profile_info/?username={USERNAME}",
        headers={"User-Agent": "Mozilla/5.0", "X-IG-App-ID": "936619743392459"},
    )
    with urllib.request.urlopen(req) as response:
        data = json.load(response)

    edges = data["data"]["user"]["edge_owner_to_timeline_media"]["edges"][:MAX_POSTS]
    lines = ["posts:"]

    for edge in edges:
        node = edge["node"]
        code = node["shortcode"]
        post_type = "reel" if node.get("product_type") == "clips" else "p"
        image_path = f"{GALLERY_DIR}/{code}.jpg"
        web_path = f"/assets/img/gallery/{code}.jpg"

        img_req = urllib.request.Request(node["display_url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(img_req) as img_response:
            with open(image_path, "wb") as img_file:
                img_file.write(img_response.read())

        lines += [
            f'  - id: "{code}"',
            f'    type: "{post_type}"',
            f'    image: "{web_path}"',
        ]

    with open(DATA_FILE, "w", encoding="utf-8") as data_file:
        data_file.write("\n".join(lines) + "\n")

    print(f"Atualizado: {len(edges)} posts em {GALLERY_DIR}")


if __name__ == "__main__":
    main()
