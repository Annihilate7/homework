<template>
    <div>
        <h4>用户详情页</h4>
        ID：{{$route.params.id}} <br>
        姓名：{{$route.params.username}} <br>
        年龄：{{$route.params.age}} <br>
        <button @click="goBack">返回上一页</button>
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
