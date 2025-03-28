export default class HolbertonCourse {
  constructor(name, length, student) {
    this.name = name;
    this.length = length;
    this.student = student;
    }

  get name() {
    return this._name;
  }
  set name(value) {
    if (typeof value !== "string") {
      throw new Error("The name must be a string.");
    }
    this._name = value;
  }

  get length() {
    return this._length;
  }
  set length(value) {
    if (typeof value !== "number") {
        throw new Error("The length must be a number.");
    }
    this._length = value;
  }

  get student() {
    return this._student;
  }
  set student(value) {
    if (typeof value !== "string" && !Array.isArray(value)) {
        throw new Error("The student/s must be a string or an array.")
    }
    this._student = value;
  }
}
