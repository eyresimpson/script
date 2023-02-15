# 使用官方的 jenkins/jenkins 镜像作为基础镜像
FROM jenkins/jenkins

# 使用 root 身份执行命令
USER root

# 安装 Python3，Git，Maven 等依赖工具
RUN apt-get update && apt-get install -y python3 python3-pip git maven

# 指定 Jenkins 的端口为 8080 和 50000
EXPOSE 8080 50000

# 指定 Jenkins 的数据卷为 /var/jenkins_home
VOLUME /var/jenkins_home