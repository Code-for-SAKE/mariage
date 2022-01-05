# KIA 先端技術研究会 2021 デモ

## Getting started

```sh
# Clone repository, and move to directory
git clone https://github.com/mebius-yokohama/kia-demo.git
cd kia-demo
# Start application (listening on 80)
docker compose up -d
```

- backend/data/modelにmodel.saveした内容を配置
  - assets
  - variables
  - keras_metadata.pd
  - saved_model.pd

```
# 再ビルドして起動
docker compose up --build
```