<template>
  <div class="about page">
    <vue-particles class="parjs" color="#fff"
        :particleOpacity="1"
        :particlesNumber="30"
        shapeType="circle"
        :particleSize="25"
        linesColor="#ffffff"
        :linesWidth="2"
        :lineLinked="true"
        :lineOpacity="0.9"
        :linesDistance="200"
        :moveSpeed="2"
    >
    </vue-particles>
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
        <div class="version">Version: 0.4.0</div>
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
        <!-- <div class="author">Satyam Singh</div> -->
      </div>
    </div>
  </div>
</template>
<script>

const baseurl = '/api/'
const quotes = [
  'Good Work Get Going',
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
    background-color: #0c4359;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .statscard {
    background: linear-gradient(45deg, rgb(64, 140, 190) 0%,
                              rgb(64, 140, 190) 4%,rgb(62, 107, 145) 4%,
                              rgb(62, 107, 145) 7%,rgb(49, 99, 131) 7%,
                              rgb(49, 99, 131) 9%,rgb(116, 172, 211) 9%,
                              rgb(116, 172, 211) 23%,rgb(125, 182, 214) 23%,
                              rgb(125, 182, 214) 29%,rgb(40, 90, 136) 29%,
                              rgb(40, 90, 136) 35%,rgb(39, 123, 190) 35%,
                              rgb(39, 123, 190) 100%);
    position: relative;
    width: 80%;
    height: 27em;
    min-width: 30em;
    max-width: 50em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    z-index: 2;
    /* margin-top: -7em; */
  }

  .parjs {
    position: absolute;
    width: 100%;
    z-index: -1;
    height: 100%;
  }

  .statscard .outer {
    width: 90%;
    position: absolute;
    max-width: 40em;
    /* margin0: 0 auto; */
    left: 5%;
    display: flex;
    justify-content: space-between;
    align-content: center;
}

  .statscard .right {
    padding-left: 2em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color:#0c4359;
  }

  .greettext {
    font-size: 2em;
    font-weight: 600;
  }

  .tasks, .taskdone {
    font-size: 1.3em;
  }

  .quote {
    font-weight: 100;
    font-size: 1.2em;
    margin-bottom: 30px;
  }

  .avatar {
    width: 12em;
    padding-top: 12em;
    background-color: rgb(255, 255, 255);
    border-radius: 50%;
  }

  .avatar img {
    position: absolute;
    top: 0;
    border-radius: 50%;
    width: inherit;
    height: inherit;
    box-shadow: 0 0 1px 0px rgba(255, 255, 255, 0) inset, 0 0 1px 0px rgba(255, 255, 255, 0), 0 0 0 5px #285a88;
  }


  .card {
    background: white;
    width: 80%;
    min-width: 30em;
    max-width: 50em;
    padding: 16px 0px;
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: row-reverse;
    justify-content: space-around;
    align-items: center;
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
    color: #0c4359;
  }

  .version {
    padding: 5px 30px;
    background-color: #0c4359;
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
    color: #0c4359;
  }

  .links i {
    font-size: 2em;
    margin: 0px 12px;
    border-radius: 50%;
  }

  @media screen and (max-width: 600px){
    .statscard {
      background: linear-gradient(225deg,
                              rgb(64, 140, 190) 0%,
                              rgb(64, 140, 190) 4%,rgb(62, 107, 145) 4%,
                              rgb(62, 107, 145) 7%,rgb(49, 99, 131) 7%,
                              rgb(49, 99, 131) 9%,rgb(116, 172, 211) 9%,
                              rgb(116, 172, 211) 23%,rgb(125, 182, 214) 23%,
                              rgb(125, 182, 214) 29%,rgb(40, 90, 136) 29%,
                              rgb(40, 90, 136) 35%,rgb(39, 123, 190) 35%,
                              rgb(39, 123, 190) 100%
                              );
    }

    .statscard, .card {
      width: 85%;
    }

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

  .links a:focus {
  -webkit-tap-highlight-color: rgba(255,255,255,0) !important;
  -webkit-focus-ring-color: rgba(255,255,255,0) !important;
  outline: none;
  }

  .links a:focus i {
    color: rgb(0, 233, 163);
  }

</style>
