| Model  |inference, ms | size of model, mb |
|---|---|---|
| YOLOv8l | 379 | 166.8 |
| YOLOv8l (quantize_dynamic) | 322.9 | 166.8 |
| YOLOv8l (prune.l1_unstructured) | 346 | 333 |
| YOLOv8l (kmean_cluster) | 353.8 | 166.8 |
| GroundingDINO (distill) | 350.4 | 661.8 |
| YOLOv8l (distill) | 18.5 | 166.8 |
| YOLOv8l (openvino) | 417.6 | 166.7 |
| YOLOv8l (onnx) | 353.2 | 166.8 |
| AutoModelForQuestionAnswering | 230 | 253.2 |
| ORTModelForQuestionAnswering | 331.72 | 473.3 |