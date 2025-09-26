const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Remove header line
      const students = lines.slice(1);

      if (students.length === 0) {
        reject(new Error('Cannot load the database'));
        return;
      }

      console.log(`Number of students: ${students.length}`);

      // Group students by field
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

      // Display students per field
      Object.keys(fields).forEach((field) => {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      });

      resolve();
    });
  });
}

module.exports = countStudents;
