<template>
<div class="rootbody">
<transition name="nav-anim" enter-active-class="animated fadeInDown" mode>
<nav v-if="authenticated">
  <p>
    <router-link to="/todo" replace> todo </router-link>
    <router-link to="/completed">completed</router-link>
    <router-link to="/about"> about </router-link>
    <router-link to="/login" v-on:click.native="logout()" replace>logout</router-link>
  </p>
</nav>
</transition>
<transition name="router-anime" enter-active-class="animated slideInRight" leave-active-class="animated slideOutRight">
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
  components: {
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1";

body {
  font-family: 'Montserrat', sans-serif;
}

.rootbody {
  /* overflow: hidden; */
  margin: 0;
  padding: 0;
  background-color: #4eabf7;
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
  padding: 20px 20px 20px 20px;
}

nav p {
  background-color: rgb(136, 250, 184);
}

nav p * {
  padding: 10px 20px;
  margin-right: 15px;
  text-decoration: none;
  color: rgb(0, 110, 255);
  background: #fff;
  border-radius: 3px;
  font-weight: bold;
  font-size: 1.4rem;
}
nav *:nth-child(4) {
  margin: 0;
  position: absolute;
  right: 20px;
  top: 26px;
}

.page {
  height: 100%;
  position: fixed;
  width: 100%;
  overflow: auto;
}

</style>
