#!/bin/sh
# Пересобрать и выложить dist/ на GitHub Pages (ветка gh-pages).
set -e
cd "$(dirname "$0")"
sh build.sh
if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -m "${1:-Обновление карточек}"
fi
git push origin main
git push origin `git subtree split --prefix dist main`:gh-pages --force
echo "Готово. Страница обновится за минуту."
