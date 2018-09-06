# requirements-demo
这是一个包管理方案demo，使用pip + requirements.txt。
1. 所有包信息存在requirements.txt中
2. 执行requirements_install.py会安装requirements.txt中的所有依赖（非pip的包会略过）
3. 执行requirements_gen.py会生成一份pip requirements存在requirements.txt.current中
4. 执行requirements_clean会清理所有不在requirements.txt中的包，并执行一次requirements_install
5. 可将requirements文件夹拷贝至任意工程中使用
