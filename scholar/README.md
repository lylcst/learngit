安装ES中文分词插件：elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.16.2/elasticsearch-analysis-ik-7.16.2.zip

## ElasticSearch采用 TF/IDF 计算文档相似性
### 检索词频率
检索词在该字段出现的频率？出现频率越高，相关性也越高。 字段中出现过 5 次要比只出现过 1 次的相关性高。
### 反向文档频率
每个检索词在索引中出现的频率？频率越高，相关性越低。检索词出现在多数文档中会比出现在少数文档中的权重更低。
### 字段长度准则
字段的长度是多少？长度越长，相关性越低。 检索词出现在一个短的 title 要比同样的词出现在一个长的 content 字段权重更大。

## Elasticsearch 是一个实时的分布式存储、搜索、分析的引擎
1 Elasticsearch对模糊搜索非常擅长（搜索速度很快）
2 从Elasticsearch搜索到的数据可以根据评分过滤掉大部分的，只要返回评分高的给用户就好了（原生就支持排序）
3 没有那么准确的关键字也能搜出相关的结果（能匹配有相关性的记录）

### 采用倒排索引

### 内置分词器

### 用户输入的内容往往并没有这么的精确

### 我们输入一段文字，Elasticsearch会根据分词器对我们的那段文字进行分词（也就是图上所看到的Ada/Allen/Sara..)，这些分词汇总起来我们叫做Term Dictionary，而我们需要通过分词找到对应的记录，这些文档ID保存在PostingList
### 在Term Dictionary中的词由于是非常非常多的，所以我们会为其进行排序，等要查找的时候就可以通过二分来查，不需要遍历整个Term Dictionary
### 由于Term Dictionary的词实在太多了，不可能把Term Dictionary所有的词都放在内存中，于是Elasticsearch还抽了一层叫做Term Index，这层只存储部分 词的前缀，Term Index会存在内存中（检索会特别快）
### Term Index在内存中是以FST（Finite State Transducers）的形式保存的，其特点是非常节省内存。FST有两个优点：
1）空间占用小。通过对词典中单词前缀和后缀的重复利用，压缩了存储空间；
2）查询速度快。O(len(str))的查询时间复杂度。

### Elasticsearch中有自动影射机制，字符串映射为string，数字映射为long。通过mappings可以指定数据类型是否存储等属性。



./mongod --fork --dbpath=../data/ --condig mongo.conf --logpath=../log/mongodb.log --logappend
