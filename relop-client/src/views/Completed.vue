<template>
    <div class="main-body page">
        <input type="text" placeholder="Search..." >
        <table class="table">
            <tr>
                <th id="sno">#</th>
                <th id >task</th>
                <th>time</th>
            </tr>
            <tr v-for="(data, index) in table" :key="index">
                <td> <div> {{index + 1}} </div> </td>
                <td>{{ data.task }}</td>
                <td>{{ data.timestamp }}</td>
            </tr>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
const baseurl = 'http://localhost:5000/api/tasker/';

export default {
    data() {
        return {
            userid: this.$parent.userhash,
            table: [],
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
            });
        },
    },
    created() {
        this.getCompleted();
    },
}
</script>

<style scoped>

.main-body {
    width: 100%;
    margin: 3em auto;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: baseline;
}

input {
    margin: 0 auto;
    margin-bottom: 30px;
    width: 40%;
    padding: 10px 20px;
    border-radius: 20px;
    border: unset
}

.table {
  border-collapse: collapse;
  width: 90%;
  margin: 10px auto;
}

.table td {
  border: 3px solid rgb(241, 241, 241);
  padding: 15px 10px;
}

.table th {
    border: 5px solid rgb(69, 235, 158);
}

.table tr:nth-child(even){background-color: #f2f2f2;}

.table tr:hover {background-color: #ddd;}


.table th {
  padding-top: 15px;
  padding-bottom: 15px;
  text-align: center;
  font-size: 1.4em;
  font-weight: 400;
  background-color: #004646;
  color: rgb(251, 255, 253);
}

.table td {
    font-size: 1.2em;
    text-align: center;
    background-color: #006666;
    color: white;
}

.table td:nth-child(3) {
    font-size: 1em;
}

</style>