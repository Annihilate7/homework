<template>
    <div>
        <h4>用户详情页</h4>
        ID：{{$route.params.id}} <br>
        姓名：{{$route.params.username}} <br>
        年龄：{{$route.params.age}} <br><br>
        <el-button type="info" round @click="goBack">返回</el-button>
    </div>
</template>

<script>
export default {
    name: "Userdetail",
    methods: {
        goBack() {
            this.$router.go(-1);
        }
    },
}
</script>

<style scoped>

</style>
