'use strict';

let json2csv = require('json2csv')

let fs = require('fs');

let fields = ['name', 'description']

let obj;

fs.readFile('data/word/components_word_chinese.json', 'utf-8', (err, data) => {
	if(err) {
		console.log('err---------------->')
		console.log(err);
		return;
	}

	console.log('start ---------------->')
	console.log(data)
	console.log('end ---------------->')

	let result = eval(data);

	let csv = json2csv({
		data: result, fields: fields
	})
	console.log(result.length)

	fs.writeFile('data/word/components_word_chinese_n.csv', csv, (err) => {
		if (err) throw err;

		console.log('file write successful')

	})
})
