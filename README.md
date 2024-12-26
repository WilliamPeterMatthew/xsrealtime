# xsrealtime
rankupdate配套项目

- `config.py` 与 `sysconfig.py` 用于配置，请理解后再配置
- `listen.py` 与 `listen one.py` 用于实时抓取并推送到 `rankupdate` 网站
- `notify.py` 用于向指定群组通知，需要配置好 `cpp.txt` 和 `py.txt` 作为组， `text.txt` 作为通知内容
- `transform.cpp` 和 `transform.py` 用于将 `rankupdate` 网站上下载的内容转换格式为成绩文件
