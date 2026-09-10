export function helloMessage() {
	console.error(`[info] ${helloMessage.name} called ${++cnt} times`)

	return {
		author: 'shynur',
		message: 'Hello, NetX!',
	}
}

let cnt = 0
