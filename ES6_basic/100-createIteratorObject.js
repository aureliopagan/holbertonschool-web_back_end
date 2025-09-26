export default function createIteratorObject(report) {
    const employees = report.allEmployees;
    
    return {
      * [Symbol.iterator]() {
        for (const department of Object.values(employees)) {
          for (const employee of department) {
            yield employee;
          }
        }
      }
    };
  }