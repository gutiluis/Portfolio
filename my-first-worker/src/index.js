/**
 * Welcome to Cloudflare Workers! This is your first worker.
 * Entry point for the cloudflare worker
 * - Run `npm run dev` in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

export default {
	// fetch is a handler called when the worker receives an http request //
	// fetch will always have the 3 parameters. is a Fetch API//
	// To return a request parameter respond with a response object //
	async fetch(request, env, ctx) {
		return new Response('Hello Worker!');
	},
};


// the worker is acting like a proxy forwarding the request to example.com and returning a real response //
// how to modify a request object. because the reques object is immutable //
/*
export default {
	async fetch(request, env, ctx) {
		const url = "https://example.com";
		const modifiedRequest = new Request(url, request);
		const response = await fetch(modifiedRequest);
	    return response;
	},
};
*/