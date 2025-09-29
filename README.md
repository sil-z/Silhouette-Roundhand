# Silhouette-Roundhand

**This font is free for commercial use, provided that the author (or any official source where the font was released) is credited in a detailed description near where the font is used. For example:**

- For posters: Credit directly on the poster itself, or on any link the poster points to.
- For trademarks: Credit on the official website’s information page, or everywhere the trademark is used.
- For books: Credit in the references section or in any other part of the book.
- For blogs or other online media: Credit within the original text.

The above scenarios are not exhaustive. If, in practice, it is not possible to credit the author in any form, you must contact the author and purchase a commercial license, which then allows unrestricted use with peace of mind.

Even in personal use cases, or when proper credit has already been given, additional sponsorship or donations to the author are always welcome.

**Author's Email:** zz7966587 AT gmail DOT com

**2025/5/31 Update:** Adjusted the font's tilt angle, set punctuation width to 0, added ligature rules for letters surrounding punctuation, modified some uppercase letters and digits, adjusted left spacing of uppercase letters, and updated the font preview image. Since this is an experimental work, it has many fundamental issues and will not be further optimized in the future.

The source files of the font are located in the src folder, which includes:

- .fea file: Glyph configuration file for import into FontForge
- .svg file: Original glyphs edited using Inkscape
- tilt_adjustment.py: Script for handling possible tilt transformations
- stroke_to_path.bat: Converts open curves into closed paths, as OpenType outlines must be closed
- glyph_union_extension.py: Performs glyph merging on intermediate SVG files after closing paths; requires an older version of Inkscape (<1.0), as newer versions seems not support this function
- get_glyph: Converts the merged path elements into glyphs that can be directly imported into FontForge

Font generation steps are to be updated.

**How to use (example for Windows systems):**

1. Double-click the .otf file and click "Install"
2. In your text-input software, find the font named SilhouetteRoundhand, select and apply it

**Note:** This font uses contextual ligature features. When using this font in office software such as Microsoft Office or WPS Office, you must:

1. Select the characters you want to apply the font to
2. Open the "Font" settings from the right-click menu
3. In the "Opentype Features", under the "Advanced" tab, set "Ligatures" to "Standard and Contextual", and check the "Use Contextual Alternates" checkbox

Otherwise, the natural connections between letters will not render correctly.

If you're using Notepad, Adobe Illustrator, or rendering directly in a web browser, no additional settings are required.

---

**本字体商用免费，前提是必须在字体被使用处附近的详细描述中注明作者（的任一字体发布来源），例如：**

- 用于海报：直接在海报中，或在海报指向的任一链接中注明
- 用于商标：在官方网站的说明页中注明，或在所有使用商标处均注明
- 用于书籍：在书籍的参考资料部分或任意其他部分注明
- 用于网络博客或其余形式载体：在原文中说明

可能的使用场景并不局限于以上所列。如实际场景不便在任何地方注明作者，需要联系作者付费以购买商用版权，这样就可以心安理得地随意使用。

即使是在个人使用场景下或使用时已经注明作者，额外向作者赞助也是受欢迎的。

**作者邮箱：** zz7966587 AT gmail DOT com

**2025/5/31 更新：** 调整了字体斜度，将标点符号的宽度改为0并添加了标点两侧字母的连字规则，修改了部分大写和数字的字形，调整了大写左侧间距，更新了字体预览图。由于这是一个实验作品，存在许多基本的问题，后续将不再进行优化。

字体源文件位于src文件夹中，其中：

- .fea 文件为导入 FontForge 中的字形配置文件
- .svg 文件为使用 Inkscape 编辑的原始字形
- tilt_adjustment.py 文件用于执行可能存在的斜度转换需求
- stroke_to_path.bat 文件用于将开放曲线转为闭合路径，因为 OpenType 的轮廓必须封闭
- glyph_union_extension.py 文件用于对转换闭合路径后的中间 svg 进行字形合并操作，必须安装旧版本（< 1.0）的 Inkscape，因为新版本似乎不支持此功能
- get_glyph.py 文件用于将合并后的路径元素转换为字形，使得文件成为能被 FontForge 直接读取的格式
- 生成字体步骤待更新

**使用步骤（以 Windows 系统为例）：**

1. 双击打开.otf文件，点击安装
2. 在文字输入软件中找到 SilhouetteRoundhand 字体，选择并应用

**注意事项：** 由于本字体使用了上下文连字特性，在 Microsoft Office 和 WPS Office 等办公软件中使用本字体必须：

1. 选中希望应用字体的字符
2. 在右键菜单中打开字体设置
3. 在高级选项卡中的 OpenType Features 下，将 Ligatures 设为 Standard and Contextual，并选中 Use Contextual Alternates 复选框

否则，字母间的自然连接将无法被正确渲染。

若使用记事本，Adobe Illustrator等软件或者直接在浏览器中进行渲染，则不需要进行额外设置。

![example.png](https://raw.githubusercontent.com/sil-z/Silhouette-Roundhand/refs/heads/main/example.png)
