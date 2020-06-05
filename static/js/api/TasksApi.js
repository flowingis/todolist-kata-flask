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
          return null;
        }
    }

}

export default TasksApi;