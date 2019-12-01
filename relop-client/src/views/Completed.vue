<template>
    <div class="main-body page">
        <div v-if="isloading" class="loading">
          <div class="logo">
            loading...
          </div>
        </div>
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
            searchtext: '',
            isloading: false
        }
    },

    methods: {
        getCompleted() {
            this.isloading = true
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
                this.isloading = false;
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

  .loading {
    height: 100vh;
    width: 100vw;
    position: absolute;
    z-index: 3;
    background: rgba(33, 58, 58, 0.733);
  }

  .loading .logo {
    height: 5em;
    width: 5em;
    color: white;
    position: absolute;
    font-size: 2em;
    z-index: 2;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

input {
    margin: 0 auto;
    width: calc(95% - 60px);
    border: 0;
    padding: 20px 30px;
    font-size: 1.2em;
    border-bottom: 1px solid #00000014;
    background-color: #ffffff;
    color: rgb(0, 0, 0);
    position: sticky;
    top: 0;
}

.table {
  /* border-collapse: collapse; */
  width: 95%;
  margin: 0px auto;
  border-spacing: 12px;
  background: white;
}

.table tr {
    /* background-color: #ffffff; */

}

/* .table tr:nth-child(even){background-color: #effbff;} */

/* .table tr:hover {background-color: #dfdfdf;} */


.table th {
  border: 3px solid rgba(171, 170, 241, 0.466);
  padding-top: 15px;
  height: 1em;
  padding-bottom: 15px;
  text-align: center;
  font-size: 1.2em;
  font-weight: 400;
  background-color: #fff;
  color: #2e2e2e;
  border-radius: 50px;
}

.table td {
    border: 5px solid #213A3A;
    border-radius: 50px;
    background-color: #213A3A;
    color: #fff;
    padding: 15px 10px;
    font-size: 1.2em;
    text-align: center;
}

.table td:nth-child(2) {
    font-size: 1em;
}
@media screen and (max-width: 600px){
    .table {
        width: 100%;
        border-spacing: 2px;
        /* border-collapse: collapse; */
    }
    .table th {
        border: unset;
    }
    .table td {
        border: 1px solid #00000000;
        border-radius: unset;
    }
    input {
        width: calc( 100% - 60px );
    }
}
</style>
