let name_input = document.getElementById('id_name')
name_input.placeholder = 'Task name here...'
let description = document.getElementById('id_summary')
description.placeholder = 'Description'

function addNewTask() {
	let menuTask = document.getElementById('menu-task')
	if (menuTask.classList.toString().includes('invisible')) {
		menuTask.classList.replace('invisible', 'visible')
	} else {
		menuTask.classList.replace('visible', 'invisible')
	}
}
function closeMenuTask() {
	let menuTask = document.getElementById('menu-task')
	if (menuTask.classList.toString().includes('invisible')) {
		menuTask.classList.replace('invisible', 'visible')
	} else {
		menuTask.classList.replace('visible', 'invisible')
	}
}
