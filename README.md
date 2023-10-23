# Itmo_Model_Compression

Lab 1/2

|  Device |  Model |Inference time   |  Weight |
|---|---|---|---|
| i7-12650 H | yolov8n  |  950ms |  6mb |
|  Nvidia 4060  Mobile   |  yolov8l |  17.5ms |  86mb |
|  Nvidia 4060  Mobile   |  yolov8l 30% sparse |  16.1ms |  85.1mb |
|  Nvidia 4060  Mobile   |  yolov8l 90% row-sparse |  15.4ms|   85.1mb  |


Lab 3

|  Model |  Model size |  Model size compressed |
|---|---|---|
| yolov8n | 6mb  |1.5 mb|

lab 4
|  Teacher |  Student  |
|---|---|
| Grounding dino | yolov8n |
| 330 mb | 6 mb |
|52.5 mAP| 15.2 mAP|
|0.15s on A100| 10ms on A100|

lab 5

|  Raw yolov8s speed | onnx |  openvino |
|---|---|---|
| 454 ms | 288 ms  |1s|

lab 6

|  ViT-B raw T4 | better-transformers accelerator |
|---|---|
| 145 s/dataset | 137 s/dataset  |
