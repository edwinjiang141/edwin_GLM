#### GLM 的学习

### ChatGLM3-6B 官方微调练习，采用AdvertiseGen数据集。max_steps=10000 ， 由于训练的GPU 是 T4 16GB。所以，max_input_length=64  max_output_length=64. 估计是因为显存大小的限制，导致max_input_length小，导致10000步训练结束后loss还是较大。
#### 训练10000步后的checkpoint在checkpoint-10000 目录下
#### 修改web_demo_gradio.py 中的模型地址为 checkpoint的模型地址：
![图片](https://github.com/edwinjiang141/edwin_GLM/assets/152252397/b22834bb-23f6-444d-a8fb-9a788517adf7)
#### 微调后，模型的测试：
![图片](https://github.com/edwinjiang141/edwin_GLM/assets/152252397/96c9dbb7-89d5-4175-b9f7-3239012130f5)
#### 加载微调后的模型，输出如下：
![图片](https://github.com/edwinjiang141/edwin_GLM/assets/152252397/a6b5ff3f-8450-462b-8106-ba193f60d3e4)
。


### 添加图片风格选项，修改characterglm_api_demo_streamlit.py 如下图
![图片](https://github.com/edwinjiang141/edwin_GLM/assets/152252397/124ee51d-c031-468d-b9ed-b7b186c2f368)

### 实现 role-play 对话数据生成工具
### role-play.py  生成的数据为 chatdata.txt
