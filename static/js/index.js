let name_input = document.getElementById('id_name')
name_input.placeholder = 'Task name here...'
let description = document.getElementById('id_summary')
description.placeholder = 'Description'

let names = document.getElementsByClassName('name')
let contador = document.getElementById('contador').innerHTML = names.length
let important_tasks = document.getElementsByClassName('name-important')
document.getElementById('total-important').innerHTML = important_tasks.length

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
	importants.className = 'option p-6 bsm:p-4 border-b-2 border-purple-700'
	document.getElementById('task-list-important').style.display = 'block'
}
function tasks() {
	document.getElementById('task-list-important').style.display = 'none'
	document.getElementById('task-list').style.display = 'block'
	let options = document.getElementsByClassName('option')
	Array.from(options).forEach(element => {
		element.classList.replace('border-b-2', 'border-none')
	})
	let tasks = document.getElementById('tasks')
	tasks.className = 'option p-6 bsm:p-4 border-b-2 border-purple-700'	
}