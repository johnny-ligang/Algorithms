# git order

### git init  
    变成git可管理的仓库

### git clone  

### git status  
    查看状态

### git add  
    git add readme.md  加单个文件  
    git add -A  加全部文件

### git commit -m "commit"  
    提交修改，需要加评论

### git pull

### git push  
    提交至远程仓库

### git log  
    查看日志

### .gitignore
    在git工程下根目录下增加文件 <.gitignore> ，文件中写入不需要提交到git远程目录的文件夹和文件，可以模糊匹配

### 解决冲突
#### 冲突一：
版本落后，无法push  
方法1:需要先在push前将本地resposiory先pull下来  
git pull origin master  
git push -u origin master  

方法2:强制push，会修改远程文件，不可取  
git push -u origin master -f

方法3:新建分支，然后push  
git branch [new-branch]  
git push -u origin [new-branch]

