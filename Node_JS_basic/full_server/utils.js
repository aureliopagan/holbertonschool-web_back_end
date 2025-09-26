const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      if (students.length === 0) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const fields = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (field) {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }
      });

      resolve(fields);
    });
  });
}

module.exports = readDatabase;