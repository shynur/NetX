# NetX TypeScript/ECMAScript SDK

同时支持 server (Node.js) 与 browser 两种 runtime.
浏览器中打开的页面也可以成为一个 NetX node (只能主动发起连接).

## 如何在君の项目中接入 SDK

### npm User

#### 从源码 (git submodule)

把本仓库放进君の项目仓库中 (e.g., git submodule 到 `third_party/NetX`), 然后在 `package.json` 中声明依赖:

```json
{
	"dependencies": {
		"netx": "file:third_party/NetX/sdk/ts"
	}
}
```

之后在代码中:

```typescript
import { helloMessage } from 'netx'
```

#### 先 pack 后 install

```bash
# 在当前 TS SDK 下执行
npm install
npm pack
```

然后在君の项目中:

```bash
npm install path/to/netx-0.1.0.tgz
```
