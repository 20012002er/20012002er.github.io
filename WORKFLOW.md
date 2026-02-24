# WORKFLOW.md - 工作习惯和规则

## 浏览器使用规则

**任务完成后务必清理浏览器资源：**

1. **每次使用浏览器执行任务后，自动关闭所有打开的tab**
   - 查询任务（如查机票、新闻等）
   - 信息收集任务
   - 任何临时性浏览任务

2. **执行步骤：**
   ```bash
   # 查看当前打开的tabs
   browser action=tabs
   # 关闭所有tabs
   browser action=close targetId=<每个tab的ID>
   # 确认已清空
   browser action=tabs
   ```

3. **为什么这样做：**
   - 节省服务器资源（内存、CPU）
   - 避免后台进程累积
   - 保持系统整洁

## 其他规则

（待补充）
