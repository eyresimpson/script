# 使用官方的 gitlab/gitlab-ce 镜像作为基础镜像
FROM gitlab/gitlab-ce

# 指定 Gitlab 的端口为 80，443，22
EXPOSE 80 443 22

# 指定 Gitlab 的数据卷为 /etc/gitlab，/var/log/gitlab，/var/opt/gitlab
VOLUME ["/etc/gitlab", "/var/log/gitlab", "/var/opt/gitlab"]
