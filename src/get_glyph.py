import xml.etree.ElementTree as ET
from svgpathtools import parse_path, Path, Line, CubicBezier, QuadraticBezier, Arc

def flip_svg_path_vertically(path_d, em_height=1000):
    path = parse_path(path_d)
    flipped_segments = []

    for segment in path:
        def flip_point(pt):
            return complex(pt.real, em_height - pt.imag)

        if isinstance(segment, Line):
            flipped_segments.append(Line(
                flip_point(segment.start),
                flip_point(segment.end)
            ))

        elif isinstance(segment, CubicBezier):
            flipped_segments.append(CubicBezier(
                flip_point(segment.start),
                flip_point(segment.control1),
                flip_point(segment.control2),
                flip_point(segment.end)
            ))

        elif isinstance(segment, QuadraticBezier):
            flipped_segments.append(QuadraticBezier(
                flip_point(segment.start),
                flip_point(segment.control),
                flip_point(segment.end)
            ))

        elif isinstance(segment, Arc):
            # 注意：rx, ry 不变；rotation 保持，large-arc, sweep 需要翻转 sweep
            flipped_segments.append(Arc(
                start=flip_point(segment.start),
                radius=segment.radius,
                rotation=segment.rotation,
                large_arc=segment.large_arc,
                sweep=not segment.sweep,  # sweep 方向翻转
                end=flip_point(segment.end)
            ))

        else:
            print(f"未知段类型：{type(segment)}，跳过")
            continue

    return Path(*flipped_segments).d()



def format_unicode_string(unicode_val):
    """将字符或字符序列转换为 U+XXXX 格式"""
    if unicode_val is None:
        return ""
    if unicode_val.startswith("-"):  # 未分配字符的负数，如 -1
        return ' '.join(f"U+{ord(c):06X}" for c in unicode_val)
    return ' '.join(f"U+{ord(c):06X}" for c in unicode_val)

def get_label(unicode_val, glyph_name):
    """生成 inkscape:label 字符串"""
    if unicode_val is None:
        return f"{glyph_name} {glyph_name}"
    return f"{format_unicode_string(unicode_val)} {unicode_val} {glyph_name}"

def copy_path_d_to_glyph(svg_path):
    NS = {
        'svg': 'http://www.w3.org/2000/svg',
        'inkscape': 'http://www.inkscape.org/namespaces/inkscape'
    }

    tree = ET.parse(svg_path)
    root = tree.getroot()

    # 获取所有 glyph 标签
    glyphs = root.findall(".//{*}glyph")
    for glyph in glyphs:
        glyph_name = glyph.get("glyph-name")
        unicode_val = glyph.get("unicode")
        if unicode_val == '"' or unicode_val == "'":
            continue

        if glyph_name is None:
            continue  # 无效 glyph，跳过

        label = get_label(unicode_val, glyph_name)

        # 查找对应的 <g inkscape:label="...">
        g_elements = root.findall(f'.//svg:g[@inkscape:label="{label}"]', NS)
        if not g_elements:
            print(f"未找到匹配的 g 元素: {label}")
            continue

        g = g_elements[0]
        paths = g.findall(".//svg:path", NS)
        if len(paths) != 1:
            print(f"g 元素中 path 数量不是 1: {label}")
            continue

        path_d = paths[0].get("d")
        if path_d:
            path_d = flip_svg_path_vertically(path_d, em_height=1000)
            glyph.set("d", path_d)
            print(f"更新 glyph: {label}")

    # 保存修改后的 SVG
    tree.write("output_with_glyphs.svg")

# 示例用法
copy_path_d_to_glyph("input.svg")
