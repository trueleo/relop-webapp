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
        <i class="fa fa-github"></i>
        <i class="fa fa-globe"></i>
        <i class="fa fa-telegram"></i>
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
  }

  .card {
    border-radius: 30px;
    background: white;
    width: 40%;
    min-width: 30em;
    max-width: 35em;
    height: 44em;
    margin: 2em auto;
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
    letter-spacing: 8px;
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
    margin-top: 3em;
    font-size: 1.2em;
  }

  .links {
    margin-top: 40px;
    width: 50%;
    display: flex;
    justify-content: center;
  }

  .links i {
    font-size: 4em;
    margin: 5px 12px;
    border-radius: 50%;
  }

</style>