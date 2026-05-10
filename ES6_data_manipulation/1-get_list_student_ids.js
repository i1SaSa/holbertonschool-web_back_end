export default function getListStudentIds(StdntId) {
	if (!Array.isArray(StdntId)) {
		return [];
	}

	return StdntId.map((student) => student.id);
}