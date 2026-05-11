import getListStudents from "./0-get_list_students.js";


export default function getStudentIdsSum(StudntId) {
	if (!Array.isArray(StudntId))
		return []

	return StudntId.reduce((acc, curr) =>
		acc += curr.id
		, 0)

}