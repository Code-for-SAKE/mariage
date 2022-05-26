# 日本酒マリアージュ

おつまみを入力すると合う日本酒の種類を教えてくれるチャットボット

## tech

- docker for dev
- python3.9
- pip3


## Getting started

```sh
# Clone repository, and move to directory
git clone https://github.com/Code-for-SAKE/mariage.git
cd mariage
```

- backend/data/modelにmodel.saveした内容を配置
  - assets
  - variables
  - keras_metadata.pd
  - saved_model.pd

```
# 再ビルドして起動
docker compose up --build

# Start application (listening on 80)
docker compose up -d
```


## Deploy

### 以下のファイルの`PATH/TO`を環境に合わせる。

- backend/mariage.service
- frontend/nginx/conf.d/mariage.conf

### `backend/data/model`に`model.save`した内容を配置
  - assets
  - variables
  - keras_metadata.pd
  - saved_model.pd

```
# settings
cp frontend/nginx/conf.d/mariage.conf /etc/nginx/conf.d/mariage.conf
ln -s /PATH/TO/backend/mariage.service /etc/systemd/system/mariage.service

# install
dnf install nginx
dnf install python39
pip3 install -r backend/app/requirements.txt

# start service
systemctl start mariage
systemctl start nginx
```