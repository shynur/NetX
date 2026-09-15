## Brief

一个 NetX 网络就是一个无向连通图.

NetX 网络是可以跨网段的.
E.g., 家庭 Wi-Fi 下有一个 NetX 网络, 而公司局域网下有另一个 NetX 网络,
但如果一台公网 server 上也运行了一个 NetX node 而且分别被家庭 Wi-Fi 中的某个 node 和公司局域网中的某个 node 连接,
则这两个 NetX 网络就连通了, 可以统称为一个 NetX 网络.

NetX 网络里随时可能有 新 node 的加入 or 旧 node 的离开 - NetX 网络是动态且去中心化的.

在设计高层通信协议 (e.g., DDS, RPC, etc.) 时, 只关注 NetX 网络的逻辑拓扑结构.
因此, 我们将屏蔽 IP 等实现细节, 假设每个 node 都只知晓相邻 node, etc.

## Edge

NetX node 之间的 edge 是双向的.

新 edge 的建立 (或者说, 新 node 的加入) 采用邀请制.
邀请码就是同一网络下的某个 node 的 IP:port, 这样新 node 才能向这个 node 发起连接.

一个 node 可以被多个 nodes 连接;
一个 node 也可以主动向多个 nodes 发起连接;
node 可以同时是连接的发起方和接收方;
两个 nodes 双方可以互相主动发起连接, 相当于 2 条 edges.

### 基于 WebSocket の edge

任何 node 可以主动监听 WebSocket 连接.

If a node 向 another node which is listening WebSocket 发起连接, 则 these two nodes 之间连通.

### 基于 HTTP (POST / SSE) の edge

任何 node 可以主动监听 HTTP 连接.

If a node 向 another node which is listening HTTP 发起连接, 则 these two nodes 之间连通.
The node which is listening HTTP 会使用 SSE 建立持久连接, 而对方 node 会使用 HTTP POST 发送数据.

## Node

```typescript
class Node {

}
```
