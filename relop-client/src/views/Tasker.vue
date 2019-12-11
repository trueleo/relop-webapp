<template>
  <div class="hello page">
    <div v-if="isloading" class="loading">
      <div class="logo">
        loading
      </div>
      <div class="loadingbar">
        <bounce-loader class="loading-circle" :loading="isloading" :size="8" sizeUnit="em" color="#fff" ></bounce-loader>
      </div>
    </div>
    <div class="holder">
        <form @submit.prevent="addTask">
          <input class="taskinput" type="text" autocomplete="off" placeholder="Create a new task or Search for existing one" v-model="task" name="task">
        </form>
           <transition-group name="list-complete" tag="ul">
            <div class="li-container" v-for="(data, index) in computedList" :key="data.task_id" v-bind:data-index="index">
              <div class="list-item" v-if="editing != data.task_id">
              <li v-if="data.task.includes('del.dog')"><span v-html="data.task"></span></li>
              <li v-else>{{data.task}}</li>
              <i class="fa fa-edit" v-on:click="editing = data.task_id; edittext = data.task"></i>
              <i class="fa fa-check" v-on:click="completeTask(data.task_id)"></i>
              <i class="fa fa-times" v-on:click="remove(data.task_id)"></i>
              </div>
              <div v-if="editing == data.task_id" class="editingdiv">
                <input type="text" placeholder="Enter a task.." v-model="edittext" v-on:keyup.enter="editTask(data.task_id)" name="edit">
                <div @click="editTask(data.task_id)"> save </div>
              </div>
            </div>
           </transition-group>
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
      isloading: false,
    }
   },
   computed: {
     computedList: function () {
       var vm = this;
       return vm.tasks.filter( function (element) {
            if ( element.task.toLowerCase().includes( vm.task.toLowerCase() ) )
              return element;
       })
     }
   },
    methods: {
    holdertext() {
      if( this.task != '') {
        if( this.computedList.length < 1 && this.tasks.length > 0 )
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
              this.tasks.unshift(data);
              })
            }
            else {
              this.isloading = true;
              axios.post('https://del.dog/documents/', this.task).then( response => {
                var link = response.data;
                axios.post(baseurl + this.userid, {completed: false, task: this.task.substring(0,30) + ' ... more at https://del.dog/' + link.key }).then( response => {
                  var data = response.data;
                  this.isloading = false;
                  this.tasks.unshift(data);
                });
              });
            }
            this.task = '';
          }
    },
    completeTask(taskid) {
      const blacklist = ['timestamp'];
      var index = this.tasks.findIndex( function (item) {
          return item.task_id == taskid
      })
      var dict = this.tasks[index]
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

    editTask(taskid) {
      if(this.edittext != '') {
        const blacklist = ['timestamp'];
        var index = this.tasks.findIndex( function (item) {
          return item.task_id == taskid
        });
        var dict = this.tasks[index]
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

     remove(taskid) {
       var index = this.tasks.findIndex( function (item) {
          return item.task_id == taskid
       });
       const task_id = this.tasks[index].task_id;
       axios.delete( baseurl + this.userid + '/' + task_id  );
       this.tasks.splice(index, 1);
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
    margin-top: 20px;
    padding: 0;
    transition: all 1s;
  }
   .loading {
    height: 100%;
    width: 96%;
    position: absolute;
    z-index: 3;
    background: rgb(48, 48, 48);
    display: flex;
    flex-direction: column;
    justify-content: center;
    left: 50%;
    transform: translateX(-50%);
  }

  .loading .logo {
    color: white;
    font-size: 3em;
    margin: 0 auto;
    font-family: 'Righteous';
    text-align: center;
    padding-bottom: 2em;
  }

  .loading-circle {
    margin: 0 auto;
  }
  .holder {
    background: rgb(255, 255, 255);
    width: 95%;
    margin: 0 auto;
    height: 95%;
    overflow: hidden;
    position: relative;
  }

  ul {
    margin: 0;
    padding: 0;
    list-style-type: none;
    overflow-y: scroll;
    height: calc( 100% - 70px);
  }

  .li-container {
    padding: 10px;
    padding-left: 30px;
    padding-right: 5px;
    border-radius: 40px;
    margin-bottom: 5px;
    margin-right: 30px;
    margin-left: 30px;
    background-color:#233C3C;
  }

  .li-container:first-child {
    margin-top: 30px;
  }

  .li-container:last-child {
    margin-bottom: 40px;
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
    font-size: 1.0em;
    padding: 10px 0px;
    color: rgb(255, 255, 255);
    background-color: #4b6bd4;
    position: fixed;
    width: calc( 95% );
    bottom: 0;
    margin-bottom: 0;
    z-index: 4;
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

  .list-complete-leave, .list-complete-leave-active {
    position: absolute;
    width: calc(100% - 105px);
    transition: all 300ms
  }
  .list-complete-enter-active {
    transition: all 300ms
  }
  .list-complete-leave-to, .list-complete-enter {
    opacity: 0;
    transform: translateY(-20px);
  }
  .list-complete-move {
    z-index: 0;
    transition: all 600ms;
  }

  @media screen and (max-width: 600px) {
    .holder {
      width: 100%;
    }
    .holder p {
      width: 100%;
    }
    .loading {
      width: 100%;
    }
    ul {
     margin: 0;
     margin-bottom: 40px;
    }
    i {
      font-size: 1.7em;
      margin: 0 3px;
    }
    .li-container {
      padding-left: 10px;
      margin: 2px;
      margin-bottom: 3px;
      border-radius: unset;
    }
    .li-container:first-child {
      margin-top: 15px;
    }

    .li-container:last-child {
      margin-bottom: 20px;
    }

    .list-complete-leave, .list-complete-leave-active {
      width: calc(100% - 30px);
    }
  }
</style>
