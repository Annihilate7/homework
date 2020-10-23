<template>
    <div id="app">

        <h3>主页</h3>
        <router-link to="/note">查看留言板</router-link>
        <router-link to="/user">查看用户表</router-link>
        <hr>

        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'App'
}
</script>

<style>
#app {

}
</style>
