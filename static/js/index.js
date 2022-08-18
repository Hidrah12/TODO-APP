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

function importants() {
	document.getElementById('task-list').style.display = 'none'
	let options = document.getElementsByClassName('option')
	Array.from(options).forEach(element => {
		element.classList.replace('border-b-2', 'border-none')
	})
	let importants = document.getElementById('importants')
	importants.className = 'option p-6 border-b-2 border-purple-700'
}
function tasks() {
	document.getElementById('task-list').style.display = 'block'
	let options = document.getElementsByClassName('option')
	Array.from(options).forEach(element => {
		element.classList.replace('border-b-2', 'border-none')
	})
	let tasks = document.getElementById('tasks')
	tasks.className = 'option p-6 border-b-2 border-purple-700'	
}