## sasa_wrapper

CeVIO AIの外部連携インターフェイスのラッパー

CeVIO AIの起動が必要（していない場合は自動で起動する）

python 3.8で動作確認済

## APIドキュメント

https://takana-v.github.io/sasawrapper/

## インストール

```bash
pip install git+https://github.com/takana-v/sasawrapper.git@releases
```

## 使用例

### コマンドラインから

```bash
python -m sasawrapper speak こんにちは
python -m sasawrapper speak --cast さとうささら --volume 60 --emotion 怒り 50 --emotion 哀しみ 50 色々オプション付きの例です
```

コマンドの一覧は`python -m sasawrapper -h`参照  
コマンドの詳細は`python -m sasawrapper コマンド名 -h`参照

### モジュールとして利用

```python
import sasawrapper
sasawrapper.speak("こんにちは")
```