<template>
  <div class="hello page">
    <div class="holder">
        <form @submit.prevent="addTask">
          <input class="taskinput" type="text" placeholder="Enter a task.." v-model="task" name="task">
        </form>
        <ul>
            <div class="li-container" v-for="(data, index) in tasks" :key="index">
              <div class="list-item" v-if="editing != index">
              <li>{{data.task}}</li>
              <i class="fa fa-edit" v-on:click="editing = index; edittext = tasks[index].task"></i>
              <i class="fa fa-check" v-on:click="completeTask(index)"></i>
              <i class="fa fa-times" v-on:click="remove(index)"></i>
              </div>
              <div v-if="editing == index" class="editingdiv">
                <input type="text" placeholder="Enter a task.." v-model="edittext" v-on:keyup.enter="editTask(index)" name="edit">
                <div @click="editTask(index)"> save </div>
              </div>
            </div>
        </ul>
      <p> {{ tasks.length > 0 ? 'Looks Like You Have Some Task To Do' : 'Such Empty Much Wow'  }} </p>
    </div>
  </div>
</template>

<script>

const baseurl = 'http://localhost:5000/api/tasker/'

import axios from 'axios';

export default {
  name: 'Tasker',
  data() {
    return {
      userid: this.$parent.userhash,
      task: '',
      editing: -1,
      edittext: '',
      tasks: [],
      debug: ''
    }
   },
    methods: {
      getAll() {
        this.debug = axios.get(baseurl + this.userid + '?status=todo').then(response => {
          var data = response.data;
          this.tasks = []
          for (let index = 0; index < data.length; index++) {
          var task_dict = data[index];
          this.tasks.unshift(task_dict);
      }
      })
    },

    addTask() {
          this.debug = axios.post(baseurl + this.userid, {completed: false, task: this.task}).then( response => {
            var data = response.data;
            this.tasks.unshift(data);
            this.task = '';
          })
    },

    completeTask(index) {
      const blacklist = ['timestamp'];
      var dict = this.tasks[index];
      var updated_task = {}

      for (const key in dict) {
        if (!(key in blacklist)) {
          const value = dict[key];
          updated_task[key] = value
        }
      }

      updated_task.completed = true;

      this.debug = axios.put(baseurl + this.userid, updated_task)
      this.tasks.splice(index, 1)
    },

    editTask(index) {
      const blacklist = ['timestamp'];
      var dict = this.tasks[index];
      var updated_task = {}

      for (const key in dict) {
        if (!(key in blacklist)) {
          const value = dict[key];
          updated_task[key] = value
        }
      }

      updated_task.task = this.edittext;

      this.debug = axios.put(baseurl + this.userid, updated_task).then(response => {
      var data = response.data;
      this.tasks.splice(index, 1, data)
      })

      this.editing = -1;
      this.edittext = '';
    },

     remove(index) {
       var task_id = this.tasks[index].task_id
       axios.delete( baseurl + this.userid + '/' + task_id  )
       this.tasks.splice(index,1);
      }
    },
    created() {
      this.getAll();
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1";
@import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";
  .hello {
    margin: 0;
    padding: 0;
  }
  .holder {
    background: rgb(255, 255, 255);
    width: 80%;
    margin: 0 auto;
  }

  ul {
    margin: 20px 30px;
    padding: 0;
    list-style-type: none;
  }

  .li-container {
    padding: 10px;
    padding-left: 30px;
    padding-right: 5px;
    border-radius: 40px;
    margin-bottom: 5px;
    background-color:#006666;
  }

  .list-item {
    display: flex;
    flex-direction: row;
    align-items: baseline;
  }

  .list-item li {
    overflow: hidden;
    color: white;
    margin-top: auto;
    margin-bottom: auto;
    margin-right: auto;
  }

  i {
  align-self: flex-end;
  padding: 10px;
  margin: 0 5px;
  border-radius: 50%;
  font-size: 2em;
  cursor:pointer;
  color: white;
  }


  .fa-check {
    background-color: #00ff6a;
  }
  .fa-times {
    padding: 10px 14px;
    background-color: rgb(255, 50, 70);
  }

  ul li {
    font-size: 1.4rem;
  }

  .editingdiv {
    display: flex;
    justify-content: flex-start;
    align-items: baseline;
    font-size: 1.4rem;
    color: white;
  }

  .editingdiv div {
    background-color: rgb(245, 245, 245);
    border-radius: 40px;
    color: rgb(70, 70, 70);
    padding: 5px 15px;
    margin-right: 15px;
    font-weight: 500;
  }

  .editingdiv input[type=text] {
    border: 0;
    padding: 10px 30px;
    padding-left: 10px;
    font-size: 1.4rem;
    width: calc(100% - 150px);
    background-color: #006666;
    color: #fff;
    font-weight: 300;
  }

  p {
    text-align:center;
    font-size: 1.1em;
    padding: 40px 0px;
    color: rgb(56, 56, 56);
  }

  .taskinput {
    width: calc(100% - 60px);
    border: 0;
    padding: 20px 30px;
    font-size: 1.3em;
    background-color: #004646;
    color: rgb(213, 214, 214);
  }

</style>