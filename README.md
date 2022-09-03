## 古诗-现代汉语翻译数据集和相应代码

## Datasets and codes about ancient Chinese poems-modern Chinese translation

#### 数据集

数据集见`output.csv`，内容格式为

```csv
半世无归似转蓬，今年作梦到巴东。,我半世以来飘零不定，像蓬草随风；谁想到今年又往巴东，那地方，已多次出现在我的梦中。
身游万死一生地，路入千峰百嶂中。,我就要进入那险阻难行、万死一生的蜀地；行走在危机四伏的小路，面对高耸的百嶂千峰。
邻舫有时来乞火，丛祠无处不祈风。,邻船有人来借火种，荒野的神祠，总有人在祈求顺风。
晚潮又泊淮南岸，落日啼鸦戍堞空。,乘着晚潮船泊在淮水南岸，戍楼空无一人，只有乌鸦啼叫，回荡在凄迷的夕阳中。
```

#### 搜索

输入：古诗句，输出：对应的人工中文翻译

命令行键入

```
cd chinese-ancient-poetry-translation && python poetry_search.py
```

在`poetry_search.py`的主函数里更改待搜索的古诗句

```python
if __name__ == "__main__":
    search_res = search("床前明月光，疑是地上霜。")
    print(search_res)
    
# 打印结果为:明亮的月光洒在床前的窗户纸上，好像地上泛起了一层霜。
```



