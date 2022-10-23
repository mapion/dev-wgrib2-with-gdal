# dev-wgrib2-with-gdal

wgrib2とGDALが使えるpython3の開発環境です

# 使い方

## git clone

```sh
git clone https://github.com/mapion/dev-wgrib2-with-gdal.git
```

## イメージ作成＆コンテナ作成＆コンテナ起動

```sh
cd path/to/dev-wgrib2-with-gdal
docker compose up -d --build
# 既にイメージが存在しているなら--buildは要らない
```

## コンテナに接続

```sh
docker compose exec dev-wgrib2 bash
```

## テスト

> コンテナに接続後以下

```sh
python -V
wgrib2 --version
gdalinfo --version
python opt/check.py
```

## 開発

コンテナに接続後`opt`フォルダ内でpython開発する

# 削除

## コンテナ削除

```sh
$ docker container ls
$ docker compose down
$ docker container ls
```

## イメージ削除

```sh
$ docker image ls
$ docker image rm {imageid}
$ docker image ls
```
