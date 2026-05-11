export default function getStudentsByLocation(Student, city) {
	if (typeof city !== 'string')
		throw TypeError(`${city} Must be a String`)
	if (!Array.isArray(Student)) {
		return [];
	}


	return Student.filter((student) => (student.location == city))

}