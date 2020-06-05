class TasksApi {

    async list() {
        let options = {
            method: 'GET'
        };
        try {
            let response = await fetch('/api/tasks', options);
            let data = await response.json();
            return data;
        } catch (err) {
            console.log(err);
            return null;
        }
    }

    async add(task) {
        let options = {
            method: 'POST',
            body: JSON.stringify(task)
        };
        try {
            let response = await fetch('/api/tasks', options);
            let data = await response.json();
            return data;
        } catch (err) {
            console.log(err);
            return null;
        }
    }

}

export default TasksApi;