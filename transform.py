import json
import numpy as np

with open('exports/camjson/transforms_train.json', 'r', encoding='utf-8') as f:
    cameras_train = json.load(f)

with open('exports/camjson/transforms_eval.json', 'r', encoding='utf-8') as f:
    cameras_eval = json.load(f)

cameras = cameras_train + cameras_eval
cameras = sorted(cameras, key=lambda x: x['file_path'])

final_path = {"keyframes":[],
              "seconds":8,
              "camera_type": "perspective",
              "fov": 55,
              "aspect": 1,
              "render_height": 512, "render_width": 512,
              "camera_path": [],
              "fps": 24,
              "smoothness_value": 0, 
              "is_cycle": False
              }

for cam in cameras:
    transform = np.array(cam["transform"])
    camera_to_world = np.vstack([transform, [0, 0, 0, 1]])
    # camera_to_world
    camera = {"camera_to_world": camera_to_world.tolist(),
              "fov": 55,
              "aspect": 1
             }
    final_path["camera_path"].append(camera)

with open('exports/camjson/cameras.json', 'w', encoding='utf-8') as f:
    json.dump(final_path, f, ensure_ascii=False, indent=4)
