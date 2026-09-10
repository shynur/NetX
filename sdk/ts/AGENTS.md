## 双 runtime

- 尽可能只使用标准 API (`fetch`, `WebSocket`, `EventSource`, etc.), 尤其是那些在 Node.js 与浏览器中均有实现的.
- `node:*` 内置模块在浏览器中不可用; DOM API 在 server 侧未必存在.  涉及此类 API 时需按 runtime 分别处理.
- Server 侧的 WebSocket server 暂时需要依赖 3rd party package.
