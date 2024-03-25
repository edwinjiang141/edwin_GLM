#### GLM 的学习

### ChatGLM3-6B 官方微调练习，采用AdvertiseGen数据集。max_steps=10000 ， 由于训练的GPU 是 T4 16GB。所以，max_input_length=64  max_output_length=64. 10000步训练结束后的截图如下：
![图片](https://github.com/edwinjiang141/edwin_GLM/assets/152252397/96c9dbb7-89d5-4175-b9f7-3239012130f5)



### 添加图片风格选项，修改characterglm_api_demo_streamlit.py 如下图
![图片](https://github.com/edwinjiang141/edwin_GLM/assets/152252397/124ee51d-c031-468d-b9ed-b7b186c2f368)

### 实现 role-play 对话数据生成工具
### role-play.py  生成的数据为 chatdata.txt
