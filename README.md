# README

## app demostration

1. `wx_user`

    存储来自微信用户数据的数据库存储和相关的后端操作。

2. `sweepstake`

    存储每次抽奖的信息的数据库存储和相关的后端操作。

3. `participate`

    存储用户参与单次抽奖的信息。

## config

需要在 `lottery_backend` 文件夹中创建 `secret.py` 文件

## API

1. `/admin`:

    数据库管理界面

2. `/wx_user/log_in`:

    登录路由，正常情况下会返回一个 Json 数据包

3. `/sweepstake/query_swpstk`:

    查询抽奖活动路由，查询所有可用的抽奖活动，并以 Json 数据包形式返回

4. `/participate/participate_in`:

    参与抽奖路由，传入一个用户 id 和一个表征抽奖活动的 id，返回是否参与成功的 Json 数据包。

5. `/participate/check_participated`:

    查询是否参与抽奖路由，返回一个表征是否参与的 Json 数据包。

6. `/participate/query_participated`:

    传入一个用户 id，查询其参与过的所有抽奖活动与其抽奖结果