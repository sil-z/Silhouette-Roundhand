# Silhouette-Roundhand

本字体个人商用免费，企业用途请联系作者；使用时需要注明出处。

作者邮箱：zz7966587 AT gmail DOT com

2025/5/31：调整了字体斜度，将标点符号的宽度改为0并添加了标点两侧字母的连字规则，修改了部分大写和数字的字形，调整了大写左侧间距，更新了字体预览图。

字体源文件位于src文件夹中，其中：

- .fea文件为导入FontForge中的字形配置文件
- .svg文件为使用Inkscape编辑的原始字形
- ***_publish.svg文件为经过合并后可以直接使用FF打开的字形文件
- stroke_to_path.bat文件用于将开放曲线转为闭合路径，因为OpenType的轮廓必须封闭
- glyph_union_extension.py文件用于对转换闭合路径后的中间svg进行字形合并操作，必须安装旧版本（<1.0）的Inkscape，因为新版本似乎不支持此功能
- 生成字体步骤待更新

使用步骤（以Windows系统为例）：

1. 双击打开.otf文件，点击安装
2. 在设计软件中找到Silhouette's Roundhand字体，选择并应用

注意事项：由于本字体使用了上下文连字特性，在Office和WPS中使用本字体必须选中希望应用字体的字符并启用上下文连字，否则字体将无法正常显示。

预览图：

![example.png](example.png)
