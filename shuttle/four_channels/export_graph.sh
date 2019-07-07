#!/usr/bin/env bash
cd /home/seten/tensorflow-object-detect/models/research
python object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path "/home/seten/TFM/models/model_shuttlecock_4_channels_0/faster_rcnn_resnet101_shuttle.config" --trained_checkpoint_prefix "/home/seten/TFM/models/model_shuttlecock_4_channels_0/train/model.ckpt-109809" --output_directory "/home/seten/TFM/exported_graphs/model_shuttlecock_4_channels_0"