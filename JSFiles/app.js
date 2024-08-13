#!/usr/bin/env node

const http = require('http');
const server = http.createServer((request, response) => {
    response.end('Hello from the server');
    console.log('A new request received');
});

// start the server
server.listen(8000, '127.0.0.1', () => {
    console.log('Server has started');
});