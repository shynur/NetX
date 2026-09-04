## Brief

一个 NetX 网络就是一个无向连通图.

## Edge

NetX node 之间的 edge 是双向的.

### 基于 WebSocket の edge

任何 node 可以主动监听 WebSocket 连接.

If a node 向 another node which is listening WebSocket 发起连接, 则 these two nodes 之间连通.

### 基于 HTTP (POST / SSE) の edge

任何 node 可以主动监听 HTTP 连接.

If a node 向 another node which is listening HTTP 发起连接, 则 these two nodes 之间连通.
The node which is listening HTTP 会使用 SSE 建立持久连接, 而对方 node 会使用 HTTP POST 发送数据.
