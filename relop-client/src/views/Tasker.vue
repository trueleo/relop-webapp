<template>
  <div class="hello page">
    <div v-if="isloading" class="loading">
      <div class="logo">
        loading...
      </div>
    </div>
    <div class="holder">
        <form @submit.prevent="addTask">
          <input class="taskinput" type="text" autocomplete="off" placeholder="Create a new task or Search for existing one" @input="filter()" v-model="task" name="task">
        </form>
        <ul>
            <div class="li-container" v-for="(data, index) in filtertable" :key="index">
              <div class="list-item" v-if="editing != index">
              <li v-if="data.task.includes('del.dog')"><span v-html="data.task"></span></li>
              <li v-else>{{data.task}}</li>
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
        <p> {{holdertext()}} </p>
    </div>
  </div>
</template>

<script>

const baseurl = '/api/tasker/'

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
      filtertable: [],
      isloading: false,
    }
   },
    methods: {
    holdertext() {
      if( this.task != '') {
        if( this.filtertable.length < 1 && this.tasks.length > 0 )
           return 'No Matching Task Found'
      }
      if(this.tasks.length > 0)
        return 'Looks Like You Have Some Task To Do'
      else
        return 'Such Empty Much Wow'
    },
    getAll() {
          axios.get(baseurl + this.userid + '?status=todo').then(response => {
            var data = response.data;
            this.tasks = []
            for (let index = 0; index < data.length; index++) {
              var task_dict = data[index];
              this.tasks.unshift(task_dict);
            }
            this.filtertable = this.tasks
          })
    },

    addTask() {
          if(this.task != '') {
            if( this.task.length < 180) {
              axios.post(baseurl + this.userid, {completed: false, task: this.task}).then( response => {
                var data = response.data;
              this.task = '';
              this.tasks.unshift(data);
              })
            }
            else {
              this.isloading = true;
              axios.post('https://del.dog/documents/', this.task).then( response => {
                var link = response.data;
                axios.post(baseurl + this.userid, {completed: false, task: this.task.substring(0,30) + ' ... more at https://del.dog/' + link.key }).then( response => {
                  var data = response.data;
                  this.tasks.unshift(data);
                  this.task = '';
                  this.isloading = false;
                });
              });
            }
          }
    },

    filter() {
      if ( this.task == '') {
        this.filtertable = this.tasks;
        }
         var newtable = [];
         this.tasks.forEach(element => {
             if ( element.task.toLowerCase().includes(this.task.toLowerCase()) || element.timestamp.toLowerCase().includes(this.task.toLowerCase()) ) {
                newtable.push(element);
             }
         });
         this.filtertable = newtable
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
      axios.put(baseurl + this.userid, updated_task);
      this.tasks.splice(index, 1)
    },

    editTask(index) {
      if(this.edittext != ''){
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

        axios.put(baseurl + this.userid, updated_task).then(response => {
          var data = response.data;
          this.tasks.splice(index, 1, data)
        })

        this.editing = -1;
        this.edittext = '';
      }
    },

     remove(index) {
       var task_id = this.tasks[index].task_id
       axios.delete( baseurl + this.userid + '/' + task_id  )
       this.tasks.splice(index,1);
      }
    },

    created() {
      this.getAll();
      this.filtertable = this.tasks
    },

    watch: {
      task: function (val) {
        if(val == '') {
          this.filtertable = this.tasks
        }
      }
    },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "../../node_modules/animate.css/animate.css";
@import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";
@import url('https://fonts.googleapis.com/css?family=Julius+Sans+One|Lexend+Deca|Righteous&display=swap');

  .hello {
    margin: 0;
    padding: 0;
    transition: all 1s;
  }

  .loading {
    height: 100%;
    width: 95%;
    position: absolute;
    z-index: 3;
    left: 50%;
    transform: translateX(-50%);
    background: rgb(33, 58, 58);
  }

  .loading .logo {
    color: white;
    position: relative;
    font-size: 3em;
    z-index: 2;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: 'Righteous';
    text-align: center;
  }

  .holder {
    background: rgb(255, 255, 255);
    width: 95%;
    margin: 0 auto;
    min-height: 95%;
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
    background-color:#233C3C;
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

  li a {
    color: white;
    text-decoration: none;
  }

  i {
  align-self: flex-end;
  padding: 0.4em;
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
    padding: 0.4em 0.53em;
    background-color: rgb(255, 50, 70);
  }

  ul li {
    font-size: 1.4em;
  }

  .editingdiv {
    display: flex;
    justify-content: flex-start;
    align-items: baseline;
    font-size: 1.55em;
    color: white;
  }

  .editingdiv div {
    background-color: rgb(245, 245, 245);
    border-radius: 40px;
    color: rgb(70, 70, 70);
    padding: 0.36em 0.7em;
    font-weight: 500;
  }

  .editingdiv input[type=text] {
    border: 0;
    padding: 10px 30px;
    padding-left: 0.2em;
    margin-right: 0.7em;
    font-size: 0.9em;
    width: calc(100% - 6.8em);
    background-color: #233C3C;
    color: #fff;
    font-weight: 300;
  }

 .holder p {
    text-align:center;
    font-size: 1.1em;
    padding: 40px 0px;
    color: rgb(56, 56, 56);
  }

  form {
    position: sticky;
    top: 0;
  }

  .taskinput {
    width: calc(100% - 60px);
    border: 0;
    padding: 20px 30px;
    font-size: 1.3em;
    background-color: #213A3A;
    color: rgb(213, 214, 214);
  }

  @media screen and (max-width: 600px) {
    .holder {
      width: 100%;
    }
    ul {
     margin: 15px 5px;
    }
    i {
      font-size: 1.7em;
      margin: 0 3px;
    }
    .li-container {
      padding-left: 10px;
      margin-bottom: 3px;
      border-radius: unset;
    }
  }
</style>
