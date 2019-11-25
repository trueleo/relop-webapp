<template>
<div class="rootbody">
<transition name="nav-anim" enter-active-class="animated slideInLeft" leave-active-class="animated slideOutLeft" mode="out-in">
<nav v-if="authenticated">
  <p>
    <router-link to="/todo" replace> todo </router-link>
    <router-link to="/completed">completed</router-link>
    <router-link to="/about"> about </router-link>
    <router-link to="/login" v-on:click.native="logout()" replace>logout</router-link>
  </p>
</nav>
</transition>
<transition name="naav-anim" enter-active-class="animated slideInRight" leave-active-class="animated slideOutRight" mode="out-in">
  <router-view @authenticated="setAuthenticated" @signoff="logout"> </router-view>
</transition>
</div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      animating: false,
      authenticated: false,
      userhash: '',
    }
  },
  watch: {
    authenticated() {
        if(!this.authenticated) {
          this.$router.replace({ name: "login" });
          this.userhash = '';
        }
    }
  },
  mounted() {
            if(!this.authenticated) {
                this.$router.replace({ name: "login" });
            }
        },
  methods: {
            setAuthenticated(hashstr) {
                this.userhash = hashstr;
                this.authenticated = true;
            },
            logout() {
                this.userhash = '';
                this.authenticated = false;
            }
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');
@import "../node_modules/animate.css/animate.css";

body {
  font-family: 'Montserrat', sans-serif;
}


.rootbody {
  /* overflow: hidden; */
  margin: 0;
  padding: 0;
  background-color: #11a9e6;
  background-size: auto;
  /* width: 100%; */
  height: 100%;
}

body, html {
  margin: 0;
  /* width: 100%; */
  height: 100%;
}

nav {
  background-color: rgb(75, 107, 212);
  margin: 0 auto 20px auto;
  padding: 1.2em;
  transition: all 0.5s;
}

nav p {
  background-color: rgb(136, 250, 184);
}

nav p * {
  padding: 0.5em 0.8em;
  margin-right: 15px;
  text-decoration: none;
  color: rgb(0, 110, 255);
  background: #fff;
  border-radius: 3px;
  font-weight: bold;
  font-size: 1.4em;
}

nav *:nth-child(4) {
  position: absolute;
  margin-right: 0;
  transform: translateY(-0.55em);
  right: 0.6em;
}

.page {
  height: 100%;
  position: fixed;
  width: 100%;
  overflow: auto;
}

@media screen and (max-width: 600px){
  body {
    font-size: 0.7rem;
  }
}

@media screen and (max-width: 500px){
  nav p * {
    margin-right: 8px;
    font-size: 1.2em;
  }
}
</style>
