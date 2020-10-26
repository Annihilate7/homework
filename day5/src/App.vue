<template>
    <div id="app">

        <h3>主页</h3>
        <router-link to="/note">
            <el-link type="primary" :underline="false">查看留言版</el-link>
        </router-link>
        <router-link to="/user">
            <el-link type="primary" :underline="false">查看用户表</el-link>
        </router-link>
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
