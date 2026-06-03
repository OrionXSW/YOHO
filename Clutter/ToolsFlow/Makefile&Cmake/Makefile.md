***makefile***

---

# Makefile
参考《跟我一起写Makefile》
## 介绍
makefile带来的好处是“自动化编译”,一旦写好，只需一个make命令，整个工程完全自动编译，极大提高软件开发效率
make是一个命令工具，是一个解释makefile中指令的命令工具，大多数的IDE都有这个命令，比如Linux下GNU的make,makefile成了一种在工程方面的编译方法
一般来说，无论是 C 还是 C++，首先要把源文件编译成中间代码文件，在 Windows 下也就是 .obj 文件，UNIX 下是 .o 文件，即 Object File，这个动作叫做编译（compile）。然后再把大量的 Object File 合成执行文件，这个动作叫作链接（link）。
编译时，编译器需要的是语法的正确，函数与变量的声明的正确。
链接时，主要是链接函数和全局变量
总结一下，源文件首先会生成中间目标文件，再由中间目标文件生成执行文件。
注释符号是 # 

## 核心规则(makefile的主线和核心)
```
target ... : prerequistites ...
    command
    ...
    ...
```
target(目标)可以是一个 object file（目标文件），也可以是一个执行文件，还可以是一个标签（label）。对于标签这种特性，在后续的“伪目标”章节中会有叙述。
prerequisites(依赖文件)生成该 target 所依赖的文件集合 或 target集合
command 该 target 要执行的命令（任意的 shell 命令）

**依赖关系的实质就是说明了目标文件是由哪些文件生成的，换言之，目标文件是哪些文件更新的。**
在定义好依赖关系后，后续的那一行定义了如何生成目标文件的操作系统命令，一定要以一个 Tab键作为开头

这是一个文件的依赖关系，也就是说，target 这一个或多个的目标文件依赖于 prerequisites 中的文
件，其生成规则定义在 command 中。说白一点就是说**prerequisites 中如果有一个以上的文件比 target 文件要新的话，command 所定义的命令就会被执行。**
记住，make 并不管命令是怎么工作的，他只管执行所定义的命令。make 会比较 targets 文件和 prerequisites 文件的修改日期，如果 prerequisites 文件的日期要比targets 文件的日期要新，或者target 不存在的话，那么，make 就会执行后续定义的命令

## 变量
```
edit : main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o
    cc -o edit main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o
```
我们可以看到 .o 文件的字符串被重复了两次，如果我们的工程需要加入一个新的 .o 文件，那么我们需要在两个地方加（应该是三个地方，还有一个地方在 clean 中）。如果 makefile 变得复杂，那么我们就有可能会忘掉一个需要加入的地方，而导致编译失败。所以，为了 makefile 的易维护，在 makefile 中我们可以使用变量。makefile 的变量也就是一个字符串，理解成 C 语言中的宏可能会更好

比如，我们声明一个变量，叫 objects ，OBJECTS ，objs ，OBJS ，obj 或是 OBJ ，不管什么,只要能够表示 obj 文件就行了。我们在 makefile 一开始就这样定义：
```
objects = main.o kbd.o command.o display.o \
    insert.o search.o files.o utils.o
edit : $(objects)
    cc -o edit $(objects)
.
.
.
clean :
    rm edit $(objects)
```

## make有自动推导的特性
GNU 的 make 很强大，它可以自动推导文件以及文件依赖关系后面的命令，于是我们就没必要去在每一个 .o 文件后都写上类似的命令，因为，我们的 make 会自动识别，并自己推导命令。只要 make 看到一个 .o 文件，它就会自动的把 .c 文件加在依赖关系中，如果 make 找到一个whatever.o ，那么 whatever.c 就会是 whatever.o 的依赖文件。并且 cc -c whatever.c 也会被推导出来，于是，我们的 makefile 再也不用写得这么复杂。我们的makefile 又出炉了。
```
objects = main.o kbd.o command.o display.o \
    insert.o search.o files.o utils.o
edit : $(objects)
    cc -o edit $(objects)
main.o : defs.h
kbd.o : defs.h command.h
command.o : defs.h command.h
display.o : defs.h buffer.h
insert.o : defs.h buffer.h
search.o : defs.h buffer.h
files.o : defs.h buffer.h command.h
utils.o : defs.h
.PHONY : clean
clean :
    rm edit $(objects)
```
这种方法，也就是 make 的“隐晦规则”。上面文件内容中，.PHONY 表示 clean 是个伪目标文件.

