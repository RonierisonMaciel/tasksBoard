for (let but of document.querySelectorAll('.task')) {
    but.addEventListener('click', () => {
        const value = but.value
        const modal = document.querySelector('#editform > div > div')
        const taskId = document.createElement("input")
        taskId.type = 'hidden'
        taskId.value = value
        taskId.id = 'id'
        taskId.name = 'id'
        if (modal.querySelector('#id')) {
            const newTaskId = modal.querySelector('#idzz')
            newTaskId.value = value
        } else {
            modal.appendChild(taskId)
        }
    })
}
