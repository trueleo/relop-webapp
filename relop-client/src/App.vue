<template>
<div class="rootbody">
<!-- <transition name="nav-anim" enter-active-class="animated slideInLeft" leave-active-class="animated slideOutLeft" mode="out-in"> -->
<nav v-if="authenticated">
    <router-link to="/todo" replace> todo </router-link>
    <router-link to="/completed">completed</router-link>
    <router-link to="/about"> about </router-link>
    <router-link to="/login" v-on:click.native="logout()" replace>logout</router-link>
</nav>
<!-- </transition> -->
<transition name="naav-anim" enter-active-class="animated slideInRight fast" leave-active-class="animated fadeOutDown fast" >
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
	this.$router.beforeEach((to, from, next) => {
		if (!this.authenticated) next('/login')
		else next()
	});
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
  overflow: hidden;
  margin: 0;
  padding: 0;
  background-color: #0c4359;
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
  margin: 0 auto;
  padding: 0.8em 1.2em;
  transition: all 0.5s;
  display: flex;
}

nav * {
  padding: 0.4em 0.6em;
  margin-right: 15px;
  text-decoration: none;
  color: rgb(0, 110, 255);
  background: #fff;
  border-radius: 3px;
  font-weight: bold;
  font-size: 1.4em;
}

nav *:nth-child(4) {
  margin-left: auto;
  margin-right: 0;
}

nav *::-moz-focus-inner {
  border: none;
}

nav *:focus {
  outline: 2px dashed rgb(255, 255, 255);
  outline-offset: 4px;
}

.page {
  height: calc( 100% - 2*0.8em - 2*1.4*0.4em - 1.4em );
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
    font-size: 1.3em;
  }
}
</style>