## 清空目标文件的规则
每个 Makefile 中都应该写一个清空目标文件（.o 和执行文件）的规则，这不仅便于重编译，也很利于保持文件的清洁。一般的风格都是
```
clean:
    rm edit $(objects)
更为稳健的做法是：
.PHONY : clean
clean :
    -rm edit $(objects)
```
PHONY 表示 clean 是一个“伪目标”。而在 rm 命令前面加了一个小减号的意思就是，也许某些文件出现问题，但不要管，继续做后面的事。。当然，clean 的规则不要放在文件的开头，不然，这就会变成 make 的默认目标，相信谁也不愿意这样。不成文的规矩是——“clean 从来都是放在文件的最后”。

## Makefile里的东西
Makefile 里主要包含了五个东西：显式规则、隐晦规则、变量定义、文件指示和注释。

1. 显式规则。显式规则说明了如何生成一个或多个目标文件。这是由 Makefile 的书写者明显指出要
生成的文件、文件的依赖文件和生成的命令。
2. 隐晦规则。由于我们的 make 有自动推导的功能，所以隐晦的规则可以让我们比较简略地书写 Makefile，这是由 make 所支持的。
3. 变量的定义。在 Makefile 中我们要定义一系列的变量，变量一般都是字符串，这个有点像你 C 语言中的宏，当 Makefile 被执行时，其中的变量都会被扩展到相应的引用位置上。
4. 文件指示。其包括了三个部分，一个是在一个 Makefile 中引用另一个 Makefile，就像 C 语言中的include 一样；另一个是指根据某些情况指定 Makefile 中的有效部分，就像 C 语言中的预编译 #if一样；还有就是定义一个多行的命令。
5. 注释。Makefile 中只有行注释，和 UNIX 的 Shell 脚本一样，其注释是用 # 字符，这个就像 C/C++中的 // 一样。如果你要在你的 Makefile 中使用 # 字符，可以用反斜杠进行转义，如：\# 。

### 引用其他的Makefile
在 Makefile 使用 include 关键字可以把别的 Makefile 包含进来，这很像 C 语言的 #include ，被包含的文件会原模原样的放在当前文件的包含位置。include 的语法是：`include <filename>`
在 include 前面可以有一些空字符，但是绝不能是 Tab 键开始。include 和 <filename> **可以用一个或多个空格隔开**。举个例子，你有这样几个Makefile：a.mk 、b.mk 、c.mk ，还有一个文件叫foo.make，以及一个变量 $(bar) ，其包含了 e.mk 和 f.mk ，

## make的工作方式
GNU的make工作时执行步骤如下
1. 读入所有的 Makefile
2. 读入被 include 的其它 Makefile
3. 初始化文件中的变量
4. 推导隐晦规则，并分析所有规则
5. 为所有的目标文件创建依赖关系链
6. 根据依赖关系，决定哪些目标要重新生成
7. 执行生成命令
1-5 步为第一个阶段，6-7 为第二个阶段。第一个阶段中，如果定义的变量被使用了，那么，make 会把其展开在使用的位置。但 make 并不会完全马上展开，make 使用的是拖延战术，如果变量出现在依赖关系的规则中，那么仅当这条依赖被决定要使用了，变量才会在其内部展开。

## 书写规则
> 通配符、伪目标、静态模式规则的思想。重点是理解依赖关系和时间戳判断。

规则包含两个部分，一个是依赖关系，一个是生成目标的方法。
在 Makefile 中，规则的顺序是很重要的，因为，Makefile 中只应该有一个最终目标，其它的目标都是被这个目标所连带出来的，所以一定要让 make 知道你的最终目标是什么。一般来说，定义在 Makefile
中的目标可能会有很多，但是第一条规则中的目标将被确立为最终的目标。如果第一条规则中的目标有
很多个，那么，第一个目标会成为最终的目标。make 所完成的也就是这个目标。

看得脑壳痛，直接跳Cmake了