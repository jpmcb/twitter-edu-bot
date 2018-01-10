// John McBride - Jan 05 2017
// -------
// Server file for the front end of the educational twitter bot

// Testing environment port
var port = process.env.PORT || 8080;

// The node mongo client 
var mongo = require('mongodb').MongoClient;

// The database name
const dbName = "heroku_wwpzkm46";

var importCred = require('./credentials.json');

// Local environment port
var url = importCred.database + dbName;


// -----------------------
// variables and constants for the express 
// -----------------------

const express = require('express');
const app = express();
app.set('view engine', 'ejs');

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
	extended: true
}));

// For the path to the public folder in the express fild tree
app.use(express.static(__dirname + '/public'));


// -----------------------
// Generates the database for the twitter handles
// and classes the students are taking
// -----------------------

var createDB = function() {
	mongo.connect(url, function(err, client) {
		if (err) throw err;

		// create the twitter handle collection
		var db = client.db(dbName);
		db.createCollection("twitter_handles", function(err, res) {
			if (err) throw err;
			console.log("Collection created!");
			client.close();
		});
	});
}


// ---------------------
// Places a new twitter handle and enrolled class as specified by the user
// ---------------------

var insertUser = function(first_name, last_name, handle, enrolled) {
	mongo.connect(url, function(err, client) {
		if (err) throw err;

		var insert = {
			handle: handle,
			first_name: first_name,
			last_name: last_name,
			enrolled: enrolled }

		var db = client.db(dbName);
		db.collection("twitter_handles").insertOne(insert, function(err, res) {
			if (err) throw err;
			console.log("User registered in database!");
			client.close();
		});
	});
}

// -------------------
// Finds and returns all instances of the enrollments that students are in
// -------------------

var findClass = function(enrolled, callback) {
	mngo.connect(url, function(err, client) {
		var db = client.db(dbName);

		if (err) {
			console.log(enrolled + " class dose not exist!");
			client.close();
		} else {
			db.collection("twitter_handles").find( {enrolled: enrolled} ), function(err, result) {
				if (err) throw err;
				client.close();

				callback(result);
			}
		}
	});
}

// -----------------
// Finds and returns the twitter handle for a specific name
// -----------------

var findHandle = function(first_name, last_name) {
	mongo.connect(url, function(err, client) {
		var db = client.db(dbName);

		if (err) {
			console.log(first_name + " " + last_name + " could not be found!");
			client.close();
		} else {
			db.collection("twitter_handles").findOne( {first_name: first_name, last_name: last_name} ), function(err, result) {
				if (err) throw err;
				client.close();

				callback(result);
			}
		}
	})
}

// --------------
// --------------
// Server code for the front end
// --------------
// --------------

createDB();

app.get('/', function(req, res) {
	res.render('home');
});

app.listen(port, function() {
	console.log('Listening on port 8080');
});

app.post('/register', function(req, res) {
	console.log('User attempting to register ...');

	console.log(req.body);
	insertUser((req.body.first_name), (req.body.last_name), (req.body.handle), (req.body.enrolled));

	res.render('registered');
});