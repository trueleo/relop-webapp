<template>
  <div class="about page">
    <div class="statscard">
      <div class="outer">
        <div class="left">
          <div class="avatar">
            <img src="https://picsum.photos/200" alt="">
          </div>
        </div>
        <div class="right">
          <div class="greettext">
            Hello,&nbsp; {{fullname}}
          </div>
          <div class="quote">
            {{ quotes[quoteindex] }}
          </div>
          <div class="tasks">
            you have ongoing {{taskongoing}} tasks
          </div>
          <div class="taskdone">
            you have completed {{taskcompleted}} tasks
          </div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="left">
        <div class="profile">
          <img src="../assets/logo.svg" alt="">
        </div>
      </div>
      <div class="right">
        <div class="title">RELOP</div>
        <div class="version">Version: 0.1.5</div>
        <div class="links">
          <a href="http://github.com/trueleo" target="_blank">
            <i class="fa fa-github"></i>
          </a>
          <a href="http://trueleo.github.io" target="_blank">
            <i class="fa fa-globe"></i>
          </a>
          <a href="http://telegram.me/trueleo" target="_blank">
            <i class="fa fa-telegram"></i>
          </a>
        </div>
        <div class="author">Author:   &nbsp;  Satyam Singh ( trueleo )</div>
      </div>
    </div>
  </div>
</template>
<script>

const baseurl = 'http://localhost:5000/api/'
const quotes = [
  'Good Work Get Going',
  'Test and Learn',
  'You must be very tired',
  'Do you need a break',
  'Consistency is the key',
  'Commit to your goals',
  'It is never too late for challenges',
  'Coffee and Work.. Good'
]

import axios from 'axios';

export default {
  name: 'Tasker',
  data() {
    return {
      userid: this.$parent.userhash,
      fullname: '',
      taskcompleted: 0,
      taskongoing: 0,
      quotes: quotes, // THIS QUOTES = GLOBAL QUOTES
      quoteindex: 0,
    }
   },
 methods: {
      getData() {
          axios.get(baseurl + 'tasker/' + this.userid).then(response => {
            var data = response.data;
            data.forEach(element => {
              if ( element.completed == true)
                this.taskcompleted++;
              else
                this.taskongoing++;
            });
          });
        axios.get(baseurl + 'login/' + this.userid).then(response => {
            var data = response.data;
            this.fullname = data.fullname;
        });
      }
 },
 mounted() {
  this.getData();
  this.quoteindex = Math.floor(Math.random()*quotes.length)
 },
}
</script>
<style scoped>
@import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";

  .about {
    width: 100%;
    height: 100%;
    margin: 0 auto;
    transition: all 1s;
    /* display: flex;
    flex-direction: column;
    justify-content: space-evenly; */
  }

  .statscard {
    background: white;
    width: 80%;
    height: 27em;
    min-width: 30em;
    max-width: 50em;
    margin: 1em auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .statscard .outer {
    width: 90%;
    max-width: 40em;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-content: center;
}

  .left {
    /* margin: auto 0; */
  }

  .right {
    padding-left: 2em;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .greettext {
    font-size: 2em;
    font-weight: 600;
  }

  .quote {
    font-weight: 100;
    font-size: 1.2em;
    margin-bottom: 30px;
  }

  .avatar {
    width: 12em;
  }

  .avatar img {
    border-radius: 50%;
    width: 100%;
  }


  .card {
    /* border-radius: 10px; */
    background: white;
    width: 80%;
    min-width: 30em;
    max-width: 50em;
    padding: 16px 0px;
    /* height: 20em; */
    margin: 8em auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .card .left {
    /* flex-basis: 15em; */
  }
  .card .right {
    flex-basis: 40%;
  }

  .profile {
    width: 10em;
  }

  .profile img {
    width: 100%;
    height: auto;
  }

  .title {
    font-size: 2em;
    letter-spacing: 10px;
    line-height: 1.4em;
    font-weight: 600;
  }

  .version {
    padding: 5px 30px;
    background-color: black;
    color: white;
    text-align: end;
    font-size: 1em;
    font-weight: 100;
    line-height: 30px;
    letter-spacing: 2px;
  }

  .author {
    margin-top: 0.5em;
    font-size: 1em;
  }

  .links {
    margin-top: 20px;
    width: 100%;
    display: flex;
    justify-content: flex-start;
  }

  .links a{
    color: black;
  }

  .links i {
    font-size: 2em;
    margin: 0px 12px;
    border-radius: 50%;
  }

  @media screen and (max-width: 500px){
    .statscard .outer, .card {
      flex-direction: column;
      justify-content: center;
    }
    .statscard .left {
      margin-left: 10px;
      margin-bottom: 20px;
    }
    .statscard .right {
      padding-left: 30px;
    }
    .statscard .quote {
      margin-bottom: 10px;
    }
  }

</style>