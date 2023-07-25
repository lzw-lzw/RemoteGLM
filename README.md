# RemoteGLM
用于遥感图像场景分析的中文多模态大模型 | Chinese multimodal large-scale model for remote sensing image scene analysis

## 介绍
目前的通用多模态大模型[LLaVA](https://github.com/haotian-liu/LLaVA)、[MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4)等模型，在广泛意义上取得了较好的效果，但这些多模态大模型在细分垂直领域的应用效果相对较差。目前还几乎没有用于遥感图像场景分析的多模态大模型，这在一定程度上受限于遥感图像相关数据集的稀缺，因此基于通用多模态大模型的微调为遥感大模型的研究提供了可能。

VisualGLM-6B 是清华大学开源开源的，支持图像、中文和英文的多模态对话语言模型，由语言模型ChatGLM-6B与图像模型BLIP2-Qformer结合得到，整体模型共78亿参数，它能够整合视觉和语言信息，可用来理解图片，解析图片内容，结合模型量化技术，用户可以在消费级的显卡上进行本地部署。

因此，RemoteGLM模型基于VisualGLM-6B，在遥感图像-中文数据集上进行微调得到，在遥感图像场景分析任务中具有较好的结果。

## 效果展示

## 方法

## 数据集
一些常见的用于训练遥感视觉语言模型的[数据集](https://github.com/lzw-lzw/awesome-remote-sensing-vision-language-models#dataset)都是英文构建的，无法直接用于中文微调。因此参照[XrayGLM](https://github.com/WangRongsheng/XrayGLM)的方法构建中文数据集。
## 使用方法

### 环境配置

### 模型推理

### 模型训练

## 问题及改进方向

## 致谢
