
使用说明
================


一、文档撰写前提
~~~~~~~~~~~~~~~~

.. note:: 

  Sphinx组件安装： 

  .. code-block:: console 

    pip install sphinx recommonmark sphinx-autobuild sphinx_rtd_theme -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com


二、源代码的使用方法
~~~~~~~~~~~~~~~~~~~~~~

1. 在 Gitee 中创建一个仓库，名字随意（这里仓库名字以用 notebook 举例）
      
  .. image:: ../../images/001.png
    :width: 200px

2. 克隆 notebook 仓库到本地随意一个位置
  
  .. code-block:: console
    
    git clone https://gitee.com/zhyantao/notebook.git

3. 下载 readthedocs 仓库的 `源代码 <https://gitee.com/zhyantao/readthedocs/repository/archive/master.zip>`_ ，解压后将文件夹中的内容复制到 notebook 文件夹下
  
  .. image:: ../../images/003.png

4. 将 notebook 文件夹下的文件提交到远程仓库
  
  .. code-block:: console
    
    git add . && git commit -m "notebook" && git push origin master

  .. image:: ../../images/004.png

5. 登录 Read the Docs 导入刚刚创建的代码仓库 notebook （这里选择手动导入）
  
  .. image:: ../../images/005-1.png
  .. image:: ../../images/005-2.png

6. 选择 Build Version ，构建完成后即可阅读文档了。

  .. image:: ../../images/006.png

7. 到现在，基本的框架搭建完了。后面就可以把自己想要写的内容填充到博客中了。


三、撰写博文并发表
~~~~~~~~~~~~~~~~~~~~~~

8. 把需要发表的文档放在 notebook/source/docs 文件夹中（写作格式可以是 Markdown 或者 reStructuredText）
9. 打开 CMD 切换到 notebook 目录下，输入 ``make html`` 
10. 打开 notebook/build/index.html 预览效果，确认无误后提交代码到 Gitee 仓库
  
  .. code-block:: console
    
    git add . && git commit -m "notebook" && git push origin master

11. 重新打开 Read the Docs 文档的网址，查看新发表的博客（有延迟，可能需要等待）。


.. warning::
  除了 *notebook/source/docs* 下的文件和 *source/index.rst* 可以修改外，其他位置的文件不要修改，否则可能会引起错误。另外，**务必在 source/index.rst 文件中添加你的博文的路径**
