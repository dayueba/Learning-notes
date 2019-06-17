# python面试题

1. **一行代码实现1--100之和** 

   ```
   sum(range(1,101))
   ```

2. **如何在一个函数内部修改全局变量**
  利用global修改全局变量
  ```
  a = 5
  def fn():
  	global a
  	a = 2
  # a = 2
  ```

3. **列出5个标准库**
  os: 提供与操作系统有关的函数
  math: 数学运算
  random:  随机数
  re:  正则匹配
  datetime:  时间
  time： 时间

4. **字典如何删除键和合并两个字典**
  ```
  dic = {'name':'wang','age':18}
  del dic['age']  # 删除
  dic.update({'age':18})  # 合并  
  ```

5. **python的GIL**

6. **python列表去重**
  ···
  list(set(a))
  [x for x in set(a)]
  ···

7. **fun(\*args,\*\*kwargs)中的\*args,\*\*kwargs什么意思**
  当不知道要传多少参数的时候使用
  args: 非键值对参数
  kwargs: 键值对参数

8. **python2和python3中range(100)的区别**
  python2返回列表,python3中返回一个迭代器,节省内存

9. **一句话解释什么样的语言可以使用装饰器**
  函数可以作为参数传递的语言

10. **python的内建数据类型**
  bool 
  int
  str
  list
  dict
  tuple

11. **面向对象中__new__,__init__的区别**
   __init__是初始化方法,类似构造函数,在对象创建的时候即被调用
   __new__至少要有一个参数cls，代表当前类，此参数在实例化时
   由Python解释器自动识别,且需要返回实例的对象

12. **with方法的作用**
   with方法可以实现close函数

13. **列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]**
   ```
   a = [1,2,3,4,5]
   b = map(lambda x: x**x, a)
   res = [x for x in map if x > 10]
   ```

14. **python中生成随机整数、随机小数、0--1之间小数方法**
   - 随机整数: random.randint(0,n)
   - 随机小数: np.random.randn(5)
   - 0--1随机小数: random.random()

15. **避免转义给字符串加哪个字母表示原始字符串？**
   r'string'

16. **<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的**
   ```
   str1 = '<div class="nam">中国</div>'
   str2 = '<div class=".*">(.*?)</div>'
   res = re.findall(r'str2', str1)
   ```

17. **python中断言方法举例**
   assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错

18. **python2和python3区别？列举5个**
   1. py2 print是关键字 py3中是函数
   2. range(100) p2中返回列表,py3中返回一个迭代器
   3. py2中 raw_input() py3中 input()

19. 列出Python中的可变数据类型和不可变数据类型
	- 不可变:数值型,字符串,元祖
		如果改变值则相当于新建了一个对象,可以用id()查看
	- 可变:list,dict
  
20. s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
	```
	s = "ajldjlajfdljfddd"
	s = set(s)
	s = list(s)
	s.sort()
	res = "".join(s)
	```

21. 用lambda函数实现两个数相乘
	```
	sum = lambda x,y:x+y
	sum(1,2)
	```

22. 字典根据键从小到大排序
	```
	dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
	list = sorted(dict.items(),key=lambda i:i[0],reverse=False)
	new_dict = {}
	for i in list:
		new_dict[i[0]] = i[1]
	```
	
23. 利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
   ```
   from collections import Counter
   a = 'asdasdasdwdasdasdasdw'
   res = Counter(a)
   ​````
   ```

24. 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
	```
	import re
	a = "not 404 found 张三 99 深圳"
	list = a.split(' ')
	res = re.findall('\d+\.?\d*|[a-zA-Z]+',a)
	for i in list:
		if i in res:
			list.remove{i}
	new_str = "".join(list)
	```

25. filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	```
	a = [x for x in range(1,11)]
	b = filter(lambda x:x%2 ==1,a)
	new_a = [x for x in b]
	```

26. 列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	```
	[x for x in a if x%2 == 1]
	```

27. 正则re.complie作用
	将正则表达式编译成一个对象,加快速度,提高复用

