const express = require('express');
const mongoose = require('mongoose');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

mongoose.connect('mongodb://localhost:27017/mydatabase', { 
	useNewUrlParser: true, 
	useUnifiedTopology: true
}).then(() => {
	console.log('MongoDB connected successfully');
}).catch(err => {
	console.error('MongoDB connection error:', err);
});

const DataSchema = new mongoose.Schema({
	name: String,
	value: String
});

const Data = mongoose.model('Data', DataSchema);

app.get('/data', async (req, res) => {
	const data = await Data.find();
	res.json(data);
});

app.post('/data', async (req, res) => {
	const newData = new Data({ 
		name: req.body.name,
		value: req.body.value
	});
	try{
		await newData.save();
		console.log('Data saved successfully:', JSON.stringify(newData, null, 2));
		res.send('Data saved successfully');
	} catch (error) {
		console.error('Error saving data:', error);
		res.status(500).send('Error saving data');
	}
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);

});

