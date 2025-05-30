import xml.etree.ElementTree as ET
from svgpathtools import parse_path, Path

from copy import deepcopy
import math

def process_path(path_obj: Path, shear: float) -> Path:

    def skew_point(pt):
        """对单个复数点应用 X 方向倾斜（斜切）"""
        x, y = pt.real, pt.imag
        x_new = x + shear * y
        return complex(x_new, y)

    new_segments = []
    for segment in path_obj:
        segment_copy = deepcopy(segment)
        if hasattr(segment_copy, 'start'):
            segment_copy.start = skew_point(segment_copy.start)
        if hasattr(segment_copy, 'end'):
            segment_copy.end = skew_point(segment_copy.end)
        if hasattr(segment_copy, 'control1'):
            segment_copy.control1 = skew_point(segment_copy.control1)
        if hasattr(segment_copy, 'control2'):
            segment_copy.control2 = skew_point(segment_copy.control2)
        new_segments.append(segment_copy)

    return Path(*new_segments)

def process_circle(elem, shear: float):
    """对 <circle> 的 cx, cy 应用倾斜变换"""
    cx = float(elem.get('cx', '0'))
    cy = float(elem.get('cy', '0'))
    # X 方向倾斜：x' = x + shear * y
    new_cx = cx + shear * cy
    elem.set('cx', str(new_cx))
    # cy 不变


def modify_svg_d_attributes_only(input_svg_path: str, output_svg_path: str):
    # 注册 SVG 命名空间（避免写入 xmlns 前缀）
    ET.register_namespace("", "http://www.w3.org/2000/svg")

    tree = ET.parse(input_svg_path)
    root = tree.getroot()

    ns = {'svg': 'http://www.w3.org/2000/svg'}

    angle_deg = 10
    shear = math.tan(math.radians(angle_deg))

    # 遍历所有 <path> 元素
    for elem in root.findall('.//svg:path', ns):
        d = elem.get('d')
        if d:
            try:
                original_path = parse_path(d)
                new_path = process_path(original_path, shear)
                elem.set('d', new_path.d())
            except Exception as e:
                print(f"⚠️ 无法处理路径: {d}\n错误: {e}")

    for elem in root.findall('.//svg:circle', ns):
        try:
            process_circle(elem, shear)
        except Exception as e:
            print(f"⚠️ 无法处理 circle: {ET.tostring(elem)}\n错误: {e}")

    # 保存新 SVG 文件
    tree.write(output_svg_path, encoding='utf-8', xml_declaration=True)

# 用法
modify_svg_d_attributes_only('input.svg', 'output_with_tilt.svg')
