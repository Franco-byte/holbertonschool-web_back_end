const fd = require('fs').promises;

async function countStudents(path) {
    try {
        const data = await fd.readFile(path, 'utf8');
        const lines = data.split('\n').filter(line => line.trim() !== '');

        const students = lines.slice(1);
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

        console.log(`Number of students: ${students.length}`);
        for (const field in fields) {
            console.log(
                `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
            );
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
};

module.exports = countStudents;