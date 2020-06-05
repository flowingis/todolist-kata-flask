import TaskApi from '../api/TasksApi.js';

const taskApi = new TaskApi();

export default {
    name: 'App',
    template: `
        <div class="container mx-auto p-4">
            <span class="text-2xl mb-2">Elenco Task:</span>
            <hr class="mb-4">
            
            <ul>
                <li v-for="task in tasks">
                    <div>{{task.description}}</div>
                </li>
            </ul>
            
        </div>
    `,
    data: function() {
        return {
            tasks: []
        };
    },
    async mounted() {
          await this.getTasks();
    },
    methods: {
        async getTasks() {
            this.tasks = await taskApi.list();
            console.log(this.tasks);
        }
    }
};