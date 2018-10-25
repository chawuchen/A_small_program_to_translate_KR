# A_small_program_to_translate_KR
十分简陋的一个小脚本
原理：
HOI4中所有显示在游戏中的文本在localisation中的各yml文件里
且由引号""框住 因此只需要以引号为标记把内容提取出来
翻译
再放入原文件中即可
注意谷歌翻译前与翻译后的引号不同，且可能忽略引号，故最终放入原文件时采取的分段标志是换行
如果所有引号是完全正确匹配的，使用google翻译能在1分钟内完成一份文件


使用说明：
需要预装pyperclip包
首先将跳出当前目录下的文件数 和 from where?
输入一个数字 即从第几个文件开始(初始为0)
然后会输出
文件名（第几个）
（如果是yml文件）它的大小
继续？


此时已经剪贴板中已保存了需要修改的内容，在源目录下也创建了reading.txt文件
翻译后将文本再写入reading.txt并保存
格式如下（隔一行），最后一行也需要加空格
"AAAAA"
（空格）
"BBBBB"
（空格）
"CCCC"
（空格）

这是因为，这一格式是用来匹配谷歌浏览器的网页翻译的。
再在程序中输入‘ENTER’（回车）后即汉化完成，进入下一个文件

另外输入‘1+ENTER’ 表示跳过该文件继续
'0+ENTER'表示放弃修改并停止


具体操作见b站视频32388853

一些常见的错误：
Traceback (most recent call last):
  File "XXXXXX\XXXXX\read.py", line 55, in <module>
    u2 = tran_list[s][-1]
IndexError: list index out of range
 这是因为汉化文本与原文本条数没有对齐
  
Traceback (most recent call last):
File "XXXX\read.py", line 42, in <module>
text2 = f2.read()
File "XXXX\Python\Python37\lib\codecs.py", line 322, in decode
(result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa1 in position 0: invalid start byte
 这是因为reading.txt没有被保存为utf-8格式，在另存为中将编码方式更改一下就行了
