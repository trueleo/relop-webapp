<template>
    <div class="main-body page">
        <div v-if="isloading" class="loading">
          <div class="logo">
            loading
          </div>
          <div class="loadingbar">
            <bounce-loader class="loading-circle" :loading="isloading" :size="8" sizeUnit="em" color="#fff" ></bounce-loader>
          </div>
        </div>
        <input type="text" autocomplete="off" v-model="searchtext" @input="filter()" placeholder="Search..." >
        <div class="container">
            <ul v-if="filtertable.length > 0">
                <li v-for="(data, index) in filtertable" :key="index">
                    <div>
                        <span class="circle"></span>
                        <div class="info">{{data.task}}</div>
                        <span class="number">
                            <span> {{data.timestamp.toString().split(' ')[4].substring(0,5)}} </span>
                            <span> {{data.timestamp.toString().split(' ')[2] + " " + data.timestamp.toString().split(' ')[1]}} </span>
                        </span>
                    </div>
                </li>
            </ul>
            <p style="font-size: 4em; color: #535353" v-else-if="table.length > 0">
                :(
            </p>
            <p v-else>
               Your Completed Tasks Will Appear Here
            </p>
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
                data.forEach(element => {
                  element.timestamp = new Date(element.timestamp + 'Z')
                });
                this.table = data;
                this.table.sort(function (a,b) {
                  return b.timestamp - a.timestamp
                })
                this.filtertable = this.table;
                this.isloading = false;
            });
        },
        matchdate(timestamp, searchtext) {
               var included = 0;
               const day = {
                      "mon": "monday",
                      "tue": "tuesday",
                      "wed": "wednesday",
                      "thu": "thursday",
                      "fri": "friday",
                      "sat": "saturday",
                      "sun": "sunday"
               };
               const month = {
                      "jan": "january",
                      "feb": "february",
                      "mar": "march",
                      "apr": "april",
                      "may": "may",
                      "jun": "june",
                      "jul": "july",
                      "aug": "august",
                      "sept": "september",
                      "oct": "october",
                      "nov": "november",
                      "dec": "december",
               }
               var tm = timestamp.toString().toLowerCase().substring(0,15);
               const replace_day = tm.substring(0,3);
               const replace_month = tm.substring(4,7);
               tm = tm.replace(replace_day, day[replace_day]);
               tm = tm.replace(replace_month, month[replace_month]);
               searchtext.toLowerCase().split(' ').forEach(el => {
                if(tm.includes(el))
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
    height: 100%;
    width: 98%;
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

input {
    margin: 0 auto;
    margin-top: 30px;
    width: calc( 95% - 60px );
    border: 0;
    padding: 20px 30px;
    font-size: 1.1em;
    border-bottom: 1px solid #00000014;
    background-color: #05aaaa;
    color: #fff;
    position: sticky;
    z-index: 2;
    /* border-radius: 7px; */
    top: 0;
}

.container {
  width: 95%;
  margin: 0px auto;
  background: #ffffff;
  height: calc(100% - 8em);
  overflow-y: scroll;
}

.container p {
  text-align: center;
  margin-top: 15vh;
}

.container ul {
  list-style: none;
  position: relative;
  top: 0;
  padding: 10px 10px 5px 7em;
  font-size: 1.4em;
}

.container ul:before {
  content: '';
  width: 1px;
  height: 100%;
  position: absolute;
  border-left: 2px dashed rgb(46, 46, 46);

}

.container ul li {
  position: relative;
  margin-left: 2em;
  background-color: rgb(243, 243, 243);
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
  background: rgb(10, 10, 10);
  left: -2em;
  top: 0;
  position: absolute;
}

.container ul li .circle:before, .container ul li .circle:after {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  border: 2px solid #1a1a1a;
  position: absolute;
  background-color: #05aaaa;
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
  color:rgb(70, 70, 70);
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
    .loading {
      width: 100%;
    }
    input {
      margin-top: 5px;
      width: calc( 100% - 60px)
    }
    .container {
        font-size: 0.9em;
        width: 100%;
    }
    .container p {
        font-size: 1.2em;
    }
    .container ul {
        padding-left: 5em;
    }
    .container ul li {
        margin-left: 1em;
        width: calc(100% - 2.5em);
    }
    .container ul li .circle {
        left: -1em;
    }
    .container ul .number span {
        left: -6em;
        font-size: 0.8em
    }
}
</style>
