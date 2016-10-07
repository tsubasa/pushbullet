Pushbullet-lite
===============

Pushbulletを通知機能のみサポートした軽量版

主な機能
--------

- note でテキストを通知
- link でテキストとURLを通知

サンプルコード
--------------

    pb = Pushbullet(APIKEY)

    # テキストをプッシュ
    pb.push_note(title, body)

    # テキストとURLをプッシュ
    pb.push_link(title, url, body)
