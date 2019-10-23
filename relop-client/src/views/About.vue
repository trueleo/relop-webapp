<template>
  <div class="about page">
    <div class="card">
      <div class="profile">
        <img src="../assets/logo.svg" alt="">
      </div>
      <div class="title">RELOP</div>
      <div class="version">Version: 0.1.5</div>
      <div class="author">Author:   &nbsp;  Satyam Singh ( trueleo )</div>
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
    </div>
  </div>
</template>

<style scoped>
@import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";

  .about {
    width: 100%;
    height: 100%;
    margin: 0 auto;
    transition: all 1s;
    /* display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center; */
  }

  .card {
    /* border-radius: 10px; */
    background: white;
    width: 40%;
    min-width: 32em;
    max-width: 35em;
    height: 44em;
    margin: 1em auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .profile {
    width: 40%;
    padding-left: 30px;
  }

  .profile img {
    width: 100%;
    height: auto;
  }

  .title {
    font-size: 3em;
    letter-spacing: 10px;
    line-height: 3em;
    font-weight: 600;
  }

  .version {
    padding: 10px 30px;
    background-color: black;
    color: white;
    font-size: 1.5em;
    font-weight: 100;
    line-height: 30px;
    letter-spacing: 2px;
  }

  .author {
    margin-top: 5em;
    font-size: 1.2em;
  }

  .links {
    margin-top: 10px;
    width: 50%;
    display: flex;
    justify-content: center;
  }

  .links a{
    color: black;
  }

  .links i {
    font-size: 3em;
    margin: 5px 12px;
    border-radius: 50%;
  }

</style>