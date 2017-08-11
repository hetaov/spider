'use strict';

let fs = require('fs');

let obj;

fs.readFile('data/word/components_word_new.json', 'utf-8', (err, data) => {
	if(err) {
		console.log('err---------------->')
		console.log(err);
		return;
	}

	console.log('start ---------------->')
	console.log(data)
	console.log('end ---------------->')

	let result = eval(data);
	console.log(result.length)
})