28. a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
	- a=(1,)  元组
	- b = (1)  int
	- c = ("1")  str
	
29. 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
	```
	a.extend(b)
	a.sort()
	```
	
30. 用python删除文件
	```
	os.remove(文件名)
	```

31. log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
	```
	datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	datetime.datetime.now().isoweekday()  # 星期
	```

32. 数据库优化查询方法
	外键、索引、联合查询、选择特定字段等等
	
33. 请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
	pychart、matplotlib
	
34. 写一段自定义异常代码
	自定义异常用raise抛出异常

35. 正则表达式匹配中，（.*）和（.*?）匹配区别？
	（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
	（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
	
36. 简述Django的orm
	```
	orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，如果数据库迁移，只需要	  更换Django的数据库引擎即可
	```
	
37. [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
	```
	[j for i in a for j in i]
	```

38. x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
	join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致

39. 举例说明异常模块中try except else finally的相关意义
	try..except..else没有捕获到异常，执行else语句
	try..except..finally不管是否捕获到异常，都执行finally语句

40. python中交换两个数值
	```
	a,b = b,a
	```

41. 说明zip（）函数用法
	zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。同时将这些序列中并排的元素配对。

	zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组。

42. a="张明 98分"，用re.sub，将98替换为100
	```
	import re
	a = "张明 98分"
	ret = re.sub(r'\d+', "100", a)
	```

43. a="hello"和b="你好"编码成bytes类型
	```
	a = b"hello"
	b = "你好".encode()
	```

44. [1,2,3]+[4,5,6]的结果是多少？
	相当于extend()

45. 提高python运行效率的方法
	1、使用生成器，因为可以节约大量内存
	2、循环代码优化，避免过多重复代码的执行
	3、核心模块用Cython  PyPy等，提高效率
	4、多进程、多线程、协程
	5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率

46. 简述mysql和redis区别
	redis： 内存型非关系数据库，数据保存在内存中，速度快
	mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢

47. list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
	利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作

48. 写一个单列模式
49. 保留两位小数
	round(float(a),2)

50. 列出常见的状态码和意义
	```
	200 OK 
    请求正常处理完毕

    204 No Content 
    请求成功处理，没有实体的主体返回

    206 Partial Content 
    GET范围请求已成功处理

    301 Moved Permanently 
    永久重定向，资源已永久分配新URI

    302 Found 
    临时重定向，资源已临时分配新URI

    303 See Other 
    临时重定向，期望使用GET定向获取

    304 Not Modified 
    发送的附带条件请求未满足

    307 Temporary Redirect 
    临时重定向，POST不会变成GET

    400 Bad Request 
    请求报文语法错误或参数错误

    401 Unauthorized 
    需要通过HTTP认证，或认证失败

    403 Forbidden 
    请求资源被拒绝

    404 Not Found 
    无法找到请求资源（服务器无理由拒绝）

    500 Internal Server Error 
    服务器故障或Web应用故障

    503 Service Unavailable 
    服务器超负载或停机维护
	```

51. 分别从前端、后端、数据库阐述web项目的性能优化
	```
	前端优化：
    1、减少http请求、例如制作精灵图
    2、html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差

    后端优化：
    1、缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。
    2、异步方式，如果有耗时操作，可以采用异步，比如celery
    3、代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况

    数据库优化：
    1、如有条件，数据可以存放于redis，读取速度快
    2、建立索引、外键等
	```

52. 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
	```
	dic = {'name':'wang','age':18}
	dic.pop('age')
	del dic['name']
	```

53. 列出常见MYSQL数据存储引擎
	innoDB
	MyISAM
	MEMORY

54. 简述同源策略
	```
	 同源策略需要同时满足以下三点要求： 
    1）协议相同 
    2）域名相同 
    3）端口相同 
     http:www.test.com与https:www.test.com 不同源——协议不同 
     http:www.test.com与http:www.admin.com 不同源——域名不同 
     http:www.test.com与http:www.test.com:8081 不同源——端口不同
     只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”
	```

55. 简述cookie和session的区别
	1，session 在服务器端，cookie 在客户端（浏览器）
    2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
    3、cookie安全性比session差
    
56. 简述多线程、多进程
	```
	进程：
    1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
    2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制

    线程：
    1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
    2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃

    应用：
    IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间
    CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，其他线程没有GIL，就不能充分利用多核CPU的优势
	```

57. 简述any()和all()方法
	any():只要迭代器中有一个元素为真就为真
    all():迭代器中所有的判断项返回都是真，结果才为真
    python中什么元素为假？
    答案：（0，空字符串，空列表、空字典、空元组、None, False)

58. IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
	```
	IOError：输入输出异常
    AttributeError：试图访问一个对象没有的属性
    ImportError：无法引入模块或包，基本是路径问题
    IndentationError：语法错误，代码没有正确的对齐
    IndexError：下标索引超出序列边界
    KeyError:试图访问你字典里不存在的键
    SyntaxError:Python代码逻辑语法出错，不能执行
    NameError:使用一个还未赋予对象的变量
	```

59. python中copy和deepcopy区别
	```
	1、复制不可变数据类型，不管copy还是deepcopy,都是同一个地址当浅复制的值是不可变对象（数值，字符串，元组）时和=“赋值”的情况一样，对象的id值与浅复制原来的值相同。

	2、复制的值是可变对象（列表和字典）
    浅拷贝copy有两种情况：
    第一种情况：复制的 对象中无 复杂 子对象，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。原来值的id值与浅复制原来的值不同.
    第二种情况：复制的对象中有 复杂 子对象 （例如列表中的一个子元素是一个列表）， 改变原来的值 中的复杂子对象的值  ，会影响浅复制的值。
    深拷贝deepcopy：完全复制独立，包括内层列表和字典
	```

60. 列出几种魔法方法并简要介绍用途
	```
	__init__:对象初始化方法
    __new__:创建对象时候执行的方法，单列模式会用到
    __str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    __del__:删除对象执行的方法
	```

61. 请将[i for i in range(3)]改成生成器
	生成器是特殊的迭代器，
    1、列表表达式的【】改为（）即可变成生成器
    2、函数在返回值得时候出现yield就变成生成器，而不是函数了；
    
62. a = "  hehheh  ",去除收尾空格
	a.strip()

63. 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
	list.sort()
	sorted(list,reverse=False)

64. 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
	a = sorted(foo,key=lambda x:x)

65. 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
	a = sorted(foo, key=lambda x:(x<0,abs(x)))

66. 列表嵌套字典的排序，分别根据年龄和姓名排序
	```
	foo = [{"name":"zs","age":19},{"name":"ll","age":54},
        {"name":"wa","age":17},{"name":"df","age":23}]
    a = sorted(foo, key=lambda x:x['age'])
    a = sorted(foo, key=lambda x:x['name'])
	```

67. 列表嵌套元组，分别按字母和数字排序
	a=sorted(foo,key=lambda x:x[1])

68. 列表嵌套列表排序，年龄数字相同怎么办？
	a = sorted(foo,key=lambda x:(x[1],x[0]))

69. 根据键对字典排序（方法一，zip函数）
	1. 字典转列表嵌套元祖
		foo = zip(dic.keys(),dic.values())
	2. 字典嵌套元组排序
	3. 排序完构造新的字典

70. 根据键对字典排序（方法二,不用zip)
	方法相同
	foo = dic.items()

71. 列表推导式、字典推导式、生成器
	列表推导式: [i for i in range(10)]
	字典推导式: {k:"1",for k in range(10)}
	生成器: (i for i in range(11))


72. 根据字符串长度排序
	```
	s = ['dwdasd','cgrses','wwsdgr','hgtts']
	b = sorted(s, key=lambda x : len(x))
	```

73. python字典和json字符串相互转化方法
	json.dumps()字典转json字符串，json.loads()json转字典





































