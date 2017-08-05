# guest
this is django demo project

## CSRF
django针对CSRF的保护措施是在生成的每个表单中放置一个自动生成的令牌，通过这个令牌判断POST请求是否来自统一个网站。
在form表单中添加{%  csrf_token %}
如果要想忽略掉该检查，可以在guest/setting.py文件中注释掉csrf

## utf-8
在 manage.py 加入
reload(sys)
sys.setdefaultencoding('utf-8')

## 遗留问题
运行test.py 报错

## django代码结构
- 创建django项目
- 创建django应用
    - 应用下，默认会生成tests.py文件
