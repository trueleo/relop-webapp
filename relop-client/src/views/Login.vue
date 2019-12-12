<template>
<div class="rbody page">
  <div class="container">
    <transition name="fade" mode="out-in">
      <div class="login-container" v-if="tab == 1" key="loginpage">
        <transition name="error-anim" enter-active-class="animated slideInDown" leave-active-class="animated slideOutRight" mode="out-in">
        <h2 v-if="haserror" v-bind:style="{ backgroundColor: '#ff0d2d' }" key="activelogin"> Login Failed </h2>
        <h2 v-else v-bind:style="{ backgroundColor: '#00574f' }" key="errorlogin"> Login </h2>
        </transition>
        <div class="login-feild">
        <input class="inputtext" v-model="login.username" v-on:keyup.enter="focusInput('passinput')" ref="userinput" type="text" placeholder="username" >
        </div>
        <div class="login-feild">
        <input class="inputtext" v-model="login.password" v-on:keyup.enter="authenticate()" ref="passinput" type="password" placeholder="password">
        </div>
        <input class="submitbutton" type="submit" value="LOGIN" @click="authenticate">
      </div>
      <div class="create-container" v-if="tab == 2" key="createpage">
        <transition name="error-anim" enter-active-class="animated slideInDown" leave-active-class="animated slideOutRight" mode="out-in">
        <h2 v-if="hascreateerror" v-bind:style="{ backgroundColor: '#ff0d2d' }" key="activelogin"> {{ errormsg }} </h2>
        <h2 v-else v-bind:style="{ backgroundColor: '#00574f' }" key="errorlogin"> Register </h2>
        </transition>
        <div class="login-feild">
        <input class="inputtext" v-model="newaccount.fullname" v-on:keyup.enter="focusInput('c_userinput')" ref="c_fullname" type="text" placeholder="full name">
        </div>
        <div class="login-feild">
        <input class="inputtext" v-model="newaccount.username" v-on:keyup.enter="focusInput('c_passinput')" ref="c_userinput" type="text" placeholder="username">
        </div>
        <div class="login-feild">
        <input class="inputtext"  v-model="newaccount.password" v-on:keyup.enter="create()" ref="c_passinput" type="password" placeholder="password">
        </div>
        <input class="submitbutton" type="submit" value="CREATE" @click="create">
      </div>
    </transition>
  </div>
  <div class="create-button" @click="tab = ( tab == 1 ? 2 : 1 );  ">
    {{ tab == 1 ? "Create New Account" : "Login To An Existing Account" }}
  </div>
</div>
</template>

<script>
import axios from 'axios';
import md5 from 'blueimp-md5';

const baseurl = '/api/login/';

export default {
  data() {
    return {
            tab: 1,
            haserror: false,
            hascreateerror: false,
            errormsg: '',
            login: {
              username: '',
              password: ''
            },
            newaccount: {
              fullname: '',
              username: '',
              password: '',
            },

    }
  },
  methods: {
    loginError() {
      this.login.username = '';
      this.login.password = '';
      this.haserror = true;
      setTimeout(this.resetError, 4000);
    },
    createError(msg) {
      this.errormsg = msg;
      this.newaccount.password = '';
      this.hascreateerror = true;
      setTimeout(this.resetError, 4000);
    },
    resetError() {
      this.haserror = false;
      this.hascreateerror = false;
    },
    create() {
      if ( this.newaccount.username == '') {
        this.createError('Username Empty');
            this.newaccount.username = '';
          }
          else if ( this.newaccount.password.length < 8 ) {
            this.createError('Password must be greater than 8 characters');
          }
          else if (this.newaccount.fullname == '' ) {
            this.newaccount.fullname = '';
            this.createError('Enter Your Name');
          }
          else {
            axios.post(baseurl, {username: this.newaccount.username, fullname: this.newaccount.fullname, hashid: this.gethash(this.newaccount.username, this.newaccount.password) }).then( response => {
              var data = response.data;
              this.$emit("authenticated", data['hash_id']);
              this.$router.replace({path:'/todo', name: "task"});
            }).catch(error => {
              if (error.response.status == 409) {
                this.createError('username already taken');
              }
            });
          }
    },
    authenticate() {
        axios.get(baseurl + this.gethash(this.login.username, this.login.password)).then( response => {
          var data = response.data;
          this.$emit("authenticated", data['hash_id']);
          this.$router.replace({path:'/todo', name: "task"});
        }).catch( () => {
            this.loginError()
          });
    },
    gethash(username, password) {
      const hstr = username + password;
      var hash = md5(hstr);
      return hash;
    },
    focusInput(inputRef) {
      this.$refs[inputRef].focus();
    },
  },
  mounted() {
      // this.focusInput('userinput');
  },
}
</script>
<style scoped>
    @import "../../node_modules/animate.css/animate.css";
    @import url('https://fonts.googleapis.com/css?family=Julius+Sans+One|Lexend+Deca|Righteous&display=swap');

    .rbody {
      background-image: url('../assets/background1.svg');
      background-repeat: no-repeat;
      background-size: cover;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

  .create-button {
    margin-top: 2em;
    padding: 10px 20px;
    background-color: rgba(0, 48, 40, 0.582);
    color: white;
    border-radius: 30px;
    width: 11em;
    text-align: center;
    cursor: pointer;
  }

  .container {
    background: #fff;
    -webkit-box-shadow: 1px 4px 11px -3px rgba(0,0,0,0.53);
    -moz-box-shadow: 1px 4px 11px -3px rgba(0,0,0,0.53);
    box-shadow: 1px 4px 12px -3px rgba(0,0,0,0.53);
    width: 30%;
    min-width: 30em;
    max-width: 32em;
  }

  .login-container {
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .login-container h2 {
    font-family: 'Righteous', Arial, Helvetica, sans-serif;
    font-size: 3em;
    font-weight: 400;
    color: white;
    padding: 1em;
    padding-top: 1.5em;
    padding-bottom: 0.8em;
    margin-top: 0;
    }

  .login-feild {
    display: flex;
    flex-direction: row;
    height: 4em;
    font-size: 1rem;
    align-items: center;
    justify-content: center;
  }

  .create-container {
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .create-container h2 {
    font-family: 'Lexend Deca', Arial, Helvetica, sans-serif;
    font-size: 3em;
    font-weight: 400;
    color: white;
    padding: 3rem;
    padding-top: 4rem;
    padding-bottom: 2rem;
    margin-top: 0;
    background-color: #08240073;
  }

 .create-container h2, .login-container h2 {
    cursor: default;
 }

  .create-container .submitbutton {
    align-self: center;
  }
  .inputtext {
    /* background-color: rgba(0,53,40,0.53); */
    /* color: white; */
    background-color: rgba(255, 255, 255, 0);
    color: black;
    border-width: 1px;
    border-width: 1px;
    border-top: unset;
    border-right: unset;
    border-left: unset;
    border-bottom-color: rgb(24, 24, 24);
    height: 57%;
    width: 76%;
    /* vertical-align: center; */
    padding: 0.3em 1em;
  }

  .submitbutton {
    background: linear-gradient(135deg, #1facd2 0%, #00ebd6 100%);
    color: white;
    border: unset;
    border-radius: 30px;
    padding: 1.2em 3.2em;
    margin-top: 2em;
    margin-bottom: 2em;
    font-size: 1em;
    font-weight: 600;
    align-self: center;
  }

  .container {
    transition: all 1s;
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
</style>
