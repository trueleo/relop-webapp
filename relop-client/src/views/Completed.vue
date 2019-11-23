<template>
    <div class="main-body page">
        <input type="text" v-model="searchtext" @input="filter()" placeholder="Search..." >
        <table class="table">
            <tr>
                <!-- <th id="sno">#</th> -->
                <th id >TASK</th>
                <th>TIME</th>
            </tr>
            <tr v-for="(data, index) in filtertable" :key="index">
                <!-- <td> <div> {{index + 1}} </div> </td> -->
                <td>{{ data.task }}</td>
                <td>{{ data.timestamp }}</td>
            </tr>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
const baseurl = '/api/tasker/';

export default {
    data() {
        return {
            userid: this.$parent.userhash,
            table: [],
            filtertable: [],
            searchtext: ''
        }
    },

    methods: {
        getCompleted() {
            axios.get(baseurl + this.userid + '?status=done').then(response => {
                var data = response.data;
                this.table = [];
                for (let index = 0; index < data.length; index++) {
                    var task_dict = data[index];
                    var date = new Date(task_dict['timestamp'])
                    task_dict['timestamp'] = date.toString().substring(0,24);
                    this.table.unshift(task_dict);
                }
                this.filtertable = this.table;
            });
        },
       filter() {
        if ( this.searchtext == '') {
            this.filtertable = this.table;
        }
         var newtable = [];
         this.table.forEach(element => {
             if ( element.task.toLowerCase().includes(this.searchtext.toLowerCase()) || element.timestamp.toLowerCase().includes(this.searchtext.toLowerCase()) ) {
                newtable.push(element);
             }
         });
         this.filtertable = newtable
       }
    },
    created() {
        this.getCompleted();
    },
}
</script>

<style scoped>

.main-body {
    width: 100%;
    margin: 0em auto;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: baseline;
    transition: all 1s;
}

input {
    margin: 0 auto;
    width: calc(90% - 60px);
    border: 0;
    padding: 20px 30px;
    font-size: 1.2em;
    background-color: #ffffff;
    color: rgb(0, 0, 0);
}

.table {
  border-collapse: collapse;
  width: 90%;
  margin: 0px auto;
}

.table tr {
    background-color: #ffffff;
}

/* .table tr:nth-child(even){background-color: #effbff;} */

.table tr:hover {background-color: #dfdfdf;}


.table th {
    border-top: 2px solid rgb(171, 170, 241);
  /* border: 2px solid rgb(0, 0, 0); */
  padding-top: 15px;
  height: 1em;
  padding-bottom: 15px;
  text-align: center;
  font-size: 1.2em;
  font-weight: 400;
  background-color: #004646;
  color: rgb(255, 255, 255);
}

.table td {
    border: 1px solid rgba(26, 26, 26, 0.575);
    padding: 15px 10px;
    font-size: 1.2em;
    text-align: center;
    color: rgb(0, 0, 0);
}

.table td:nth-child(2) {
    font-size: 1em;
}
@media screen and (max-width: 600px){
    .table {
        width: 95%;
    }
    input {
        width: calc( 95% - 60px );
    }
}
</style>
