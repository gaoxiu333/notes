Mac 修改Hosts

```bash
# 修改 hosts
sudo nano /etc/hosts
# 刷新DNS（macOS Sonoma）
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

> 网上找到方法，但是设置失败～
