<template>
    <div class="main-body page">
        <div v-if="isloading" class="loading">
          <div class="logo">
            loading...
          </div>
        </div>
        <input type="text" autocomplete="off" v-model="searchtext" @input="filter()" placeholder="Search..." >
        <div class="container">
            <ul>
                <li v-for="(data, index) in filtertable" :key="index">
                    <div>
                        <span class="circle"></span>
                        <div class="info">{{data.task}}</div>
                        <span class="number">
                            <span> {{data.timestamp.split(' ')[4].substring(0,5)}} </span>
                            <span> {{data.timestamp.split(' ')[2] + " " + data.timestamp.split(' ')[1]}} </span>
                        </span>
                    </div>
                </li>
            </ul>
        </div>
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
        matchdate(timestamp, searchtext) {
               var included = 0;
               timestamp.toLowerCase().split(' ').forEach(el => {
                if(searchtext.split(' ').includes(el))
                  included++;
               });
               if(included == searchtext.split(' ').length) {
                 return true
               }
        },
       filter() {
        if ( this.searchtext == '' ) {
            this.filtertable = this.table;
        }
        else {
         var newtable = [];
         this.table.forEach(element => {
             if ( element.task.toLowerCase().includes(this.searchtext.toLowerCase()) || this.matchdate(element.timestamp, this.searchtext)) {
                 newtable.push(element);
             }
         });
         this.filtertable = newtable
        }
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
    width: 90%;
    border: 0;
    padding: 20px 30px;
    font-size: 1.1em;
    border-bottom: 1px solid #00000014;
    background-color: #ffffff;
    color: rgb(0, 0, 0);
    position: sticky;
    z-index: 2;
    border-radius: 7px;
    top: 0;
}

.container {
  width: 90%;
  margin: 0px auto;
  background: rgba(255, 255, 255, 0.192);
}


.container ul {
  list-style: none;
  position: relative;
  top: 0;
  padding: 10px 10px 5px 7em;
  color: rgb(255, 255, 255);
  font-size: 1.4em;
}

.container ul:before {
  content: '';
  width: 1px;
  height: 100%;
  position: absolute;
  border-left: 2px dashed rgba(255, 255, 255, 0.856);

}
.container ul li {
  position: relative;
  margin-left: 2em;
  background-color: rgba(29, 29, 29, 0.438);
  padding: 15px 10px 15px 5px;
  border-radius: 6px;
  width: calc(100% - 4em);
  /* box-shadow: 0 0 4px rgba(0, 0, 0, .12), 0 2px 2px rgba(0, 0, 0, .08) */
}

.container ul li:not(:first-child) {
  margin-top: 2em;
}

.container ul li .circle {
  width: 2px;
  height: 100%;
  background: #fff;
  left: -2em;
  top: 0;
  position: absolute;
}

.container ul li .circle:before, .container ul li .circle:after {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  border: 2px solid #fff;
  position: absolute;
  background: #86b7e7;
  left: -5px;
  top: 0;
}
.container ul li .circle:after {
  top: 100%;
}

.container ul li .info {
  margin-left: 0.8em;
}

.container .number {
  height: 100%;
}

.container .number span {
  position: absolute;
  font-size: 0.7em;
  left: -11em;
  font-weight: bold;
}

.container .number span:first-child{
  top: 28%;
}

.container .number span:last-child {
    top: 60%;
}

@media screen and (max-width: 600px){

    input {
        padding: 10px 20px;
    }

    .container {
        font-size: 0.9em;
        width: 95%;
    }
    .container ul {
        padding-left: 5em;
    }
    .container ul li {
        margin-left: 1em;
    }
    .container ul li .circle {
        left: -1em;
    }

    .container ul .number span {
        left: -9em;
        font-size: 0.65em
    }
}
</style>
