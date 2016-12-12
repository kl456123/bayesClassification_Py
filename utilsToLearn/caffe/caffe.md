---
title: caffe
date: 2016-09-17 22:34:13
tags:
---

# Caffe：


## 1.如何构造Net:
如果要写确定Net的结构的prototxt,
再进行实例化Net
	

```
net = caffe.Net(model_def,      # defines the structure of the model
model_weights,  # contains the trained weights
caffe.TEST)     # use test mode (e.g., don't perform dropout)
```

如果用python也可以通过'n=Caffe.NetSpec()',给n添加属性构造，但最好仍需通过
	`f.write(str(n.to_proto()))`
保存为prototxt文本以便构造solver.

***

## 2.如何构造Solver:
可以直接像Net一样写Solver训练有关参数的prototxt,
也可以用python接口的

	`from caffe.proto import caffe_pb2`
	`s = caffe_pb2.SolverParameter()`
	
往s里面添加属性然后保存`f.write(str(s))`
***

## 3.如何运行Solver:
* 如果通过CLI运行:
	
```
	build/tools/caffe train \
    	-solver models/finetune_flickr_style/solver.prototxt \
    	-weights models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel \
    	-gpu 0
```
输入类似的格式即可.
weights参数为了fine-tuning或则resume.
这种方法一般用于得到最终训练结果

* 如果通过python则麻烦一点,但可以自己随意调整一般用于临时实验
自己动手保存记录中间的acc和loss
`s.step(1)`
代表运行一次SGD,forward and backward
然后自己看看什么时候输出一下信息记录一下临时精度.
以便画图`plot`
***

## 4.如何加载数据
* `ImageData(transform_param,source,batch_size,new_height,new_width)//read data from raw image`

* `Data(transform_param,source,batch_size,backend)//read data from database`

They are in layers all.So for example , you just call it using `layers.ImageData`

	
***

## 5.如何使用hdf5和lmdb格式

***




## 6.prototxt格式:

* 定义:
  


* 书写:


更多细节可以浏览google的prototxt官方文档
[prototxt](https://developers.google.com/protocol-buffers/)
***



## 7.Caffe代码结构

***
### python:
运行`dir(caffe)` 
display some message:
```
	['AdaDeltaSolver',
	 'AdaGradSolver',
	 'AdamSolver',
	 'Classifier',
	 'Detector',
	 'Layer',
	 'NesterovSolver',
	 'Net',
	 'NetSpec',
	 'RMSPropSolver',
	 'SGDSolver',
	 'TEST',
	 'TRAIN',
	 'classifier',
	 'detector',
	 'get_solver',
	 'io',
	 'layer_type_list',
	 'layers',
	 'net_spec',
	 'params',
	 'proto',
	 'pycaffe',
	 'set_device',
	 'set_mode_cpu',
	 'set_mode_gpu',
	 'set_random_seed',
	 'to_proto']
```
我们来进行分类了解下:
```
	['AdaDeltaSolver',
	 'AdaGradSolver',
	 'AdamSolver',
	'NesterovSolver',
	'RMSPropSolver',
	'SGDSolver',]
```
为各种type的Solver，`layers`为各种layers的集合eg,InnerProduct,ReLU,Convolution,ImageData

`params`为各种常用参数,eg,`Pooling.MAX` and other constant value.
or weight and bias that should be updated during training.

Usage
```
import caffe
<!-- initiate net -->


caffe.param['$blobname'][0] //weight blob
caffe.param['$blobname'][1] //bias blob
```
***

### C++:






* 注意:
** `batch_size`是在*Net*的data layer里面设置的与*Solver*无关.
如果out of memerroy可以调节 `iter_size`, 等效的batch的大小为`batch_size * iter_size` 
** transform_param使用
** `nvidia-smi`查看GPU
** forward and backward
- forward perform a load data and get loss or pred value,return output vector
- backward perform BP,caculate gradient and update the weight and bias. 
- step perform a minbatch both forward and backward

** `Solver` contains any infomation of train.(`Solver.net`)
** `blob` is a data struction containing data flowing in the net.Its struction is like 
```
-blob
	-data:value
	-diff:gradient of weight(only exist in weight blob)
```
** transformer preprocess for image and return a new image
- `scale`:simple scaling for pixel
- `mean`:mean file you must subtract before scaling
How to get it?
like below
```
sudo build/tools/compute_image_mean examples/mnist/mnist_train_lmdb examples/mnist/mean.binaryproto
```





# caffe file struction

## caffe.cpp

* train():



* test():
```

<!-- result is vector<Blob<Dtype>*> type, result[j] is one blob of all output blobs and result[j][k] is one example trained in one batch -->
result = caffe_net.Forward(&iter_loss);


/////////////////////////////////////////

<!-- test_score contains all output value in one batch -->
<!-- test_scroe contains output blobs' ids -->
test_score.push_back(score);
test_score_output_id.push_back(j);


loss /= FLAGS_iterations;
<!-- loss is averaged  -->

```


* 


***




