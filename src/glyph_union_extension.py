import subprocess
import os
from lxml import etree
import threading
import time

# 用于合并字体分组下所有内容的脚本
# 需要用到Inkscape 1.0前的版本

def get_all_paths(group_element):
    paths = []
    for child in group_element:
        if child.tag.endswith('g'):
            paths.extend(get_all_paths(child))
        elif child.tag.endswith('path'):
            paths.append(child)
    return paths

def run_union(filename):
    subprocess.run([
        "inkscapeold", 
        filename, 
        "--verb=EditSelectAll", 
        "--verb=SelectionUnion", 
        "--verb=FileSave", 
        "--verb=FileClose"])

def glyph_union():
    input_svg = r".\output_1.svg"
    output_svg = r".\output_with_union.svg"

    threads = []
    filenames = []

    tree = etree.parse(input_svg)
    root = tree.getroot()
    
    top_level_group = root.find(".//{http://www.w3.org/2000/svg}g")

    child_groups = [child for child in top_level_group if child.tag.endswith('g')]
    # print(child_groups)
    for group in child_groups:
        paths = get_all_paths(group)

        temp_svg = etree.Element('svg', nsmap={None: "http://www.w3.org/2000/svg"})
        for path in paths:
            for attr in ['style', 'visibility', 'opacity']:
                if attr in path.attrib:
                    del path.attrib[attr]
            temp_svg.append(path)

        group_id = group.attrib.get('id', 'default_id')
        temp_svg_file = f"{group_id}_temp_paths.svg"
        
        with open(temp_svg_file, 'wb') as f:
            f.write(etree.tostring(temp_svg))

        new_thread = threading.Thread(target = run_union, args = (temp_svg_file,))
        while threading.active_count() >= 100:
            time.sleep(0.1)
        new_thread.start()
        threads.append(new_thread)
        filenames.append(temp_svg_file)

    for thread in threads:
        thread.join()
    
    for i, group in enumerate(child_groups):
        for child in list(group):
            if child.tag.endswith('g') or child.tag.endswith('path'):
                group.remove(child)

        union_path = None
        try:
            group_tree = etree.parse(filenames[i])
            union_path = group_tree.getroot().find(".//{http://www.w3.org/2000/svg}path")
        except Exception as e:
            print(f"[警告] 解析 {filenames[i]} 失败：{e}")

        if union_path is not None:
            group.append(union_path)
        else:
            print(f"[跳过] {filenames[i]} 中没有找到合并后的 path，已跳过。")

        os.remove(filenames[i])

    tree.write(output_svg, encoding="utf-8", xml_declaration=True)

if __name__ == '__main__':
    glyph_union()
