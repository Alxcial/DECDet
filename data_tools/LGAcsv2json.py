import csv
import json

dataset_dir =  '/Users/duan/Documents/MyProgram/MicroVision/Dataset/Batch 8'
annotation_file_path = '/Users/duan/Documents/MyProgram/MicroVision/Dataset/Batch 8/via_region_data.csv'
with open(annotation_file_path, 'r') as csv_file:
    # 创建CSV读取器
    csv_reader = csv.reader(csv_file)
    
    # 跳过第一行（表头）
    next(csv_reader)
    
    # 逐行读取数据
    target_json = {
                "version": "5.0.1",
                "flags": {},
                "shapes": [],
                "imageHeight": 600,
                "imageWidth": 800
            }
    i = 0
    for row in csv_reader:
        if i ==0:
            filename1 = row[0]
        i = i+1
        filename = row[0]
        region_shape_attributes_str = row[5]
        region_attributes_str = row[6]
        # 解析region_shape_attributes字符串为字典
        region_shape_attributes = json.loads(region_shape_attributes_str)  
        region_attributes = json.loads(region_attributes_str)
        # 在这里进行您希望的操作，例如打印数据
        if not region_shape_attributes:
            continue  # 跳过当前行
        if not region_attributes:
            continue
        if 'all_points_x' not in region_shape_attributes:
            continue
        shape_name = region_shape_attributes['name']
        all_points_x = region_shape_attributes['all_points_x']
        all_points_y = region_shape_attributes['all_points_y']
        label = region_attributes['crystal form']
        print(type(region_shape_attributes))
        points = [[x, y] for x, y in zip(all_points_x, all_points_y)]
        # 在这里进行您希望的操作，例如打印数据
        print(f"Shape name: {shape_name}")
        print(f"label: {label}")
        print("Points:")
        for point in points:
            print(f"  Point: {point}")
        print(i)
        if filename1 == filename:
            shape_entry = {
            "label": label,
            "points": points,
            "group_id": None,
            "shape_type": shape_name,
            "flags": {}
            }
            target_json["shapes"].append(shape_entry)
        else:
            target_json = {
                "version": "5.0.1",
                "flags": {},
                "shapes": [],
                "imageHeight": 600,
                "imageWidth": 800
            }
            shape_entry = {
            "label": label,
            "points": points,
            "group_id": None,
            "shape_type": shape_name,
            "flags": {}
            }
            target_json["shapes"].append(shape_entry)

            filename1 = filename
        out_filename = filename.split('.')[0]
        output_file_path = f'/Users/duan/Documents/MyProgram/MicroVision/Dataset/Batch 8/{out_filename}.json'
        with open(output_file_path, 'w') as json_file:
            json.dump(target_json, json_file, indent=2)    
        
