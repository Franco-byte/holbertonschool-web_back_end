const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1); // Saltamos la cabecera

    const fields = {};

    for (const line of students) {
      const parts = line.split(',');
      const firstName = parts[0];
      const field = parts[3];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstName);
    }

    // Construimos el string que espera el checker
    let output = `Number of students: ${students.length}`;
    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        output += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
      }
    }

    return output;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
